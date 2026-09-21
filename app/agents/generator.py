from app.llm.factory import get_llm

def generate_answer(question: str, documents) -> str:
    if not documents:
        return "I could not find supporting information in the knowledge base."

    context = []
    for i, doc in enumerate(documents, 1):
        source = doc.metadata.get("source", "unknown")
        page = doc.metadata.get("page")
        label = f"{source}" + (f", page {page}" if page else "")
        context.append(f"[{i}] {label}\n{doc.page_content}")

    prompt = f'''You are the answer-generation component of a grounded RAG assistant.
Answer the question using ONLY the supplied evidence.
If the evidence does not contain the answer, say that the knowledge base does not provide enough information.
Do not invent facts.
Cite evidence inline using [1], [2], etc.

Question:
{question}

Evidence:
{chr(10).join(context)}
'''
    return get_llm().generate(prompt)
