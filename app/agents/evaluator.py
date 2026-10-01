from app.llm.factory import get_llm


def evaluate(question: str, contexts: list[str]) -> bool:

    if not contexts:
        return False

    prompt = f"""You are an evidence evaluator in a Retrieval-Augmented Generation system.

Determine whether the retrieved evidence contains enough relevant information to answer the user's question.

Return YES only if the evidence contains information directly related to the main topic of the question.

Return NO if the evidence is unrelated, only shares generic words with the question, or does not contain enough information to answer it.

Return ONLY YES or NO.

Question:
{question}

Evidence:
{"".join(contexts)}
"""

    result = get_llm().generate(prompt).strip().upper()

    if result.startswith("YES"):
        return True

    if result.startswith("NO"):
        return False

    # Fallback: require at least two meaningful question terms
    # to appear in the retrieved evidence.
    stop_words = {
        "what", "which", "who", "how", "why", "when", "where",
        "can", "is", "are", "do", "does", "the", "a", "an",
        "for", "to", "of", "and", "in", "on", "with",
        "university", "policy", "requirements", "rules",
        "information", "details"
    }

    question_words = {
        word.strip("?,.!").lower()
        for word in question.split()
    }

    relevant_words = [
        word
        for word in question_words
        if len(word) > 4 and word not in stop_words
    ]

    evidence_text = " ".join(contexts).lower()

    matches = sum(
        1 for word in relevant_words
        if word in evidence_text
    )

    return matches >= 2
