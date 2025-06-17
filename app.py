from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

from datachunker import ChunkConfig, DataChunker

app = FastAPI(title="Generic Data Chunker")


class ChunkRequest(BaseModel):
    data: Union[str, List[str]]
    chunk_size: int = 100
    overlap: int = 0
    mode: str = "word"


@app.post("/chunk")
async def chunk_data(request: ChunkRequest):
    config = ChunkConfig(
        chunk_size=request.chunk_size,
        overlap=request.overlap,
        mode=request.mode,
    )
    chunker = DataChunker(config)
    chunks = chunker.chunk(request.data)
    return {"chunks": chunks}
