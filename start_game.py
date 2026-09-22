import http.server, socketserver, webbrowser, threading, os
PORT=8765
class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control','no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma','no-cache')
        self.send_header('Expires','0')
        super().end_headers()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
with socketserver.ThreadingTCPServer(('127.0.0.1',PORT),Handler) as httpd:
    print(f'YWP Offline — http://127.0.0.1:{PORT}/index.html')
    threading.Timer(0.5, lambda:webbrowser.open(f'http://127.0.0.1:{PORT}/index.html')).start()
    httpd.serve_forever()
