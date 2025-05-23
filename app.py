import os
import webview
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from backend.api import init_api

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='frontend/out')
CORS(app)  # Enable CORS for all routes

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

def start_server():
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

if __name__ == '__main__':
    import threading
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    
    # Create the desktop window with text selection enabled
    webview.create_window(
        'Desktop App',
        'http://127.0.0.1:5000',
        width=1200,
        height=800,
        resizable=True,
        min_size=(800, 600),
        text_select=True,  # Enable text selection
        confirm_close=True  # Add confirmation dialog when closing
    )
    webview.start() 