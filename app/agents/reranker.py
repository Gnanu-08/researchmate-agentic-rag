from typing import List, Tuple

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

from app.config import EMBEDDING_MODEL


_model = None


def get_reranker_model():
    global _model

    if _model is None:
        _model = SentenceTransformer(EMBEDDING_MODEL)

    return _model


def rerank_documents(query: str, documents: list, top_k: int = 5) -> list:
    """
    Rerank retrieved documents using semantic similarity.

    The same local embedding model used by the RAG system
    is used to compare the query with each document.
    """

    if not documents:
        return []

    model = get_reranker_model()

    query_embedding = model.encode(
        query,
        convert_to_tensor=True
    )

    document_texts = [
        document.page_content
        for document in documents
    ]

    document_embeddings = model.encode(
        document_texts,
        convert_to_tensor=True
    )

    scores = cos_sim(
        query_embedding,
        document_embeddings
    )[0]

    ranked: List[Tuple[float, object]] = [
        (float(score), document)
        for score, document in zip(scores, documents)
    ]

    ranked.sort(
        key=lambda item: item[0],
        reverse=True
    )

    return [
        document
        for _, document in ranked[:top_k]
    ]
