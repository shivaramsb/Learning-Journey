# 🚀 Full Stack Generative AI Bootcamp

The **Full-Stack Generative AI BootCamp** is a **5–6 month, industry-focused program** designed for AI engineers, software developers, and tech professionals who want to move beyond theory and learn how to build, deploy, and scale real-world GenAI systems.

> This is not a “prompting-only” course. You will master the complete modern GenAI stack—**LLMs + Fine-Tuning + RAG + Agents + Guardrails + Evaluation + LLMOps + Cloud Deployment**—and learn to ship production-grade AI applications on platforms like **AWS** and **Azure**.

By the end of the bootcamp, you won’t just understand Generative AI—you’ll be able to **architect and deploy enterprise-ready systems** like RAG-powered document portals and autonomous multi-agent report generation pipelines, complete with safety controls, evaluations, monitoring, and scalable deployments.

---

## 📚 What You Will Learn

Master the complete **Full-Stack Generative AI lifecycle** from transformer foundations and model selection to fine-tuning, RAG systems, agent orchestration, guardrails, evaluation, and scalable cloud-native deployment on AWS/Azure.

### 🧠 LLM Foundations & Core Concepts
Understand what powers modern LLMs from the ground up. Learn **Transformer architecture**, how attention works, and why LLMs generalize so well. Build strong fundamentals in **tokenization, text encoding, embeddings, vector similarity**, and the evolution from classical NLP to modern contextual representations.

### 🌐 LLM Ecosystem & Model Selection
Navigate the complete landscape of modern models — **LLMs vs SLMs vs Multimodal models**. Compare and understand major model families like **GPT, Gemini, Claude, LLaMA, Mistral, Qwen**, plus efficient SLMs like **Phi & Gemma**. Learn a practical **model selection framework** based on task type, latency, cost, deployment feasibility, and modality (text / code / vision).

### 🔌 LLM APIs, Streaming & Provider Abstraction
Work hands-on with real commercial API ecosystems like **OpenAI, Anthropic, Gemini, Groq, and Open Router**. Learn how to structure production calls (system/user prompts, parameters like temperature/max tokens), implement **streaming responses**, handle retries, and track token usage. Build **abstraction layers** to switch providers seamlessly without rewriting your application logic.

### ⚙️ Fine-Tuning (LoRA / QLoRA / PEFT)
Go beyond prompt engineering and learn how to adapt models for your own domain. Master **full fine-tuning vs parameter-efficient fine-tuning (PEFT)**, including **LoRA** and **QLoRA**. Learn dataset preparation (instruction formatting, splits, cleaning), modern tooling like **Hugging Face Transformers + PEFT, Unsloth, Axolotl**, and advanced concepts like **RLHF, DPO/ORPO/GRPO**.

### 🔍 Production RAG Systems (Vector DB + Re-Ranking)
Build complete **Retrieval-Augmented Generation** pipelines that reduce hallucinations and deliver grounded answers. Learn ingestion and parsing (PDFs, docs, web), **chunking strategies**, embedding selection, metadata filtering, and vector DB integrations with **Pinecone/Qdrant/Chroma**. Implement robust retrieval workflows including **similarity search, MMR, and cross-encoder re-ranking**, plus citation-aware prompting.

### ⚡ Advanced RAG & Multimodal Systems
Take RAG from demo → production. Learn **context engineering**, context window optimization, **caching strategies** (response cache, embedding cache, CAG), and reliability evaluation methods (faithfulness, relevance, retrieval quality). Extend systems to **multimodal RAG** (text + image grounding) and debug common RAG failure modes.

### 🤖 Agentic AI + LangGraph Orchestration
Design autonomous AI systems that do more than chat. Learn to build **single-agent and multi-agent architectures**, including supervisor, hierarchical, and network-based systems. Implement tool use (APIs, functions, search, RAG), memory + state management, and **human-in-the-loop** workflows. Learn orchestration layers through frameworks like **LangGraph** (and CrewAI/AutoGen conceptually).

### 🛡️ Guardrails, Evaluation & Cloud Deployment
Ship production-safe GenAI applications with quality control. Learn **observability** (logging/tracing) and evaluation strategies like **LLM-as-a-judge**. Implement guardrails for input/output validation, **schema enforcement (Pydantic)**, refusal logic, and prompt injection defense. Finally, containerize and deploy using **AWS ECS/Fargate, SageMaker**, and **API Gateway**.

---

## 🛠️ Projects You'll Build

In this bootcamp, you’ll gain real production experience by building end-to-end GenAI applications.

### 📂 Project 1: Intelligent Document Portal (End-to-End RAG Deployment)
> **Build a production-grade Document Intelligence Portal** that can ingest large document collections and answer questions with grounded, citation-backed outputs.
> *   **Pipeline:** Upload → Parse → Chunk → Embed → Index → Retrieve → Generate.
> *   **Features:** Query rewriting, MMR retrieval, re-ranking, multi-document chat, document comparison.
> *   **Tech:** Redis caching (CAG), Evaluation + Guardrails, AWS ECS/Fargate deployment with CI/CD + Observability.

### 📂 Project 2: Autonomous Report Generation System (Multi-Agent Deployment)
> **Build a complete multi-agent AI system** that researches, analyses, and generates structured reports like a real AI analyst team.
> *   **Agents:** Search, Reader, Analyst, Generator, Coordinator.
> *   **Orchestration:** LangGraph / CrewAI / AutoGen-style state workflows.
> *   **Features:** Shared memory, tool-calling, RAG grounding, human-in-the-loop checkpoints.
> *   **Tech:** FastAPI dispatcher, report preview UI, complete traces/logs.

---

## 📜 Detailed Syllabus

### 1️⃣ Foundations of Modern GenAI
1. **Introduction to Modern Generative AI & LLMs:** What GenAI is and how LLMs work at a high level.
2. **Transformer Architecture (Core Concept):** Why transformers are the backbone of modern LLMs.
3. **Text Encoding & Tokenization:** Why text must be encoded, tokenization basics, vocabulary creation, subword tokens.
4. **Evolution of Text Representations:** Classical encoding techniques and the shift to word embeddings.
5. **Embeddings, Vector Space & Similarity:** Word, contextual, and sentence embeddings, vector space representation, similarity measures.

### 2️⃣ Understanding LLMs, SLMs & MultiModal LLMs
1. **LLMs vs SLMs vs Multimodal Models:** High-level differentiation and purpose of each category.
2. **Major LLM Families:** GPT, Gemini, Claude, LLaMA, Mistral, Qwen.
3. **Small & Efficient Language Models (SLMs):** Phi, Gemma and their low-cost / low-latency use cases.
4. **Specialized Models (Code & Multimodal):** CodeLLaMA, StarCoder, DeepSeek-Coder, LLaVA, BLIP, CLIP.
5. **Model Selection Strategy:** Choosing the right model based on task type, cost, latency, modality, and deployment needs.

### 3️⃣ API for Accessing LLMs
1. **LLM API Ecosystem Overview:** OpenAI, Anthropic, Gemini, Groq, OpenRouter.
2. **Making LLM API Calls (Core Hands-On):** Prompt → request → response, parameters (temperature, max tokens), streaming vs non-streaming.
3. **Token Usage, Cost & Latency Management:** Token counting, pricing models, cost control strategies.
4. **Provider Switching & Abstraction Layer:** OpenAI ↔ Groq ↔ OpenRouter using the same code structure.
5. **Cloud-Managed LLM APIs:** Azure OpenAI, AWS Bedrock, GCP Vertex AI (Enterprise usage).

### 4️⃣ Fine-Tuning Techniques
1. **Foundations of Fine-Tuning:** Fine-tuning in classical DL vs transformers.
2. **Fine-Tuning Landscape:** Hugging Face ecosystem vs LangChain integration.
3. **Fine-Tuning Strategies:** Full fine-tuning vs parameter-efficient approaches.
4. **Parameter-Efficient Fine-Tuning (PEFT):** LoRA, QLoRA, PEFT overview and usage.
5. **Dataset Preparation:** Instruction datasets, formatting, cleaning, train/validation splits.
6. **Advanced Optimization:** Knowledge distillation and quantization.
7. **Frameworks & Tooling:** Hugging Face Transformers, PEFT, Unsloth, Axolotl.
8. **API-Based Fine-Tuning:** OpenAI / provider-based workflows.
9. **Model Packaging & Distribution:** Hugging Face checkpoints, Safetensors, GGUF, GGML.
10. **Advanced Paradigms:** RLHF, DPO, ORPO, GRPO (Conceptual).
11. **Specialized Fine-Tuning:** Embedding models and vision-language models.

### 5️⃣ LLM Hosting & Deployment
1. **Fine-Tuning on AWS SageMaker:** LoRA-based fine-tuning using managed infrastructure.
2. **Deploying LLMs as SageMaker Endpoints:** Real-time inference endpoints and scaling.
3. **API Exposure & Traffic Management:** API Gateway or ALB integration.
4. **Inference Compute Options:** AWS Lambda (lightweight), ECS Fargate (container-based).
5. **Client Integration:** Connecting frontend/backend apps to deployed LLMs.

### 6️⃣ Prompt Engineering
1. **Core Prompting Concepts:** System vs User prompts, zero-shot, few-shot prompting.
2. **Reasoning-Based Techniques:** Chain-of-Thought (CoT), self-consistency, ReAct.
3. **Prompt Design Strategies:** Task-wise and domain-specific prompting.
4. **Production-Grade Management:** Prompt libraries, Jinja2 templates, YAML configurations.
5. **Structured & Controlled Prompting:** JSON/YAML outputs, schema enforcement.
6. **Optimization:** Token cost optimization and context window management.

### 7️⃣ Retrieval-Augmented Generation (RAG) Systems
1. **Why RAG is Needed:** Overcoming hallucinations and grounding with external knowledge.
2. **End-to-End RAG Architecture:** Ingestion → Indexing → Retrieval → Generation.
3. **Data Ingestion & Parsing:** Handling PDFs, docs, web data (structured vs unstructured).
4. **Chunking Strategies:** Optimization and overlap trade-offs.
5. **Embeddings & Vector Databases:** Vector DB types (local, open-source, managed).
6. **Metadata Design & Filtering:** Scoped retrieval strategies.
7. **Retrieval, Ranking & Re-Ranking:** Similarity search, MMR, cross-encoder re-ranking.
8. **Prompting with Context:** Context injection, grounding, citation-aware prompting.

### 8️⃣ Advanced RAG & Multimodal Systems
1. **Context Engineering & Memory:** Context window control, memory vs retrieval.
2. **Caching & Performance:** Response caching, embedding cache, CAG.
3. **RAG Evaluation:** Faithfulness, relevance, retrieval quality metrics.
4. **Multimodal RAG:** Text + image retrieval, vision-language grounding.
5. **Common Failure Modes:** Debugging bad chunks, noisy retrieval, and missing context.

### 9️⃣ Agents, Multi-Agent & Deep Agent Systems
1. **Agentic AI Fundamentals:** Agents vs simple LLM pipelines.
2. **Single-Agent Architectures:** Planning, reasoning, and acting loops.
3. **Multi-Agent System Designs:** Supervisor, hierarchical, and network-based architectures.
4. **Deep Agent Systems:** Long-horizon agents with planning and reflection.
5. **LLMs as the Reasoning Core:** Decision-making and tool selection.
6. **Tools as Agent Interfaces:** APIs, functions, search, code execution.
7. **Agent Orchestration Layers:** LangGraph / CrewAI concepts.
8. **Memory & State Management:** Short-term vs long-term memory.
9. **Prompting Strategies for Agents:** Role-based, planner, and executor prompts.
10. **Human-in-the-Loop:** Approval gates, feedback loops, interrupt & resume.
11. **Safety Controls:** Loop prevention, max steps, error handling.
12. **Cost & Execution Management:** Token budgeting and execution limits.
13. **Agentic RAG:** Combining agents with retrieval.
14. **Inter-Agent Collaboration:** Task delegation and conflict resolution.

### 🔟 Evaluation Strategies
1. **Observability & Debugging:** Logging, monitoring, tracing prompts/tools.
2. **Why Classical Evaluation Breaks:** Limitations of traditional ML metrics.
3. **Model vs System Evaluation:** Distinguishing model performance from system quality.
4. **Core Strategies:** LLM-as-a-judge, human-in-the-loop, offline vs online eval.
5. **Evaluating RAG & Agents:** Grounding, relevance, hallucination detection.
6. **System-Level Metrics:** Cost, latency, UX, quality–speed–cost trade-offs.
7. **Classical Metrics:** Perplexity, BLEU, ROUGE (limitations).
8. **Evaluation Anti-Patterns:** Avoiding single-metric obsession.

### 1️⃣1️⃣ Guardrails
1. **Foundations of Guardrails:** Safety, reliability, and compliance.
2. **Traditional vs GenAI Guardrails:** Validation constraints.
3. **Input Validation:** Prompt sanitization, length limits, content filtering.
4. **Output Validation:** Response checks, format enforcement, refusal logic.
5. **Schema-Based Guardrails:** Pydantic-based schemas.
6. **Prompt Injection Defense:** Attack types and mitigation strategies.
7. **Tools & Frameworks:** Guardrails.ai, OpenAI Guardrails.

### 1️⃣2️⃣ MCP (Model Context Protocol)
1. **Introduction to MCP:** Purpose and origin.
2. **Why MCP:** Comparison with plugins and function calling.
3. **MCP in GenAI:** Integration with RAG and agents.
4. **Architecture:** Client ↔ Server ↔ LLM interaction.
5. **Core Components:** Host, Client, Server.
6. **Transports:** STDIO, SSE, Streamable HTTP.
7. **Python SDK:** FastMCP, CLI tools.
8. **Building MCP Servers:** Project structure and lifecycel.
9. **Capabilities:** Tools, structured outputs, reusable prompts.
10. **Advanced Concepts:** Auth, pagination, large data handling.
11. **MCP for Agentic Systems:** As a tool layer for multi-agent systems.

### 1️⃣3️⃣ Cloud Services (AWS)
1. **Core ML Platform:** Amazon SageMaker.
2. **Generative AI & Intelligent Agents:** Amazon Bedrock, Agent Core, OpenSearch.
3. **Specialized AI Services:** Textract, Comprehend, Rekognition, Transcribe.

### 1️⃣4️⃣ No-Code Agent Tools (n8n)
1. **AI Automation with n8n:** Introduction and fit.
2. **Basic Setup:** Nodes, workflows, JSON handling.
3. **APIs & AI:** Calling APIs, using LLMs.
4. **Agent Patterns:** Chain, parallel, controller flows.
5. **RAG with n8n:** Integration with vector DBs.
6. **MCP + n8n:** Cloud vs self-hosted.
7. **Use Cases:** Social media, GitHub, WhatsApp automation.

---

## 🏗️ End-to-End Project Breakdown

### **Project 1: Document Portal System** (Deployment Focus)
*   **Document Ingestion:** Upload → Parse → Chunk → Embed → Index.
*   **Advanced RAG:** Query rewriting, MMR, Re-ranking.
*   **Chat Features:** Context condensation, source-grounded responses.
*   **Collaboration:** Document comparison engine.
*   **Orchestration:** Model routing (Groq/OpenAI).
*   **Optimization:** CAG, Redis caching.
*   **Reliability:** Retries, fallbacks, autoscaling.
*   **Deployment:** AWS ECS, S3, RDS, Vector DB, CI/CD.

### **Project 2: Autonomous Report Generation System** (Agent Focus)
*   **Foundations:** Async orchestration, multi-agent roles.
*   **Roles:** Search, Reader, Analyst, Generator, Coordinator.
*   **Frameworks:** LangGraph / CrewAI state graphs.
*   **Memory:** Shared state, context control.
*   **Tools:** Web search, Arxiv parsers.
*   **RAG Integration:** Grounded research with citations.
*   **Human-in-the-Loop:** Feedback and approvals.
*   **Backend/UI:** FastAPI dispatcher, report previews, traces.

---

## 🎯 Skills You Will Acquire

| Core Foundations | Advanced Techniques | Production Engineering |
| :--- | :--- | :--- |
| ✅ Transformer Fundamentals | ✅ PEFT (LoRA / QLoRA) | ✅ End-to-End RAG Architecture |
| ✅ Tokenization & Embeddings | ✅ Fine-Tuning Strategies | ✅ Vector Databases (Pinecone, Qdrant) |
| ✅ LLM/SLM Selection | ✅ Multi-Agent Orchestration | ✅ Caching & Optimization (Redis) |
| ✅ Prompt Engineering (CoT, ReAct) | ✅ Agentic Logic & State | ✅ LLM-as-a-Judge Evaluation |
| ✅ API Integration & Streaming | ✅ Guardrails & Safety | ✅ Cloud Deployment (AWS ECS, SageMaker) |

**Tools & Formats:** `OpenAI` `Semanting Kernel` `LangGraph` `Hugging Face` `Safetensors` `GGUF` `Docker` `AWS` `Azure`