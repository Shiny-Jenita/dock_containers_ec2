from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

DATA_FILE = "/app/data/submissions.json"

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/api/submit":
            length = int(self.headers.get("Content-Length", 0))
            post_data = self.rfile.read(length).decode("utf-8")
            try:
                new_data = json.loads(post_data)
            except:
                new_data = {"raw": post_data}

            # Ensure data folder exists
            os.makedirs("/app/data", exist_ok=True)

            # Read existing submissions
            if os.path.exists(DATA_FILE):
                with open(DATA_FILE, "r") as f:
                    existing = json.load(f)
            else:
                existing = []

            # Append new submission
            existing.append(new_data)

            # Save back to file
            with open(DATA_FILE, "w") as f:
                json.dump(existing, f, indent=2)

            # Send response
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode())
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

if __name__ == "__main__":
    server_address = ("", 5000)  # Listen on all interfaces
    httpd = HTTPServer(server_address, Handler)
    print("Backend running on port 5000...")
    httpd.serve_forever()
