from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlsplit


PAGE = Path(__file__).with_name("index.html")


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path not in ("/", "/index.html"):
            self.send_error(404)
            return

        try:
            page = PAGE.read_bytes()
        except OSError:
            self.send_error(500, "Could not read index.html")
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)


if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    print("Open http://127.0.0.1:8000 in your browser")
    HTTPServer(address, AppHandler).serve_forever()
