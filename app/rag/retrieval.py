from app.rag.vectorstore import get_vectorstore
from app.config import TOP_K

def retrieve(query: str, k: int = TOP_K):
    vs = get_vectorstore()
    return vs.similarity_search(query, k=k)
