from http.server import HTTPServer, BaseHTTPRequestHandler
import json, os

DATA_FILE = "/app/data/submissions.json"

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/api/submit":
            length = int(self.headers["Content-Length"])
            post_data = self.rfile.read(length).decode("utf-8")
            try:
                new_data = json.loads(post_data)
            except:
                new_data = {"raw": post_data}

            os.makedirs("/app/data", exist_ok=True)
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f:
                    existing = json.load(f)
            else:
                existing = []

            existing.append(new_data)
            with open(DATA_FILE, "w") as f:
                json.dump(existing, f)

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Success")
        else:
            self.send_response(404)
            self.end_headers()

    def do_GET(self):
        if self.path == "/api/data":
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
            else:
                data = []
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()

server_address = ("", 8000)
httpd = HTTPServer(server_address, Handler)
print("Backend running on port 8000...")
httpd.serve_forever()
