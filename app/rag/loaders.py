from pathlib import Path
from typing import List, Tuple
from pypdf import PdfReader

def load_documents(folder: str) -> List[Tuple[str, str, int | None]]:
    records = []
    for path in sorted(Path(folder).glob("*")):
        suffix = path.suffix.lower()
        if suffix == ".pdf":
            reader = PdfReader(str(path))
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                if text.strip():
                    records.append((text, path.name, i + 1))
        elif suffix in {".txt", ".md"}:
            text = path.read_text(encoding="utf-8")
            if text.strip():
                records.append((text, path.name, None))
    return records
