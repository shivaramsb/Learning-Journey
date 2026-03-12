import json
import re
import requests
import boto3

from botocore.config import Config

# ── AWS Bedrock client ─────────────────────────────────────────────────────────
# Increase timeout because Amazon Nova Pro reasoning can sometimes take > 60s
config = Config(read_timeout=120, retries={'max_attempts': 3})
client = boto3.client("bedrock-runtime", region_name="us-east-1", config=config)
MODEL_ID = "amazon.nova-pro-v1:0"

# ── Tool definitions ───────────────────────────────────────────────────────────
def get_weather(city: str):
    print(f"🔨 Tool Called: get_weather → {city}")
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is {response.text}."
    return "Something went wrong fetching the weather."

def run_command(command: str):
    import os
    print(f"🔨 Tool Called: run_command → {command}")
    result = os.popen(command).read()
    return result or "(no output)"

available_tools = {
    "get_weather": {
        "fn": get_weather,
        "description": "Takes a city name as input and returns the current weather for the city",
    },
    "run_command": {
        "fn": run_command,
        "description": "Takes a shell command as input, executes it on the system and returns the output",
    },
}

# ── System prompt ──────────────────────────────────────────────────────────────
system_prompt = """
You are a helpful AI Assistant specialized in resolving user queries.
You work in: start → plan → action → observe → output mode.

For EVERY new user query, you MUST plan step-by-step execution and use tools.
Do NOT assume a new query is already resolved just because you answered a previous one.
Based on planning, select the relevant tool and call it (action step).
Wait for the observation, then resolve the user query in the output step.

Rules:
- ALWAYS output a single valid JSON object. No text outside the JSON.
- Always perform ONE step at a time.
- Carefully analyse the user query.
- If the user asks for weather in a new city, you MUST output an "action" step to call get_weather. Do NOT skip tool calling.

Output JSON Format:
{ "step": "string", "content": "string", "function": "function name if step is action", "input": "function input if step is action" }

Available Tools:
- get_weather: Takes a city name as input and returns the current weather for the city
- run_command: Takes a shell command as input and returns the output

Example:
User Query: What is the weather of New York?
Output: { "step": "plan", "content": "The user wants weather data for New York." }
Output: { "step": "plan", "content": "I should call get_weather with 'New York'." }
Output: { "step": "action", "content": "Calling get_weather", "function": "get_weather", "input": "New York" }
Output: { "step": "observe", "content": "12 Degree Celsius, Clear" }
Output: { "step": "output", "content": "The weather in New York is 12°C and clear." }
"""

def extract_json(text: str) -> dict:
    """Extract the first JSON object from text, handles markdown fences and extra commentary."""
    text = re.sub(r"```(?:json)?\s*", "", text).strip()
    match = re.search(r"\{.*?\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise json.JSONDecodeError("No JSON object found", text, 0)

# ── Bedrock requires strictly alternating user/assistant messages.
# ── System prompt goes in the separate `system` param.
# ── We maintain a flat messages list and inject "continue" or observation turns.

print("=" * 50)
print("  🌤️  Weather Agent — AWS Bedrock (Nova Pro)")
print("  Type 'exit' to quit")
print("=" * 50)

while True:
    user_query = input("\n> ").strip()
    if user_query.lower() in ("exit", "quit"):
        print("👋 Bye!")
        break

    # Start fresh conversation for each user query
    messages = [
        {"role": "user", "content": [{"text": user_query}]}
    ]

    step_count = 0
    plan_count = 0
    MAX_PLAN_STEPS = 3

    while True:
        step_count += 1
        
        # Hard limit on turns to prevent infinite loops completely
        if step_count > 15:
            print("⚠️ Agent reached maximum turn limit (15).")
            break

        response = client.converse(
            modelId=MODEL_ID,
            system=[{"text": system_prompt}],
            messages=messages,
        )

        reply_text = response["output"]["message"]["content"][0]["text"]

        # Append assistant reply
        messages.append({"role": "assistant", "content": [{"text": reply_text}]})

        try:
            parsed_output = extract_json(reply_text)
        except json.JSONDecodeError:
            print(f"⚠️ Could not parse JSON: {reply_text}")
            break

        step = parsed_output.get("step")

        # ── PLAN ──────────────────────────────────────────────────────────────
        if step == "plan":
            plan_count += 1
            print(f"🧠 Plan: {parsed_output.get('content')}")
            
            # Force the model to move forward if it's stuck planning
            if plan_count >= MAX_PLAN_STEPS:
                messages.append({"role": "user", "content": [{"text": "You have planned enough. You MUST now proceed to either 'action' or 'output'."}]})
            else:
                messages.append({"role": "user", "content": [{"text": "continue"}]})
            continue
        
        # Reset plan count if we move past planning
        plan_count = 0

        # ── ACTION ────────────────────────────────────────────────────────────
        if step == "action":
            tool_name  = parsed_output.get("function")
            tool_input = parsed_output.get("input")

            if tool_name in available_tools:
                tool_result = available_tools[tool_name]["fn"](tool_input)
                # Inject the observation back as a user turn
                observe_msg = json.dumps({"step": "observe", "content": str(tool_result)})
                messages.append({"role": "user", "content": [{"text": observe_msg}]})
            else:
                messages.append({"role": "user", "content": [{"text": f"Tool '{tool_name}' not found. continue"}]})
            continue

        # ── OUTPUT ────────────────────────────────────────────────────────────
        if step == "output":
            print(f"🤖 {parsed_output.get('content')}")
            break

        # ── OBSERVE (model generated observe itself) ──────────────────────────
        if step == "observe":
            messages.append({"role": "user", "content": [{"text": "continue"}]})
            continue

        # Fallback — unknown step
        print(f"⚠️ Unknown step '{step}': {parsed_output}")
        break