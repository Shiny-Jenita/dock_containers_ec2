from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
import json
import os

DATA_FILE = "submissions.json"

# Ensure JSON file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("form.html", "rb") as f:
                self.wfile.write(f.read())
        elif self.path == "/submissions.json":
             self.send_response(200)
             self.send_header("Content-type", "application/json")
             self.end_headers()
             with open(DATA_FILE, "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()
   
    
    def do_POST(self):
        if self.path == "/submit":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = urllib.parse.parse_qs(post_data.decode())

            submission = {
                "name": data.get("name", [""])[0],
                "email": data.get("email", [""])[0],
                "message": data.get("message", [""])[0]
            }

            # Load existing data
            with open(DATA_FILE, "r") as f:
                submissions = json.load(f)

            # Append new submission
            submissions.append(submission)

            # Save back
            with open(DATA_FILE, "w") as f:
                json.dump(submissions, f, indent=4)

            # Response
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h2>Thank you for your submission!</h2>")

        else:
            self.send_response(404)
            self.end_headers()

# Run server
PORT = 8000
with HTTPServer(("", PORT), SimpleHandler) as httpd:
    print(f"Serving on port {PORT}...")
    httpd.serve_forever()
