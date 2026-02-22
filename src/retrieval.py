from typing import List
from src.embeddings import EmbeddingModel
from src.vector_store import VectorStore


class Retriever:

    def __init__(self, documents: List[str]):
        self.documents = documents
        self.embedder = EmbeddingModel()

        self.doc_vectors = self.embedder.encode_documents(documents)
        self.vector_store = VectorStore(self.doc_vectors.shape[1])
        self.vector_store.add(self.doc_vectors)

    def retrieve(self, query: str, top_k: int = 5) -> List[str]:
        query_vector = self.embedder.encode_query(query)
        indices = self.vector_store.search(query_vector, top_k)
        return [self.documents[i] for i in indices]