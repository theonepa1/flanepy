# Flanepy - Modern Desktop Application Template

A powerful template for building modern desktop applications using Flask (backend), PyWebView (desktop wrapper), and Next.js (frontend). This template provides a solid foundation for creating cross-platform desktop applications with a beautiful web-based UI and robust Python backend.

## Key Features

- 🖥️ **Desktop Application**: Native desktop experience using PyWebView
- 🔄 **Hot Reloading**: Automatic reloading of both frontend and backend during development
- 🎨 **Modern UI**: Next.js frontend with all modern web capabilities
- 🐍 **Python Backend**: Flask-powered backend for robust server-side operations
- 🔌 **API Integration**: Built-in API endpoints for frontend-backend communication
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
- Hot reloading is enabled by default in development mode
- Changes to both frontend and backend code will automatically trigger reloads

## Contributing

Feel free to use this template as a starting point for your desktop applications. Contributions and improvements are welcome!

## License

MIT License - Feel free to use this template for your projects. 