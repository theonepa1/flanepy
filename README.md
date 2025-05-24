# Flanepy - Modern Desktop Application Template

A powerful template for building modern desktop applications using Python, PyWebView (desktop wrapper), and Next.js (frontend). This template provides a solid foundation for creating cross-platform desktop applications with a beautiful web-based UI and robust Python backend logic.

## Key Features

- 🖥️ **Desktop Application**: Native desktop experience using PyWebView
- 🔄 **Hot Reloading**: Automatic reloading of the frontend during development
- 🎨 **Modern UI**: Next.js frontend with all modern web capabilities
- 🐍 **Python Backend**: Python-powered backend logic, exposed to the frontend via a bridge (no Flask server required)
- 🔌 **API Integration**: Built-in API bridge for frontend-backend communication
- 📦 **Easy Distribution**: Simple process to create standalone applications
- 🔧 **Development Tools**: Comprehensive development environment setup

## Use Cases

This template is perfect for:
- Desktop applications requiring a modern web-based UI
- Cross-platform applications with Python backend logic
- Applications needing both local and web capabilities
- Projects requiring rapid development with hot reloading
- Applications that need to be distributed as standalone executables

## Setup

### Backend Setup
1. Create a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Frontend Setup
1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install Node.js dependencies:
```bash
npm install
```

3. Build the Next.js application (for production/distribution):
```bash
npm run build
```

## Running the Application

### Development Mode
1. Start the development environment:
```bash
python app.py --dev
```
- This will start the Next.js dev server (npm process) in the background.
- The desktop window will open and connect to the dev server at http://localhost:3000.
- When you close the app, the npm process is automatically terminated.

### Production Mode
1. Build the frontend (if not already built):
```bash
cd frontend
npm run build
cd ..
```
2. Start the application:
```bash
python app.py
```
- This will start a lightweight Python HTTP server to serve static files from `frontend/out`.
- The desktop window will open and connect to http://127.0.0.1:42791.

## Architecture
- **No Flask server is used.**
- All backend logic is exposed to the frontend via a Python API bridge (see `backend/bridge.py`).
- In production, static files are served using Python's built-in `http.server`.
- In development, the Next.js dev server is used for hot reloading and fast feedback.
- The app window is managed by PyWebView, and all JS ↔ Python communication goes through the bridge.
- The npm process is automatically cleaned up when the app is closed in dev mode (even if the window is closed).

## Distribution

### Creating a Standalone Application

1. Build the frontend:
```bash
cd frontend
npm run build
cd ..
```

2. Create the standalone application using PyInstaller:
```bash
# On Windows:
pyinstaller --noconfirm --windowed --add-data "frontend/out;frontend/out" --name "Flanepy" app.py

# On macOS/Linux:
pyinstaller --noconfirm --windowed --add-data "frontend/out:frontend/out" --name "Flanepy" app.py
```

3. Create a DMG installer (macOS only):
```bash
dmgbuild -s dmg_settings.py "Flanepy" "dist/Flanepy.dmg"
```

The final distribution files will be:
- Windows: `dist/Flanepy/Flanepy.exe` - The standalone application
- macOS: `dist/Flanepy.app` - The standalone application
- macOS: `dist/Flanepy.dmg` - The macOS installer

### Distribution Files
- On Windows: Copy the entire `dist/Flanepy` folder and run `Flanepy.exe`
- On macOS: The `.app` bundle can be distributed directly to macOS users
- On macOS: The `.dmg` file provides a proper installer with drag-and-drop installation

## Development

- Backend logic is exposed via the Python API bridge (no HTTP API server)
- Frontend development server runs on: http://localhost:3000
- Hot reloading is enabled by default in development mode
- Changes to frontend code will automatically trigger reloads
- Closing the app in dev mode will also terminate the npm process

## Contributing

Feel free to use this template as a starting point for your desktop applications. Contributions and improvements are welcome!

## License

MIT License - Feel free to use this template for your projects. 