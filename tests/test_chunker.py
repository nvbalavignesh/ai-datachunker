import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from datachunker import DataChunker, ChunkConfig


def test_chunk_by_word():
    config = ChunkConfig(chunk_size=3, overlap=1, mode="word")
    chunker = DataChunker(config)
    text = "one two three four five six"
    assert chunker.chunk(text) == [
        "one two three",
        "three four five",
        "five six",
    ]


def test_chunk_by_char():
    config = ChunkConfig(chunk_size=4, overlap=2, mode="char")
    chunker = DataChunker(config)
    text = "abcdefg"
    assert chunker.chunk(text) == ["abcd", "cdef", "efg"]
