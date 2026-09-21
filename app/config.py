import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "ollama").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2"
)
CHROMA_PATH = os.getenv("CHROMA_PATH", "./data/chroma")
COLLECTION_NAME = os.getenv("COLLECTION_NAME", "researchmate")
TOP_K = int(os.getenv("TOP_K", "5"))
MAX_RETRIEVAL_ATTEMPTS = int(os.getenv("MAX_RETRIEVAL_ATTEMPTS", "2"))
