from app.llm.factory import get_llm

def evaluate(question: str, contexts: list[str]) -> bool:
    if not contexts:
        return False
    prompt = f'''Evaluate whether the evidence below is sufficient to answer the question.
Return only YES or NO.

Question: {question}

Evidence:
{chr(10).join(contexts)}
'''
    result = get_llm().generate(prompt).strip().upper()
    return result.startswith("YES")
