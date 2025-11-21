@echo off
REM Start Frontend Application Only

echo.
echo ===============================================================
echo   Starting Frontend Application
echo ===============================================================
echo.

set APP_DIR=%~dp0..\file-display-app

cd /d "%APP_DIR%"
if %errorlevel% neq 0 (
    echo [ERROR] Could not find application directory
    pause
    exit /b 1
)

echo [INFO] Frontend starting at http://localhost:3000
echo [INFO] Make sure the backend server is running!
echo.
npm start

pause
