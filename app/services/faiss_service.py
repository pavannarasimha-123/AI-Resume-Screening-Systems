import faiss
import numpy as np


class FAISSService:

    def __init__(self, dimension=384):

        self.dimension = dimension

        self.index = faiss.IndexFlatL2(dimension)

    def clear(self):
        """
        Reset the FAISS index.
        """
        self.index = faiss.IndexFlatL2(self.dimension)

    def add_embedding(self, embedding):

        embedding = np.array(
            embedding,
            dtype=np.float32
        ).reshape(1, -1)

        self.index.add(embedding)

    def search(
        self,
        embedding,
        top_k=10
    ):

        if self.index.ntotal == 0:
            return [], []

        embedding = np.array(
            embedding,
            dtype=np.float32
        ).reshape(1, -1)

        distances, indices = self.index.search(
            embedding,
            min(top_k, self.index.ntotal)
        )

        return distances[0], indices[0]