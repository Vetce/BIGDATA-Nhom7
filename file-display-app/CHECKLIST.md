# ✅ Installation & Setup Checklist

## Pre-Installation

- [ ] Node.js 14+ installed
- [ ] npm 6+ available
- [ ] Read/write access to `/home/sirin/BIGDATA/`
- [ ] Internet connection (for npm packages)
- [ ] Terminal/Command prompt access

## Installation Steps

### Step 1: Make Scripts Executable
```bash
chmod +x /home/sirin/BIGDATA/file-display-app/setup.sh
chmod +x /home/sirin/BIGDATA/file-display-app/install.sh
```
- [ ] Scripts are executable

### Step 2: Run Setup Script
```bash
/home/sirin/BIGDATA/file-display-app/setup.sh
```
- [ ] Frontend dependencies installed
- [ ] Backend dependencies installed
- [ ] No error messages
- [ ] Installation completed successfully

### Step 3: Verify Installation
```bash
cd /home/sirin/BIGDATA/file-display-app
npm list | head -20
```
- [ ] React is installed
- [ ] Material-UI is installed
- [ ] Other dependencies listed

### Step 4: Start Backend (Terminal 1)
```bash
cd /home/sirin/BIGDATA/file-display-app/server
npm start
```
- [ ] Server message: "Server running on http://localhost:5000"
- [ ] No error messages
- [ ] "Scanning directories..." message appears

### Step 5: Start Frontend (Terminal 2)
```bash
cd /home/sirin/BIGDATA/file-display-app
npm start
```
- [ ] Webpack compilation successful
- [ ] "compiled successfully" message
- [ ] Browser opens at http://localhost:3000

## Verification Steps

### Check File Access
```bash
ls -la /home/sirin/BIGDATA/quick-result/
ls -la /home/sirin/BIGDATA/Inventory-Management/result/
```
- [ ] Files are readable
- [ ] No permission denied errors

### Test API Endpoints
```bash
curl http://localhost:5000/api/health
curl http://localhost:5000/api/files | head -50
```
- [ ] Health check returns: `{"status":"ok"}`
- [ ] Files endpoint returns JSON with file lists

### Browser Testing
1. Open http://localhost:3000
   - [ ] Page loads without errors
   - [ ] No console errors (F12)
   
2. Tab Visibility
   - [ ] 3 tabs visible: quick-result, Optimize-Delivery, Inventory-Management
   - [ ] Each tab shows file count
   
3. File Display
   - [ ] Files displayed in table format
   - [ ] Columns: Icon, Filename, Type, Size, Modified, Actions
   - [ ] All files listed
   
4. Preview Functionality
   - [ ] Click preview icon on CSV file
   - [ ] Table preview opens
   - [ ] Data displays correctly
   - [ ] Close button works
   
5. Download Functionality
   - [ ] Click download icon on any file
   - [ ] File downloads to Downloads folder
   - [ ] Filename is correct
   
6. File Details
   - [ ] Click details icon
   - [ ] Modal shows file info
   - [ ] Path, size, type displayed
   - [ ] Download button works

## Common Issues & Solutions

### Issue: "Port already in use"
- [ ] Run: `lsof -ti:3000 | xargs kill -9`
- [ ] Run: `lsof -ti:5000 | xargs kill -9`
- [ ] Try again

### Issue: "Module not found"
- [ ] Run: `npm cache clean --force`
- [ ] Run: `rm -rf node_modules package-lock.json`
- [ ] Run: `npm install`

### Issue: "Permission denied"
- [ ] Run: `chmod +r /home/sirin/BIGDATA/quick-result/*`
- [ ] Run: `chmod +r /home/sirin/BIGDATA/Inventory-Management/result/*`

### Issue: "Files not showing"
- [ ] Check backend console for errors
- [ ] Verify directory paths in server/index.js
- [ ] Check file permissions
- [ ] Try refreshing browser

### Issue: "Preview not working"
- [ ] Check file type (.csv, .json, .png supported)
- [ ] Verify file is readable
- [ ] Check browser console for errors
- [ ] Try downloading instead

## Performance Checks

- [ ] Initial page load < 2 seconds
- [ ] File list loads < 1 second
- [ ] Preview loads < 2 seconds
- [ ] Download starts immediately
- [ ] No console warnings

## Security Checks

- [ ] Only allowed directories accessible
- [ ] No directory traversal possible
- [ ] File paths validated
- [ ] CORS properly configured
- [ ] No sensitive info in logs

## Final Verification

### Desktop Browser
- [ ] Chrome: Works ✅
- [ ] Firefox: Works ✅
- [ ] Safari: Works ✅
- [ ] Edge: Works ✅

### Responsive Design
- [ ] Desktop (1920x1080): ✅
- [ ] Tablet (768x1024): ✅
- [ ] Mobile (375x667): ✅

### All Features
- [ ] File browsing: ✅
- [ ] Tabbed navigation: ✅
- [ ] File preview: ✅
- [ ] File download: ✅
- [ ] File details: ✅
- [ ] Error handling: ✅
- [ ] Loading states: ✅
- [ ] Responsive layout: ✅

## Documentation Review

- [ ] README.md read
- [ ] SETUP_GUIDE.md reviewed
- [ ] SUMMARY.md understood
- [ ] DEVELOPMENT.md bookmarked
- [ ] Quick reference available

## Optional: Docker Deployment

```bash
cd /home/sirin/BIGDATA/file-display-app
docker-compose up --build
```
- [ ] Docker installed
- [ ] Image builds successfully
- [ ] Container runs on ports 3000 & 5000
- [ ] App accessible at http://localhost:3000

## Optional: Production Build

```bash
npm run build
serve -s build
```
- [ ] Build completes without errors
- [ ] Build folder created
- [ ] App runs from build folder
- [ ] All features work in production

## System Information

```bash
node --version
npm --version
npm list react
npm list @mui/material
```

Document versions:
- [ ] Node.js version: _______
- [ ] npm version: _______
- [ ] React version: _______
- [ ] Material-UI version: _______

## Success! 🎉

- [ ] All checks passed
- [ ] App is running smoothly
- [ ] Ready for use
- [ ] Documentation saved
- [ ] Support info bookmarked

## Next Steps

1. **Customize** - Edit colors, add directories
2. **Extend** - Add new file previews
3. **Deploy** - Use Docker or production build
4. **Share** - Use with team members
5. **Monitor** - Track file access logs

---

**Installation Date:** _______________

**Notes:** 
```
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

---

For issues, check:
- README.md - Full documentation
- SETUP_GUIDE.md - Detailed setup
- DEVELOPMENT.md - Extension guide
