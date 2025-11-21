@echo off
REM Start Backend Server Only

echo.
echo ===============================================================
echo   Starting Backend Server
echo ===============================================================
echo.

set APP_DIR=%~dp0..\file-display-app

cd /d "%APP_DIR%\server"
if %errorlevel% neq 0 (
    echo [ERROR] Could not find server directory
    pause
    exit /b 1
)

echo [INFO] Server starting at http://localhost:5000
echo.
npm start

pause
