from abc import ABC, abstractmethod

class LLMProvider(ABC):
    name = "base"

    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError
