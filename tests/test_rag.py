from app.rag.loaders import load_documents

def test_sample_documents_exist():
    records = load_documents("data/documents")
    assert len(records) >= 3
