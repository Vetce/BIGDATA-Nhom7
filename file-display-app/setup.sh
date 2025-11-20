#!/bin/bash

# BIGDATA File Display App - Complete Setup Guide
# This script will install and prepare everything

set -e

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  BIGDATA File Display App - Setup & Installation             ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check Node.js
echo "🔍 Checking prerequisites..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js 14+ from https://nodejs.org"
    exit 1
fi

NODE_VERSION=$(node -v)
NPM_VERSION=$(npm -v)
echo "✅ Node.js: $NODE_VERSION"
echo "✅ npm: $NPM_VERSION"
echo ""

# Navigate to app directory
APP_DIR="/home/sirin/BIGDATA/file-display-app"
cd "$APP_DIR"
echo "📂 Working directory: $APP_DIR"
echo ""

# Install frontend dependencies
echo "📦 Installing frontend dependencies..."
if npm install > /tmp/npm-frontend.log 2>&1; then
    echo "✅ Frontend dependencies installed"
else
    echo "❌ Failed to install frontend dependencies"
    tail -20 /tmp/npm-frontend.log
    exit 1
fi

# Install backend dependencies
echo "📦 Installing backend dependencies..."
if cd server && npm install > /tmp/npm-backend.log 2>&1 && cd ..; then
    echo "✅ Backend dependencies installed"
else
    echo "❌ Failed to install backend dependencies"
    tail -20 /tmp/npm-backend.log
    exit 1
fi

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║  ✅ Installation Complete!                                     ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

echo "🚀 To start the application:"
echo ""
echo "   Method 1 - Run everything at once (recommended):"
echo "   $ cd $APP_DIR"
echo "   $ npm run dev"
echo ""
echo "   Method 2 - Run backend and frontend separately:"
echo "   Terminal 1: cd $APP_DIR/server && npm start"
echo "   Terminal 2: cd $APP_DIR && npm start"
echo ""
echo "📱 Frontend: http://localhost:3000"
echo "🖥️  Backend:  http://localhost:5000"
echo ""
echo "📚 Full documentation: $APP_DIR/README.md"
echo ""
