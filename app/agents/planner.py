from app.llm.factory import get_llm
from app.models.schemas import Plan


SYSTEM = """You are the planning component of an Agentic RAG system.

Decide whether the user question can be answered without the knowledge base.

If it asks about facts likely contained in organizational documents, choose retrieve.

Return exactly:

action: retrieve|answer

QUERY: <search query>

REASON: <short reason>
"""


def plan(question: str, analysis: dict | None = None) -> Plan:
    llm = get_llm()

    context = ""

    if analysis:
        context = (
            "\nQUERY ANALYSIS:\n"
            f"Type: {analysis.get('query_type', 'general')}\n"
            f"Keywords: {', '.join(analysis.get('keywords', []))}\n"
        )

    raw = llm.generate(
        SYSTEM
        + context
        + "\nUSER QUESTION:\n"
        + question
    )

    action = "retrieve" if "action: retrieve" in raw.lower() else "answer"

    query = question
    reason = "The question may require knowledge-base evidence."

    for line in raw.splitlines():
        if line.upper().startswith("QUERY:"):
            query = line.split(":", 1)[1].strip() or question
        elif line.upper().startswith("REASON:"):
            reason = line.split(":", 1)[1].strip() or reason

    return Plan(
        action=action,
        search_query=query,
        reason=reason
    )
