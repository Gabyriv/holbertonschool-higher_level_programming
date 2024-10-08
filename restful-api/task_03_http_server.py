#!/usr/bin/python3
"""Develop a simple API using Python
    with the http.server module"""

import http.server
import socketserver
import json


class Server(http.server.BaseHTTPRequestHandler):
    """Handles Get requests and serves responses
    based on the requested path.
    """

    def do_GET(self):
        """This function handles the endpoints
        """
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

            self.wfile.write(json.dumps(data).encode())

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }

            self.wfile.write(json.dumps(info).encode())

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
