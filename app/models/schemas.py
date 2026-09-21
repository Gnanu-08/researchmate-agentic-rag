from typing import List, Literal
from pydantic import BaseModel, Field

class Plan(BaseModel):
    action: Literal["retrieve", "answer"]
    search_query: str = ""
    reason: str = ""

class Source(BaseModel):
    source: str
    page: int | None = None
    content: str = ""

class AgentResponse(BaseModel):
    answer: str
    sources: List[Source] = Field(default_factory=list)
    steps: List[str] = Field(default_factory=list)
    provider: str
