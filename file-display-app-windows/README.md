# BIGDATA File Display App - Windows Setup Guide

## Prerequisites

Before running this application, you need to have **Node.js** installed on your Windows machine.

### Install Node.js

1. Download Node.js (version 14 or higher) from: https://nodejs.org
2. Run the installer and follow the installation wizard
3. Verify installation by opening Command Prompt and typing:
   ```
   node -v
   npm -v
   ```

## Installation

### Step 1: Run Setup

Double-click `setup.bat` or run from Command Prompt:
```batch
setup.bat
```

This will:
- Check if Node.js is installed
- Install all frontend dependencies
- Install all backend dependencies

## Running the Application

### Option 1: Automatic Start (Recommended)

Double-click `start.bat` or run:
```batch
start.bat
```

This will automatically start both the backend server and frontend application.

### Option 2: Manual Start

If you prefer to run them separately:

1. **Start Backend** (in one Command Prompt window):
   ```batch
   start-backend.bat
   ```

2. **Start Frontend** (in another Command Prompt window):
   ```batch
   start-frontend.bat
   ```

## Accessing the Application

- **Frontend (Web Interface)**: http://localhost:3000
- **Backend (API Server)**: http://localhost:5000

## Troubleshooting

### "Node.js is not installed" error
- Install Node.js from https://nodejs.org
- Restart your Command Prompt after installation

### "Could not find directory" error
- Make sure the `file-display-app` folder exists in the parent directory
- Update the `APP_DIR` path in the batch files if your folder structure is different

### Port already in use
- If port 3000 or 5000 is already in use, you'll need to:
  1. Close the application using that port
  2. Or modify the port in the configuration files

### Dependencies installation failed
- Try running Command Prompt as Administrator
- Delete `node_modules` folders and run `setup.bat` again
- Check your internet connection

## Application Structure

```
file-display-app/
├── src/                    # React frontend source
├── public/                 # Static files
├── server/                 # Express backend
│   └── index.js           # Server entry point
├── package.json           # Frontend dependencies
└── server/package.json    # Backend dependencies
```

## Features

- Browse files from multiple data directories
- Preview CSV and JSON files
- Download files directly from the interface
- View file metadata
- Material-UI responsive design

## Support

For issues or questions, please refer to the main project documentation.
