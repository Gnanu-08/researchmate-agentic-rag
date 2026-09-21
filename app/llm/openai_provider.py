from langchain_openai import ChatOpenAI
from .base import LLMProvider
from app.config import OPENAI_API_KEY, OPENAI_MODEL

class OpenAIProvider(LLMProvider):
    name = "openai"

    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required when LLM_PROVIDER=openai")
        self.llm = ChatOpenAI(
            model=OPENAI_MODEL,
            api_key=OPENAI_API_KEY,
            temperature=0
        )

    def generate(self, prompt: str) -> str:
        return self.llm.invoke(prompt).content
