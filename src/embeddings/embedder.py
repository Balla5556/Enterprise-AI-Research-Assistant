"""Sentence-transformer embedding helpers."""

from sentence_transformers import SentenceTransformer


DEFAULT_MODEL_NAME = "all-MiniLM-L6-v2"


def load_embedding_model(model_name: str = DEFAULT_MODEL_NAME) -> SentenceTransformer:
    """Load and return the sentence-transformer embedding model."""
    return SentenceTransformer(model_name)


def embed_texts(texts: list[str], model_name: str = DEFAULT_MODEL_NAME) -> list[list[float]]:
    """Generate embeddings for a list of texts."""
    model = load_embedding_model(model_name=model_name)
    vectors = model.encode(texts, convert_to_numpy=True)
    return vectors.tolist()
