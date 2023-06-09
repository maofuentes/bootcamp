import http.server
import socketserver


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        message = "Bienvenidos a TeLoVendo"
        self.wfile.write(bytes(message, "utf8"))
        return


PORT = 8000

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("Sirviendo en el puerto", PORT)
    httpd.serve_forever()
