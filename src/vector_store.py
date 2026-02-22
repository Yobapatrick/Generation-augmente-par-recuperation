import faiss
import numpy as np


class VectorStore:

    def __init__(self, dimension: int):
        self.index = faiss.IndexFlatL2(dimension)

    def add(self, vectors: np.ndarray):
        self.index.add(vectors)

    def search(self, query_vector: np.ndarray, top_k: int = 5):
        distances, indices = self.index.search(query_vector, top_k)
        return indices[0]
    