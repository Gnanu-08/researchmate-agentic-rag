from app.rag.vectorstore import get_vectorstore
from app.config import TOP_K
from app.agents.reranker import rerank_documents


def retrieve(query: str, k: int = TOP_K):
    vs = get_vectorstore()

    # Retrieve extra candidates so the reranker has more evidence to compare.
    candidate_k = max(k * 2, 8)

    documents = vs.similarity_search(
        query,
        k=candidate_k
    )

    # Rerank candidates and return the best k documents.
    return rerank_documents(
        query,
        documents,
        top_k=k
    )
