import http.server
import socketserver

PORT = 8080
DIRECTORY = "."

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run(server_class=http.server.HTTPServer, handler_class=CustomHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    print(f"Serving HTTP on port {PORT}...")
    try:
        httpd.serve_forever()
    except PermissionError as e:
        print(f"PermissionError: {e}. Try running the script as an administrator or using a different port.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run()

