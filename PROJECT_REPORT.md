# ResearchMate — Agentic AI + RAG Project Report

## 1. Abstract
ResearchMate is a provider-independent Agentic AI research assistant that combines Retrieval Augmented Generation (RAG) with a multi-step agent workflow. The system retrieves relevant knowledge-base evidence, evaluates whether the evidence is sufficient, optionally refines retrieval, and generates a grounded response with source references. The generation layer supports both OpenAI and locally hosted Ollama models through a common interface.

## 2. Problem Statement
Traditional question-answering systems may hallucinate when they lack domain-specific information. A pure RAG pipeline retrieves information but does not explicitly reason about whether retrieval is necessary or sufficient. ResearchMate addresses this by introducing planning and evidence evaluation around the RAG pipeline.

## 3. Objectives
- Build an Agentic AI workflow.
- Implement RAG over institutional documents.
- Reduce unsupported answers through evidence grounding.
- Provide source visibility.
- Support cloud and local LLM providers without changing agent code.
- Provide a usable web interface and REST API.

## 4. Architecture
Planner → Retriever → Evidence Evaluator → Answer Generator.

The LLM provider abstraction is independent of the agent logic. ChromaDB stores document embeddings and Sentence Transformers produces local embeddings.

## 5. Methodology
1. Load PDF/TXT/MD documents.
2. Split documents into overlapping chunks.
3. Generate embeddings.
4. Store chunks in ChromaDB.
5. Analyze the user query.
6. Retrieve top-k relevant chunks when required.
7. Evaluate evidence sufficiency.
8. Refine the query if evidence is insufficient.
9. Generate a grounded answer with citations.
10. Display the answer, sources, and agent trace.

## 6. Technologies
Python, FastAPI, Streamlit, LangChain, ChromaDB, Sentence Transformers, PyPDF, OpenAI, Ollama.

## 7. Advantages
- Provider independence.
- Local embeddings.
- Transparent agent trace.
- Source-grounded answers.
- Easy document replacement.
- REST API and web UI.

## 8. Limitations
- Retrieval quality depends on document quality and chunking.
- Local LLM response quality depends on the selected model and hardware.
- Source citations are evidence references, not guarantees of factual correctness.
- Demo documents are fictional and must be replaced for real institutional deployment.

## 9. Future Scope
- Add web search as an optional tool.
- Add reranking models.
- Add conversation memory.
- Add authentication and role-based access.
- Add evaluation metrics such as retrieval recall and answer faithfulness.
- Add document upload from the UI.
- Add support for additional LLM providers.

## 10. Conclusion
ResearchMate demonstrates how Agentic AI can be combined with RAG to create a grounded knowledge assistant. The provider abstraction makes the system flexible enough to use either cloud-based or local language models while keeping the agent workflow unchanged.
