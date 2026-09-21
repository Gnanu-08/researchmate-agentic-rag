import subprocess
import sys

if __name__ == "__main__":
    subprocess.run([sys.executable, "-m", "app.rag.ingest"], check=True)
    print("Knowledge base indexed. Start UI with: streamlit run frontend/streamlit_app.py")
