# AI Data Chunker

This repository provides a small utility to split arbitrary data into chunks. It
exposes a reusable library and a lightweight API server implemented with the
standard library.

## Library Usage

```python
from datachunker import DataChunker, ChunkConfig

config = ChunkConfig(chunk_size=100, overlap=10, mode="word")
chunker = DataChunker(config)

chunks = chunker.chunk("some long text ...")
```

## API Usage

Run the HTTP server:

```bash
python server.py
```

Then send a POST request to `/chunk` with the data and configuration:

```bash
curl -X POST http://localhost:8000/chunk \
  -H "Content-Type: application/json" \
  -d '{"data": "your text", "chunk_size": 100, "overlap": 10, "mode": "word"}'
```

## Development

Install dependencies and run tests with `pytest`.

## Embedding Utility

`EmbeddingGenerator` wraps the [`sentence-transformers`](https://www.sbert.net/) library to
produce vector embeddings suitable for retrieval-augmented generation (RAG)
workflows:

```python
from datachunker import EmbeddingConfig, EmbeddingGenerator

config = EmbeddingConfig(model_name="sentence-transformers/all-MiniLM-L6-v2")
embedder = EmbeddingGenerator(config)
vectors = embedder.embed(["my text"])  # returns a list of embedding vectors
```

The optional dependency `sentence-transformers` must be installed to use this
class.

