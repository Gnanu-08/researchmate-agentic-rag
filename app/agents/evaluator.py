from app.llm.factory import get_llm


def evaluate(question: str, contexts: list[str]) -> bool:
    if not contexts:
        return False

    prompt = f"""You are an evidence evaluator in a Retrieval-Augmented Generation system.

Determine whether the retrieved evidence contains enough relevant information to answer the user's question.

If the evidence contains information directly related to the question, return YES.
If the evidence is completely unrelated or contains no useful information, return NO.

Return ONLY YES or NO.

Question:
{question}

Evidence:
{"".join(contexts)}
"""

    result = get_llm().generate(prompt).strip().upper()

    if result.startswith("YES"):
        return True

    # Fallback: accept clearly relevant retrieved evidence.
    question_words = set(question.lower().split())
    evidence_text = " ".join(contexts).lower()

    relevant_words = [
        word.strip("?,.!") for word in question_words
        if len(word.strip("?,.!")) > 4
    ]

    matches = sum(1 for word in relevant_words if word in evidence_text)

    return matches >= 1
