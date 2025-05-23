# Flanepy - Desktop Application

A modern desktop application built with Flask (backend), PyWebView (desktop wrapper), and Next.js (frontend).

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

3. Build the Next.js application:
```bash
npm run build
```

## Running the Application

### Development Mode
1. Start the development environment:
```bash
python dev.py
```

The application will automatically open in a desktop window using PyWebView.

### Production Mode
1. Start the Flask backend:
```bash
python app.py
```

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
pyinstaller --noconfirm --windowed --add-data "frontend/out:frontend/out" --name "Flanepy" app.py
```

3. Create a DMG installer:
```bash
dmgbuild -s dmg_settings.py "Flanepy" "dist/Flanepy.dmg"
```

The final distribution files will be:
- `dist/Flanepy.app` - The standalone application
- `dist/Flanepy.dmg` - The macOS installer

### Distribution Files
- The `.app` bundle can be distributed directly to macOS users
- The `.dmg` file provides a proper installer with drag-and-drop installation

## Development

- Backend runs on: http://localhost:5000
- Frontend development server runs on: http://localhost:3000 