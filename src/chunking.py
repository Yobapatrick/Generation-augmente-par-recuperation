from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


def chunk_documents(documents: List[str]) -> List[str]:
    all_chunks = []
    for doc in documents:
        all_chunks.extend(chunk_text(doc))
    return all_chunks