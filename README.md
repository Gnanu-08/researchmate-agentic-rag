# ResearchMate — Provider-Independent Agentic RAG Assistant

ResearchMate is a submission-ready Agentic AI + RAG project. It supports OpenAI and Ollama through a common LLM provider interface.

## Features
- Agentic workflow: planner → retrieval → evidence evaluation → answer generation
- Retrieval Augmented Generation with ChromaDB
- Local sentence-transformer embeddings
- Provider-independent LLM layer
- OpenAI or Ollama
- Streamlit UI
- FastAPI API
- PDF/TXT/MD ingestion
- Source citations
- Basic tests

## Quick start

### 1. Create environment
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure
Copy `.env.example` to `.env`.

For OpenAI:
```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key
OPENAI_MODEL=gpt-4o-mini
```

For Ollama:
```env
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
```

Install Ollama separately and run:
```bash
ollama pull llama3.2
ollama serve
```

### 3. Add documents
Put PDF, TXT, or MD files into `data/documents/`.

Sample text files are already included.

### 4. Build the vector store
```bash
python -m app.rag.ingest
```

### 5. Run Streamlit
```bash
streamlit run frontend/streamlit_app.py
```

### 6. Run API
```bash
uvicorn app.main:app --reload
```

Open API docs at `/docs`.

## Architecture
```text
User
  |
Streamlit / FastAPI
  |
Agent Controller
  |
Planner
  |---- direct answer
  |
Retriever -> ChromaDB -> Evidence Evaluator
                     |
               insufficient?
                 /       \
               yes       no
                |         |
          refined search  |
                \        /
                 Answer Generator
                       |
                 cited response

LLM Provider Interface
       |             |
    OpenAI         Ollama
```

## Important design decision
Embeddings are kept local and deterministic through Sentence Transformers, while generation is provider-independent. This means switching LLM providers does not require rebuilding the vector store.

## Project structure
```text
app/
  agents/       planner, retriever, evaluator, generator, controller
  llm/          provider interface + OpenAI/Ollama adapters
  rag/          loading, chunking, embeddings, Chroma retrieval
  models/       Pydantic schemas
  main.py       FastAPI
frontend/       Streamlit
data/documents/ sample knowledge base
tests/          basic tests
```

## Example questions
- What documents are required for an internship application?
- What is the minimum attendance requirement?
- How many rounds are in the placement process?
- Compare internship and placement requirements.

## Disclaimer
Sample documents are fictional academic/demo material and should be replaced with your institution's real documents for a domain-specific deployment.
