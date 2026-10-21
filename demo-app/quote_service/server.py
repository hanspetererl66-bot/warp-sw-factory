import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

from .auth import role_from_headers
from .pricing import Quote, apply_discount

QUOTES = {"Q-1001": Quote("Q-1001", 1_000_000)}


class Handler(BaseHTTPRequestHandler):
    def _send(self, status, body):
        data = json.dumps(body).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path == "/health":
            return self._send(200, {"status": "ok", "version": os.environ.get("APP_VERSION", "dev")})
        quote_id = self.path.rsplit("/", 1)[-1]
        quote = QUOTES.get(quote_id)
        if quote is None:
            return self._send(404, {"error": "not found"})
        self._send(200, {"id": quote.quote_id, "net_price_cents": quote.net_price_cents,
                         "discount_pct": quote.discount_pct})

    def do_POST(self):
        try:
            role_from_headers(self.headers)
        except PermissionError:
            return self._send(403, {"error": "forbidden"})
        quote_id = self.path.rsplit("/", 1)[-1]
        quote = QUOTES.get(quote_id)
        if quote is None:
            return self._send(404, {"error": "not found"})
        length = int(self.headers.get("Content-Length", 0))
        try:
            pct = int(json.loads(self.rfile.read(length) or b"{}")["discount_pct"])
            QUOTES[quote_id] = apply_discount(quote, pct)
        except (KeyError, ValueError, TypeError):
            return self._send(400, {"error": "invalid discount"})
        self._send(200, {"id": quote_id, "discount_pct": pct})


def main():
    HTTPServer(("0.0.0.0", int(os.environ.get("PORT", "8080"))), Handler).serve_forever()


if __name__ == "__main__":
    main()
