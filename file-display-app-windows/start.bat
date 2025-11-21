@echo off
REM BIGDATA File Display App - Start Both Backend and Frontend

echo.
echo ===============================================================
echo   Starting BIGDATA File Display App
echo ===============================================================
echo.

set APP_DIR=%~dp0..\file-display-app

REM Start backend in a new window
echo [INFO] Starting backend server...
start "BIGDATA Backend" cmd /k "cd /d %APP_DIR%\server && npm start"

REM Wait a moment for backend to initialize
timeout /t 3 /nobreak >nul

REM Start frontend
echo [INFO] Starting frontend application...
cd /d "%APP_DIR%"
npm start

echo.
echo [INFO] Application is running!
echo Frontend: http://localhost:3000
echo Backend:  http://localhost:5000
echo.
