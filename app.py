from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def DO_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from ArgoCD!")

HTTPServer(("", 8080), Handler).serve_forever()
