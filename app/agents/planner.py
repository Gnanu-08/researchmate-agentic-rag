from app.llm.factory import get_llm
from app.models.schemas import Plan

SYSTEM = '''You are the planning component of an Agentic RAG system.
Decide whether the user question can be answered without the knowledge base.
If it asks about facts likely contained in organizational documents, choose retrieve.
Return exactly:
ACTION: retrieve|answer
QUERY: <search query>
REASON: <short reason>
'''

def plan(question: str) -> Plan:
    llm = get_llm()
    raw = llm.generate(SYSTEM + "\nUSER QUESTION:\n" + question)
    action = "retrieve" if "ACTION: retrieve" in raw.lower() else "answer"
    query = question
    reason = "The question may require knowledge-base evidence."
    for line in raw.splitlines():
        if line.upper().startswith("QUERY:"):
            query = line.split(":", 1)[1].strip() or question
        elif line.upper().startswith("REASON:"):
            reason = line.split(":", 1)[1].strip() or reason
    return Plan(action=action, search_query=query, reason=reason)
