#!/usr/bin/env bash

# BIGDATA File Display App - Quick Reference Card

cat << 'EOF'

╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║            📊 BIGDATA FILE DISPLAY APP - QUICK REFERENCE                 ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝

🎯 PROJECT LOCATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   /home/sirin/BIGDATA/file-display-app

🚀 GETTING STARTED (3 STEPS)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   1. chmod +x /home/sirin/BIGDATA/file-display-app/setup.sh
   2. /home/sirin/BIGDATA/file-display-app/setup.sh
   3. cd /home/sirin/BIGDATA/file-display-app && npm run dev

📱 THEN OPEN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Browser:  http://localhost:3000
   Backend:  http://localhost:5000

📂 SCANNED DIRECTORIES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ✅ /home/sirin/BIGDATA/quick-result
   ✅ /home/sirin/BIGDATA/Optimize-Delivery/optimize/result
   ✅ /home/sirin/BIGDATA/Inventory-Management/result

💻 QUICK COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Start App (both backend & frontend)
   $ npm run dev

   Start Backend Only
   $ cd server && npm start

   Start Frontend Only
   $ npm start

   Build for Production
   $ npm run build

   Install Dependencies
   $ npm install

   Use Docker (if installed)
   $ docker-compose up --build

📚 DOCUMENTATION FILES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   README.md               - Full documentation
   SETUP_GUIDE.md          - Detailed setup instructions
   SUMMARY.md              - Quick overview
   DEVELOPMENT.md          - Developer guide
   app.json                - App configuration

✨ FEATURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   📁 Browse files from 3 directories
   👁️  Preview CSV, JSON, and images
   ⬇️  Download any file type
   📊 View file metadata
   🎨 Beautiful Material-UI design
   ⚡ Fast and responsive

🔧 TECH STACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Frontend:  React 18 + Material-UI 5
   Backend:   Node.js + Express 4
   Database:  File system
   Port:      3000 (frontend), 5000 (backend)

🆘 TROUBLESHOOTING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Port In Use
   $ lsof -ti:3000 | xargs kill -9
   $ lsof -ti:5000 | xargs kill -9

   Clear Dependencies
   $ npm cache clean --force && rm -rf node_modules
   $ npm install

   Check Permissions
   $ chmod +r /home/sirin/BIGDATA/quick-result/*

📞 FILE STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   file-display-app/
   ├── public/              HTML & static files
   ├── src/                 React components
   │   ├── App.js
   │   ├── index.js
   │   └── components/
   ├── server/              Express backend
   │   └── index.js
   ├── package.json         Frontend config
   ├── README.md            Documentation
   └── setup.sh             Quick installer

🎉 YOU'RE ALL SET!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   Your BIGDATA File Display App is ready to use!
   
   Next Step: Follow the 3-step Getting Started guide above

EOF

echo ""
