from dataclasses import dataclass


@dataclass
class ChunkConfig:
    """Configuration for data chunking."""

    chunk_size: int = 100
    overlap: int = 0
    mode: str = "word"

    def __post_init__(self) -> None:
        if self.chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        if self.overlap < 0 or self.overlap >= self.chunk_size:
            raise ValueError("overlap must be non-negative and less than chunk_size")
        if self.mode not in {"word", "char"}:
            raise ValueError("mode must be 'word' or 'char'")
