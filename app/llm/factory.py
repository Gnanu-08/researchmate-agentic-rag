from .openai_provider import OpenAIProvider
from .ollama_provider import OllamaProvider
from app.config import LLM_PROVIDER

def get_llm():
    if LLM_PROVIDER == "openai":
        return OpenAIProvider()
    if LLM_PROVIDER == "ollama":
        return OllamaProvider()
    raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
