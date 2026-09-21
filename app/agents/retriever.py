from app.rag.retrieval import retrieve

def retrieve_evidence(query: str):
    return retrieve(query)
