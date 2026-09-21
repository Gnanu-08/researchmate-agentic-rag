from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.loaders import load_documents
from app.rag.vectorstore import get_vectorstore
from app.config import CHROMA_PATH

DATA_DIR = "data/documents"

def build_index():
    records = load_documents(DATA_DIR)
    if not records:
        raise RuntimeError(f"No supported documents found in {DATA_DIR}")

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
    docs = []
    for text, source, page in records:
        for chunk in splitter.split_text(text):
            docs.append(Document(
                page_content=chunk,
                metadata={"source": source, "page": page}
            ))

    vs = get_vectorstore()
    # Avoid duplicate accumulation during repeated demos by rebuilding collection.
    try:
        vs.delete_collection()
    except Exception:
        pass
    vs = get_vectorstore()
    vs.add_documents(docs)
    print(f"Indexed {len(docs)} chunks into {CHROMA_PATH}")

if __name__ == "__main__":
    build_index()
