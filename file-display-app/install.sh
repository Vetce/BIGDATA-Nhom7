#!/bin/bash

echo "🚀 BIGDATA File Display App - Quick Start"
echo "=========================================="

# Check if Node.js is installed
if ! command -v node &> /dev/null
then
    echo "❌ Node.js is not installed. Please install Node.js 14+ first."
    exit 1
fi

echo "✅ Node.js version: $(node --version)"
echo "✅ npm version: $(npm --version)"
echo ""

# Change to app directory
cd /home/sirin/BIGDATA/file-display-app

echo "📦 Installing frontend dependencies..."
npm install

echo ""
echo "📦 Installing backend dependencies..."
cd server
npm install
cd ..

echo ""
echo "✅ Installation complete!"
echo ""
echo "🎉 To start the application, run one of these commands:"
echo ""
echo "   Option 1 (Recommended): npm run dev"
echo "   - Runs both backend and frontend"
echo ""
echo "   Option 2 (Manual):"
echo "   - Terminal 1: cd server && npm start"
echo "   - Terminal 2: npm start"
echo ""
echo "📱 Frontend will open at: http://localhost:3000"
echo "🖥️  Backend API at: http://localhost:5000"
