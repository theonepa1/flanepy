import os
import sys
import time
import threading
import subprocess
import argparse
import webview
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
from backend.bridge import ApiBridge
from backend.api import health_check, hello, echo

FRONTEND_OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), 'frontend', 'out'))
PROD_PORT = 42791
DEV_PORT = 3000

npm_process = None  # Global handle for the dev server process

class StaticHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=FRONTEND_OUT, **kwargs)

    def end_headers(self):
        # Allow CORS if needed
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def start_http_server():
    with TCPServer(('127.0.0.1', PROD_PORT), StaticHandler) as httpd:
        print(f"Serving at http://127.0.0.1:{PROD_PORT}")
        httpd.serve_forever()

def run_next_dev():
    global npm_process
    os.chdir('frontend')
    if sys.platform == 'win32':
        npm_process = subprocess.Popen('npm run dev', shell=True)
    else:
        npm_process = subprocess.Popen(['npm', 'run', 'dev'])

def cleanup():
    global npm_process
    if 'npm_process' in globals() and npm_process is not None:
        npm_process.terminate()
        npm_process.wait()
        npm_process = None

class DesktopApp:
    """
    Wrapper around a pywebview Window plus a lightweight bridge that
    exposes backend functions to the JS front-end (pywebview ≥ 4.x).
    """
    def __init__(self, is_dev: bool = False) -> None:
        self.window: webview.Window | None = None
        self.is_dev = is_dev
        self.api = ApiBridge()
        self.api.register_api('health_check', health_check)
        self.api.register_api('hello', hello)
        self.api.register_api('echo', echo)

    def create_window(self) -> None:
        """
        Create the WebView window and expose Python functions to JS.
        """
        if self.is_dev:
            url = f'http://localhost:{DEV_PORT}'
            title = 'Desktop App (Development)'
        else:
            url = f'http://127.0.0.1:{PROD_PORT}'
            title = 'Desktop App'
        self.window = webview.create_window(
            title=title,
            url=url,
            width=1200,
            height=800,
            resizable=True,
            min_size=(800, 600),
            text_select=True,
            confirm_close=True,
        )
        self.api.expose_all(self.window)
        if self.is_dev:
            self.window.events.closed += cleanup

def main():
    parser = argparse.ArgumentParser(description='Desktop App')
    parser.add_argument('--dev', action='store_true', help='Run in development mode')
    args = parser.parse_args()

    if args.dev:
        # Start Next.js dev server
        next_thread = threading.Thread(target=run_next_dev, daemon=True)
        next_thread.start()
        print("Waiting for Next.js dev server to start...")
        time.sleep(5)  # crude, but works for most setups
    else:
        # Start static HTTP server for production
        server_thread = threading.Thread(target=start_http_server, daemon=True)
        server_thread.start()

    app = DesktopApp(is_dev=args.dev)
    app.create_window()
    webview.start(debug=args.dev)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nShutting down...')
        cleanup()
        sys.exit(0) 