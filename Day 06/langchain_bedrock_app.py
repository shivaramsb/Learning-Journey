"""
Sample Application using LangChain + AWS Bedrock (Amazon Nova Pro)
Demonstrates:
  1. Basic chat with ChatBedrock
  2. Prompt Templates + Chains (LCEL)
  3. Multi-turn conversation with message history
"""

from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# ── 1. Setup ChatBedrock ──────────────────────────────────────────────────────
llm = ChatBedrock(
    model_id="amazon.nova-pro-v1:0",
    region_name="us-east-1",
    model_kwargs={"temperature": 0.7, "max_tokens": 512},
)

print("=" * 55)
print("   LangChain + AWS Bedrock — Amazon Nova Pro Demo")
print("=" * 55)


# ── 2. Basic Chat ─────────────────────────────────────────────────────────────
print("\n📌 Example 1: Basic Chat")
print("-" * 35)

messages = [
    SystemMessage(content="You are a helpful assistant. Keep answers short and clear."),
    HumanMessage(content="What is AWS Bedrock in one sentence?"),
]

response = llm.invoke(messages)
print(f"🤖 {response.content}")


# ── 3. Prompt Template + Chain (LCEL) ─────────────────────────────────────────
print("\n📌 Example 2: Prompt Template + Chain")
print("-" * 35)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in {domain}. Answer concisely."),
    ("human",  "{question}"),
])

chain = prompt | llm  # LangChain Expression Language (LCEL)

result = chain.invoke({
    "domain":   "cloud computing",
    "question": "What are the top 3 benefits of serverless architecture?",
})
print(f"🤖 {result.content}")


# ── 4. Multi-turn Conversation ────────────────────────────────────────────────
print("\n📌 Example 3: Multi-turn Conversation")
print("-" * 35)

history = [
    SystemMessage(content="You are a friendly travel guide. Keep responses brief."),
]

turns = [
    "Suggest a great country to visit in Asia.",
    "What is the best time of year to go there?",
    "Give me one must-try local food.",
]

for user_input in turns:
    history.append(HumanMessage(content=user_input))
    reply = llm.invoke(history)
    history.append(AIMessage(content=reply.content))
    print(f"👤 {user_input}")
    print(f"🤖 {reply.content}\n")

print("=" * 55)
print("✅ Done!")
