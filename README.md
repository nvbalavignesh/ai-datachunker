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

