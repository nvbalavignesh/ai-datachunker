import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from datachunker import ChunkConfig, DataChunker


class ChunkHandler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        if self.path != "/chunk":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length)
        try:
            payload = json.loads(body)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")
            return

        config = ChunkConfig(
            chunk_size=payload.get("chunk_size", 100),
            overlap=payload.get("overlap", 0),
            mode=payload.get("mode", "word"),
        )
        chunker = DataChunker(config)
        chunks = chunker.chunk(payload.get("data", ""))

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"chunks": chunks}).encode())


def run(host: str = "0.0.0.0", port: int = 8000) -> None:
    server = HTTPServer((host, port), ChunkHandler)
    print(f"Serving on {host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run()
