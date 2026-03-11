import json
import re
import boto3

def extract_json(text):
    """Extract the first JSON object found in the text, even if there's extra text around it."""
    # Strip markdown code fences if present (```json ... ``` or ``` ... ```)
    text = re.sub(r"```(?:json)?\s*", "", text).strip()
    # Find the first {...} block
    match = re.search(r"\{.*?\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    raise json.JSONDecodeError("No JSON object found", text, 0)

# AWS Bedrock client
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Amazon Nova Pro — Amazon's own frontier model
MODEL_ID = "amazon.nova-pro-v1:0"

system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final result.

Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input.
3. Carefully analyse the user query.
4. ALWAYS respond with a single valid JSON object only. No extra text outside the JSON.

Output Format:
{ "step": "string", "content": "string" }

Example:
Input: What is 2 + 2.
Output: { "step": "analyse", "content": "Alright! The user is interested in maths query and he is asking a basic arithmetic operation" }
Output: { "step": "think", "content": "To perform the addition i must go from left to right and add all the operands" }
Output: { "step": "output", "content": "4" }
Output: { "step": "validate", "content": "seems like 4 is correct ans for 2 + 2" }
Output: { "step": "result", "content": "2 + 2 = 4 and that is calculated by adding all numbers" }

"""

# Bedrock converse requires messages to strictly alternate: user → assistant → user → ...
# System prompt is passed separately. We start with the user's query.
query = input("> ")

messages = [
    {"role": "user", "content": [{"text": query}]}
]

MAX_THINKS = 3   # max "think" steps before we push the model forward
think_count = 0
step_count  = 0

# Ordered sequence the model should follow
SEQUENCE = ["analyse", "think", "output", "validate", "result"]

while True:
    response = client.converse(
        modelId=MODEL_ID,
        system=[{"text": system_prompt}],
        messages=messages,
    )

    reply_text = response["output"]["message"]["content"][0]["text"]

    # Append assistant reply to maintain alternating conversation history
    messages.append({"role": "assistant", "content": [{"text": reply_text}]})

    try:
        parsed_response = extract_json(reply_text)
    except json.JSONDecodeError:
        print(f"⚠️  Could not parse JSON: {reply_text}")
        break

    step    = parsed_response.get("step")
    content = parsed_response.get("content")
    step_count += 1

    if step == "think":
        think_count += 1

    if step == "result":
        print(f"🤖: {content}")
        break

    print(f"🧠: {content}")

    # Safety cap — stop if way too many steps
    if step_count >= 10:
        print("⚠️  Reached max steps limit.")
        break

    # After too many thinks, tell the model to move forward
    if step == "think" and think_count >= MAX_THINKS:
        next_step = "output"
        next_msg  = f"You have thought enough. Now provide the '{next_step}' step."
    elif step == "output":
        next_msg = "Now provide the 'validate' step."
    elif step == "validate":
        next_msg = "Now provide the 'result' step."
    else:
        next_msg = "continue"

    messages.append({"role": "user", "content": [{"text": next_msg}]})