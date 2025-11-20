# 🛠️ Development Guide

## Overview

This guide covers how to develop, extend, and customize the BIGDATA File Display App.

---

## 📋 Project Files

### React Components

#### `src/App.js`
Main application component. Handles:
- Fetching files from backend
- Managing tab navigation
- Error handling and loading states

**Key Functions:**
- `fetchFiles()` - Retrieves file list from API
- `handleTabChange()` - Switches between directory tabs

#### `src/components/FileExplorer.js`
File table display component. Shows:
- File name, type, size, modification date
- Action buttons (preview, details, download)

**Key Functions:**
- `handlePreview()` - Opens preview modal
- `handleDetails()` - Opens details modal
- `handleDownload()` - Initiates file download
- `getFileType()` - Determines file category
- `formatFileSize()` - Human-readable file sizes

#### `src/components/FilePreview.js`
File preview modal. Supports:
- CSV table display (first 20 rows)
- JSON data viewing
- Image display with base64 encoding

**Key Functions:**
- `fetchPreview()` - Gets preview data from backend
- `renderPreview()` - Renders appropriate preview type

#### `src/components/FileDetails.js`
File details modal. Shows:
- Complete file metadata
- Download button

---

### Backend Files

#### `server/index.js`
Express API server. Provides:
- File listing endpoint
- File preview endpoint
- Download endpoint
- Health check endpoint

**Key Endpoints:**
- `GET /api/files` - List all files
- `GET /api/preview` - Preview file
- `GET /api/download` - Download file
- `GET /api/health` - Health check

**Key Functions:**
- `getFileInfo()` - Extract file metadata
- File security validation
- CSV/JSON parsing
- Image base64 encoding

---

## 🔧 How to Extend

### Add New File Type Preview

**Example: Add PDF Preview**

1. Update backend (`server/index.js`):
```javascript
else if (extension === 'pdf') {
  // Handle PDF preview
  const pdfData = convertPdfToImages(filePath);
  res.json({
    type: 'pdf',
    data: pdfData
  });
}
```

2. Update frontend (`src/components/FilePreview.js`):
```javascript
if (preview.type === 'pdf') {
  return <PdfViewer data={preview.data} />;
}
```

3. Update FileExplorer column:
```javascript
{(file.extension === 'pdf') && (
  <Tooltip title="Preview">
    <IconButton
      size="small"
      onClick={() => handlePreview(file)}
      color="primary"
    >
      <VisibilityIcon fontSize="small" />
    </IconButton>
  </Tooltip>
)}
```

### Add New Directory

1. Edit `server/index.js`:
```javascript
const DIRECTORIES = [
  {
    name: 'quick-result',
    path: '/home/sirin/BIGDATA/quick-result',
  },
  {
    name: 'My New Directory',
    path: '/path/to/new/directory',
  },
];
```

2. Backend automatically picks it up on restart

### Add Search Functionality

Add to `src/App.js`:
```javascript
const [searchTerm, setSearchTerm] = useState('');

const filteredFiles = files[activeDir]?.filter(file =>
  file.name.toLowerCase().includes(searchTerm.toLowerCase())
);
```

Add to UI:
```javascript
<TextField
  placeholder="Search files..."
  value={searchTerm}
  onChange={(e) => setSearchTerm(e.target.value)}
  size="small"
  sx={{ mb: 2 }}
/>
```

### Custom Styling

Material-UI uses `sx` prop for styling:

```javascript
<Box sx={{
  backgroundColor: '#f5f5f5',
  padding: '16px',
  borderRadius: '8px',
}}>
  Content
</Box>
```

For global styles, edit `src/App.css`.

---

## 🚀 Development Workflow

### 1. Setup Development Environment

```bash
cd /home/sirin/BIGDATA/file-display-app
npm install
cd server && npm install && cd ..
```

### 2. Start in Development Mode

```bash
# Terminal 1: Backend
cd server
npm start

# Terminal 2: Frontend
npm start
```

### 3. Make Changes

Frontend changes hot-reload automatically.
For backend changes, manually restart.

### 4. Testing Changes

- Open http://localhost:3000
- Check Console (F12) for errors
- Use browser DevTools for debugging

---

## 🐛 Debugging

### React DevTools
Install Chrome extension:
https://chrome.google.com/webstore/detail/react-developer-tools

### Network Debugging
1. Open Chrome DevTools (F12)
2. Go to Network tab
3. Watch API calls
4. Check responses

### Backend Logging
Add console.log in `server/index.js`:
```javascript
app.get('/api/files', (req, res) => {
  console.log('Fetching files...'); // Add this
  // ... rest of code
});
```

---

## 📦 Adding Dependencies

### Frontend
```bash
cd /home/sirin/BIGDATA/file-display-app
npm install package-name
```

Then import and use:
```javascript
import { MyComponent } from 'package-name';
```

### Backend
```bash
cd /home/sirin/BIGDATA/file-display-app/server
npm install package-name
```

Then require and use:
```javascript
const myModule = require('package-name');
```

---

## 🎨 Customizing Theme

Edit `src/index.js`:

```javascript
const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
      light: '#42a5f5',
      dark: '#1565c0',
    },
    secondary: {
      main: '#dc004e',
    },
    background: {
      default: '#fafafa',
      paper: '#fff',
    },
  },
  typography: {
    fontFamily: 'Roboto, sans-serif',
    fontSize: 14,
  },
});
```

---

## 📊 Data Flow

```
User Action
    ↓
React Component
    ↓
API Call (axios/fetch)
    ↓
Express Server (server/index.js)
    ↓
File System
    ↓
Parse/Process Data
    ↓
JSON Response
    ↓
Update React State
    ↓
Re-render UI
```

---

## 🔄 State Management

Currently using React Hooks (`useState`):

```javascript
const [files, setFiles] = useState({});
const [loading, setLoading] = useState(false);
const [error, setError] = useState(null);
```

For larger app, consider:
- Redux
- Context API
- Zustand

---

## 🚢 Deployment

### To Production

1. Build frontend:
```bash
npm run build
```

2. Serve build:
```bash
npm install -g serve
serve -s build
```

3. Or use Docker:
```bash
docker-compose up --build
```

---

## 📈 Performance Tips

- Limit CSV preview to first 20 rows
- Use React.memo for expensive components
- Lazy load components as needed
- Compress images
- Enable gzip compression

---

## 🔐 Security Considerations

- ✅ Validate all file paths
- ✅ Whitelist directories only
- ✅ Check file permissions
- ✅ Limit file sizes
- ✅ Escape user input
- ✅ Use HTTPS in production

---

## 📝 Code Style

- Use ESLint for JavaScript linting
- Use Prettier for code formatting
- Follow React best practices
- Comment complex logic
- Use meaningful variable names

---

## 🧪 Testing (Future)

Add Jest + React Testing Library:

```bash
npm install --save-dev @testing-library/react jest
```

Create test files:
```javascript
// src/App.test.js
import { render } from '@testing-library/react';
import App from './App';

test('renders without crashing', () => {
  render(<App />);
});
```

---

## 📚 Useful Resources

- React: https://react.dev
- Material-UI: https://mui.com
- Express: https://expressjs.com
- MDN Web Docs: https://developer.mozilla.org
- Stack Overflow: https://stackoverflow.com

---

## 💡 Common Tasks

### Change Port
```bash
PORT=3001 npm start
PORT=5001 npm run server
```

### Clear Node Modules
```bash
rm -rf node_modules
npm install
```

### Update Dependencies
```bash
npm update
```

### View Logs
```bash
npm start 2>&1 | tee app.log
```

---

## ✅ Checklist Before Production

- [ ] All dependencies installed
- [ ] No console errors
- [ ] API endpoints working
- [ ] File previews working
- [ ] Download functionality tested
- [ ] Responsive on mobile
- [ ] Performance acceptable
- [ ] Security checks passed
- [ ] Documentation updated
- [ ] Build succeeds

---

Happy coding! 🚀
