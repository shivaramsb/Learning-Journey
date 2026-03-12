"""
RAG Implementation using AWS Bedrock (Embeddings + LLM) and PostgreSQL (pgvector)
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# LangChain Imports
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_aws import BedrockEmbeddings, ChatBedrock
from langchain_postgres.vectorstores import PGVector

# Load environment variables
load_dotenv()

# ── 1. Load and Split Document ───────────────────────────────────────────────
pdf_path = Path("Fundamentals of Data Engineering.pdf")

if not pdf_path.exists():
    print(f"File not found: {pdf_path}. Please ensure the PDF is in the directory.")
    exit(1)

print("Loading PDF...")
loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

print("Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
split_docs = text_splitter.split_documents(docs)
print(f"Generated {len(split_docs)} chunks.")

# ── 2. AWS Bedrock Setup ───────────────────────────────────────────────────
# Use Amazon Titan Text Embeddings V2
print("Initializing Bedrock Embeddings (Amazon Titan)...")
embedder = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0",
    region_name="us-east-1"
)

# ── 3. PGVector Store Setup ────────────────────────────────────────────────
# Connection string for your AWS PGVector Database (RDS / Aurora)
aws_host = os.getenv("AWS_PGVECTOR_URL")
pg_port  = os.getenv("PG_PORT", "5432")
pg_db    = os.getenv("PG_DBNAME", "postgres")
pg_user  = os.getenv("your_db_username")
pg_pass  = os.getenv("PG_PASSWORD")

if aws_host and pg_user and pg_pass:
    DB_CONNECTION = f"postgresql+psycopg://{pg_user}:{pg_pass}@{aws_host}:{pg_port}/{pg_db}"
else:
    # Fallback to direct URL if the env var already contains the full connection string
    DB_CONNECTION = os.getenv("AWS_PGVECTOR_URL", "postgresql+psycopg://user:pass@host:5432/dbname")

COLLECTION_NAME = "data_engineering_collection"

# Check if we should inject (only need to do this once)
print(f"Connecting to Postgres DB at {aws_host}...")
vector_store = PGVector(
    embeddings=embedder,
    collection_name=COLLECTION_NAME,
    connection=DB_CONNECTION,
)

# Optional: Add an arg or check to skip injection if already done
INJECT_DOCS = False  # Set to True if the PDF changed
if INJECT_DOCS:
    print(f"Injecting {len(split_docs)} documents in batches...")
    BATCH_SIZE = 50
    for i in range(0, len(split_docs), BATCH_SIZE):
        batch = split_docs[i : i + BATCH_SIZE]
        vector_store.add_documents(batch)
        print(f"  -> Added {i + len(batch)} / {len(split_docs)} chunks...")
    print("Injection Done!")
else:
    print("Skipping PDF injection (already in DB).")

# ── 4. Retrieval and Generation ────────────────────────────────────────────
print("\n" + "=" * 50)
print("  📚  AWS Bedrock RAG Chat (Nova Pro + PGVector)")
print("  Type 'exit' or 'quit' to stop")
print("=" * 50)

# Set up Retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 3})

# Initialize Bedrock LLM (Amazon Nova Pro)
llm = ChatBedrock(
    model_id="amazon.nova-pro-v1:0",
    region_name="us-east-1",
    model_kwargs={"temperature": 0.3}
)

while True:
    query = input("\n👤 You: ").strip()
    
    if not query:
        continue
    if query.lower() in ("exit", "quit"):
        print("👋 Bye!")
        break

    # 1. Retrieve relevant chunks from PGVector
    print("   🔍 Searching database...", end="\r")
    relevant_chunks = retriever.invoke(query)
    
    # Combine retrieved context
    context = "\n\n".join([doc.page_content for doc in relevant_chunks])

    SYSTEM_PROMPT = f"""
    You are an expert Data Engineering instructor.
    Use the following pieces of retrieved context to answer the question.
    If you don't know the answer based on the context, just say that you don't know.

    Context:
    {context}
    """

    # 2. Generate response via Bedrock LLM
    from langchain_core.messages import HumanMessage, SystemMessage
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=query)
    ]
    
    print("   🤖 Generating answer...  ", end="\r")
    response = llm.invoke(messages)

    # 3. Print answer
    print("\n🤖 Bot: " + response.content)
    # Optional: print(f"\n   [Source chunks used: {len(relevant_chunks)}]")
