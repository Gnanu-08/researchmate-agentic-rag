from app.agents.planner import plan
from app.agents.retriever import retrieve_evidence
from app.agents.evaluator import evaluate
from app.agents.generator import generate_answer
from app.config import MAX_RETRIEVAL_ATTEMPTS, LLM_PROVIDER
from app.models.schemas import AgentResponse, Source

def run_agent(question: str) -> AgentResponse:
    steps = []
    p = plan(question)
    steps.append(f"Planner: {p.action} — {p.reason}")

    if p.action == "answer":
        answer = generate_answer(question, [])
        return AgentResponse(answer=answer, steps=steps, provider=LLM_PROVIDER)

    docs = []
    query = p.search_query
    for attempt in range(MAX_RETRIEVAL_ATTEMPTS):
        steps.append(f"Retriever attempt {attempt + 1}: {query}")
        docs = retrieve_evidence(query)
        sufficient = evaluate(question, [d.page_content for d in docs])
        steps.append(f"Evidence evaluator: {'sufficient' if sufficient else 'insufficient'}")
        if sufficient:
            break
        query = question + " requirements eligibility documents rules details"

    answer = generate_answer(question, docs)
    sources = []
    seen = set()
    for d in docs:
        key = (d.metadata.get("source"), d.metadata.get("page"))
        if key not in seen:
            seen.add(key)
            sources.append(Source(
                source=key[0] or "unknown",
                page=key[1],
                content=d.page_content[:300]
            ))
    return AgentResponse(
        answer=answer,
        sources=sources,
        steps=steps,
        provider=LLM_PROVIDER
    )
