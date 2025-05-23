import os
import subprocess
import sys
import time
import webview
import requests
from threading import Thread
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from backend.api import init_api

# Create Flask app
app = Flask(__name__, static_folder='frontend/out')
# Configure CORS to allow all origins in development
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000", "http://127.0.0.1:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Initialize API routes
init_api(app)

# Serve the Next.js static files
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    try:
        if path != "" and os.path.exists(app.static_folder + '/' + path):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.html')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def wait_for_flask():
    """Wait for Flask server to be ready"""
    max_retries = 30
    retry_interval = 1
    
    for i in range(max_retries):
        try:
            response = requests.get('http://127.0.0.1:5000/api/health')
            if response.status_code == 200:
                print("Flask server is ready!")
                return True
        except requests.exceptions.ConnectionError:
            print(f"Waiting for Flask server... ({i+1}/{max_retries})")
            time.sleep(retry_interval)
    
    print("Failed to connect to Flask server")
    return False

def run_flask():
    # Run Flask without debug mode in thread
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

def run_next_dev():
    os.chdir('frontend')
    if sys.platform == 'win32':
        subprocess.run('npm run dev', shell=True)
    else:
        subprocess.run(['npm', 'run', 'dev'])

class DesktopApp:
    def __init__(self):
        self.window = None
        self.last_reload = time.time()
        self.reload_interval = 1  # Check for changes every second

    def create_window(self):
        self.window = webview.create_window(
            'Desktop App (Development)',
            'http://localhost:3000',
            width=1200,
            height=800,
            resizable=True,
            min_size=(800, 600),
            text_select=True,
            confirm_close=True
        )

    def reload_window(self):
        if self.window:
            current_time = time.time()
            if current_time - self.last_reload >= self.reload_interval:
                self.window.evaluate_js('window.location.reload()')
                self.last_reload = current_time

def main():
    # Start Flask in a separate thread
    flask_thread = Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Wait for Flask to be ready
    if not wait_for_flask():
        print("Failed to start Flask server")
        sys.exit(1)

    # Start Next.js development server
    next_thread = Thread(target=run_next_dev)
    next_thread.daemon = True
    next_thread.start()

    # Wait for Next.js to start
    time.sleep(5)

    # Create and start the desktop app
    desktop_app = DesktopApp()
    desktop_app.create_window()

    # Start the webview event loop
    webview.start(debug=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nShutting down development servers...")
        sys.exit(0) 