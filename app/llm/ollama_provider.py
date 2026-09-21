from langchain_ollama import ChatOllama
from .base import LLMProvider
from app.config import OLLAMA_BASE_URL, OLLAMA_MODEL

class OllamaProvider(LLMProvider):
    name = "ollama"

    def __init__(self):
        self.llm = ChatOllama(
            model=OLLAMA_MODEL,
            base_url=OLLAMA_BASE_URL,
            temperature=0
        )

    def generate(self, prompt: str) -> str:
        return self.llm.invoke(prompt).content
