from typing import Dict, List


def analyze_query(question: str) -> Dict:
    """
    Analyze a user question before retrieval.

    Returns:
        query_type: type of question
        keywords: important terms for retrieval
        needs_retrieval: whether document retrieval is required
    """

    question = question.strip()

    lower_question = question.lower()

    if lower_question.startswith(("what", "which", "who")):
        query_type = "fact"
    elif lower_question.startswith(("how", "why")):
        query_type = "explanation"
    elif lower_question.startswith(("when", "where")):
        query_type = "specific"
    elif lower_question.startswith(("can", "is", "are", "do", "does")):
        query_type = "yes_no"
    else:
        query_type = "general"

    stop_words = {
        "what", "which", "who", "how", "why", "when", "where",
        "can", "is", "are", "do", "does", "the", "a", "an",
        "for", "to", "of", "and", "in", "on", "with", "must"
    }

    words = question.lower().replace("?", "").split()

    keywords: List[str] = [
        word.strip(".,!?")
        for word in words
        if word.strip(".,!?") not in stop_words
        and len(word.strip(".,!?")) > 2
    ]

    return {
        "original_question": question,
        "query_type": query_type,
        "keywords": keywords,
        "needs_retrieval": True,
    }
