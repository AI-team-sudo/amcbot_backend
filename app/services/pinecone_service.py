import pinecone
from app.core.config import settings

class PineconeService:
    def __init__(self):
        """
        Initialize the Pinecone client and set the index name.
        """
        try:
            # Initialize Pinecone client with API key and environment
            pinecone.init(api_key=settings.PINECONE_API_KEY, environment=settings.PINECONE_ENVIRONMENT)
            self.index_name = settings.PINECONE_INDEX_NAME

            # Check if the index exists, otherwise raise an error
            if self.index_name not in pinecone.list_indexes():
                raise ValueError(f"Pinecone index '{self.index_name}' does not exist. Please create it first.")
        except Exception as e:
            raise RuntimeError(f"Failed to initialize Pinecone client: {e}")

    def upsert_vectors(self, vectors: list):
        """
        Upsert vectors into the Pinecone index.

        Args:
            vectors (list): A list of dictionaries containing vector data.
                            Example: [{"id": "1", "values": [0.1, 0.2, 0.3], "metadata": {"key": "value"}}]
        """
        try:
            # Connect to the Pinecone index
            index = pinecone.Index(self.index_name)
            # Upsert the vectors
            index.upsert(vectors)
        except Exception as e:
            raise RuntimeError(f"Pinecone upsert error: {e}")

    def query_vectors(self, vector: list, top_k: int = 10):
        """
        Query the Pinecone index with a vector.

        Args:
            vector (list): The query vector to search for.
            top_k (int): The number of top results to return.

        Returns:
            dict: The query results from Pinecone.
        """
        try:
            # Connect to the Pinecone index
            index = pinecone.Index(self.index_name)
            # Query the index
            results = index.query(vector=vector, top_k=top_k, include_metadata=True)
            return results
        except Exception as e:
            raise RuntimeError(f"Pinecone query error: {e}")
