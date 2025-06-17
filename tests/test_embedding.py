import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from datachunker.embedding import EmbeddingConfig, EmbeddingGenerator


def test_embedding_generator_requires_dependency():
    config = EmbeddingConfig()
    with pytest.raises(ImportError):
        EmbeddingGenerator(config)
