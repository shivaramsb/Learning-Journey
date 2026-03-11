from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

llm = ChatBedrock(
    model_id="amazon.nova-pro-v1:0",
    region_name="us-east-1",
    model_kwargs={"temperature": 0.7, "max_tokens": 512},
)

history = [
    SystemMessage(content="You are a helpful AI assistant. Keep answers clear and concise.")
]

print("=" * 45)
print("   💬 LangChain Bedrock Chat (Nova Pro)")
print("   Type 'exit' or 'quit' to stop")
print("=" * 45)

while True:
    user_input = input("\n👤 You: ").strip()

    if not user_input:
        continue
    if user_input.lower() in ("exit", "quit"):
        print("👋 Bye!")
        break

    history.append(HumanMessage(content=user_input))
    response = llm.invoke(history)
    history.append(AIMessage(content=response.content))

    print(f"🤖 Bot: {response.content}")
