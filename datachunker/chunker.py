from typing import List, Sequence, Union

from .config import ChunkConfig


class DataChunker:
    """Generic utility to split data into chunks."""

    def __init__(self, config: ChunkConfig) -> None:
        self.config = config

    def chunk(self, data: Union[str, Sequence[str]]) -> List[str]:
        """Chunk the input data according to the configuration."""
        if isinstance(data, str):
            text = data
        else:
            text = " ".join(str(d) for d in data)

        if self.config.mode == "word":
            tokens = text.split()
            joiner = " ".join
        else:
            tokens = list(text)
            joiner = "".join

        chunk_size = self.config.chunk_size
        step = chunk_size - self.config.overlap
        chunks: List[str] = []
        i = 0
        while i < len(tokens):
            chunk = joiner(tokens[i : i + chunk_size])
            chunks.append(chunk)
            if i + chunk_size >= len(tokens):
                break
            i += step
        return chunks
