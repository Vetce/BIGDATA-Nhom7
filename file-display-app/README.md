# BIGDATA File Display App

A modern React + Material-UI application to browse and manage files from multiple BIGDATA directories.

## Features

✨ **Core Features:**
- 📁 Browse files from 3 main directories:
  - `quick-result/` - Quick analysis results
  - `Optimize-Delivery/optimize/result/` - Delivery optimization outputs
  - `Inventory-Management/result/` - Inventory analysis results
- 📊 View file details (name, size, type, modification time)
- 👁️ Preview CSV, JSON, and image files
- ⬇️ Download files directly from the UI
- 📑 Tabbed interface for easy navigation
- 🎨 Beautiful Material-UI design
- 📱 Responsive layout

## Installation

### Prerequisites
- Node.js 14+ 
- npm 6+

### Setup

1. **Navigate to the project:**
```bash
cd /home/sirin/BIGDATA/file-display-app
```

2. **Install dependencies:**

Frontend:
```bash
npm install
```

Backend:
```bash
cd server
npm install
cd ..
```

## Usage

### Development Mode

Run both frontend and backend concurrently:

```bash
npm run dev
```

Or run them separately:

**Terminal 1 - Backend:**
```bash
cd server
npm start
```

**Terminal 2 - Frontend:**
```bash
npm start
```

The application will open at `http://localhost:3000`

### Production Build

```bash
npm run build
```

## Project Structure

```
file-display-app/
├── public/
│   └── index.html
├── src/
│   ├── components/
│   │   ├── FileExplorer.js      # Main file table component
│   │   ├── FilePreview.js       # File preview dialog
│   │   └── FileDetails.js       # File details dialog
│   ├── App.js                   # Main app component
│   ├── App.css                  # App styles
│   └── index.js                 # React entry point
├── server/
│   ├── index.js                 # Express server
│   └── package.json
├── package.json
├── .env                         # Environment variables
└── README.md
```

## API Endpoints

### GET /api/files
Returns all files from configured directories
```json
{
  "quick-result": [...],
  "Optimize-Delivery Results": [...],
  "Inventory-Management Results": [...]
}
```

### GET /api/preview
Preview file contents (CSV, JSON, images)
- Query params: `path` - full file path

### GET /api/download
Download a file
- Query params: `path` - full file path

### GET /api/health
Health check endpoint

## File Types Supported

| Type | Preview | Download |
|------|---------|----------|
| CSV  | ✅      | ✅       |
| JSON | ✅      | ✅       |
| PNG  | ✅      | ✅       |
| JPG  | ✅      | ✅       |
| H5   | ❌      | ✅       |
| PKL  | ❌      | ✅       |
| Other| ❌      | ✅       |

## Customization

### Add More Directories

Edit `server/index.js` and update the `DIRECTORIES` array:

```javascript
const DIRECTORIES = [
  {
    name: 'Your Directory Name',
    path: '/path/to/directory',
  },
  // ... more directories
];
```

### Customize Theme

Edit `src/index.js` to modify the Material-UI theme:

```javascript
const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2', // Change primary color
    },
    secondary: {
      main: '#dc004e', // Change secondary color
    },
  },
});
```

## Troubleshooting

**Port already in use:**
```bash
# Backend (port 5000):
PORT=5001 npm run dev

# Frontend (port 3000):
PORT=3001 npm start
```

**Permission denied errors:**
Ensure the application has read access to the directories:
```bash
chmod +r /home/sirin/BIGDATA/quick-result
chmod +r /home/sirin/BIGDATA/Optimize-Delivery/optimize/result
chmod +r /home/sirin/BIGDATA/Inventory-Management/result
```

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

## License

MIT
