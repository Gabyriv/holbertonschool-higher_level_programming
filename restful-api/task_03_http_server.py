#!/usr/bin/python3
"""Develop a simple API using Python
    with the http.server module"""

import http.server
import socketserver
import json


class Server(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {
                "error": "Endpoint Not Found"
            }
        self.wfile.write(json.dumps(error_message).encode())


PORT = 8000

with socketserver.TCPServer(("", PORT), Server) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()