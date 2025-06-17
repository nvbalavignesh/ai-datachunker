from dataclasses import dataclass
from typing import List, Union


@dataclass
class EmbeddingConfig:
    """Configuration for text embedding generation."""

    model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    batch_size: int = 32


class EmbeddingGenerator:
    """Generate embeddings for text using sentence-transformers."""

    def __init__(self, config: EmbeddingConfig) -> None:
        self.config = config
        try:
            from sentence_transformers import SentenceTransformer
        except ImportError as exc:  # pragma: no cover - optional dependency
            raise ImportError(
                "sentence-transformers is required for EmbeddingGenerator"
            ) from exc
        self._model = SentenceTransformer(self.config.model_name)

    def embed(self, texts: Union[str, List[str]]) -> List[List[float]]:
        """Return embeddings for a text or list of texts."""
        if isinstance(texts, str):
            texts = [texts]
        embeddings = self._model.encode(
            texts,
            batch_size=self.config.batch_size,
            convert_to_numpy=True,
        )
        return embeddings.tolist()
