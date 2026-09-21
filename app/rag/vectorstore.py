from pathlib import Path
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from app.config import EMBEDDING_MODEL, CHROMA_PATH, COLLECTION_NAME

def get_embeddings():
    return HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def get_vectorstore():
    Path(CHROMA_PATH).mkdir(parents=True, exist_ok=True)
    return Chroma(
        collection_name=COLLECTION_NAME,
        persist_directory=CHROMA_PATH,
        embedding_function=get_embeddings(),
    )
