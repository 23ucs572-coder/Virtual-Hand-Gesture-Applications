@echo off
REM ═══════════════════════════════════════════════════════════════
REM Air Drawing App — Quick Deployment Script (Windows)
REM ═══════════════════════════════════════════════════════════════

setlocal enabledelayedexpansion

echo.
echo 🚀 Air Drawing App — Deployment Script
echo ========================================
echo.

if "%1"=="" (
    echo Usage: deploy.bat [railway^|render^|heroku]
    echo.
    echo Options:
    echo   railway  - Deploy backend to Railway.app
    echo   render   - Deploy backend to Render.com
    echo   heroku   - Deploy backend to Heroku
    echo.
    exit /b 1
)

set PLATFORM=%1

if "%PLATFORM%"=="railway" (
    echo 📦 Deploying to Railway...
    echo.
    echo 1. Install Railway CLI:
    echo    npm i -g @railway/cli
    echo.
    echo 2. Login to Railway:
    echo    railway login
    echo.
    echo 3. Initialize and deploy:
    echo    railway init
    echo    railway up
    echo.
    echo 4. Get your backend URL from Railway dashboard
    echo.
) else if "%PLATFORM%"=="render" (
    echo 📦 Deploying to Render...
    echo.
    echo 1. Go to https://render.com
    echo 2. Click 'New +' ^> 'Web Service'
    echo 3. Connect your GitHub repository
    echo 4. Configure:
    echo    - Build Command: pip install -r backend/requirements.txt
    echo    - Start Command: uvicorn backend.main:app --host 0.0.0.0 --port %%PORT%%
    echo 5. Deploy and get your backend URL
    echo.
) else if "%PLATFORM%"=="heroku" (
    echo 📦 Deploying to Heroku...
    echo.
    echo 1. Install Heroku CLI from https://devcenter.heroku.com/articles/heroku-cli
    echo.
    echo 2. Login and deploy:
    echo    heroku login
    echo    heroku create your-app-name
    echo    git push heroku main
    echo.
    echo 3. Get your backend URL:
    echo    heroku open
    echo.
) else (
    echo ❌ Unknown platform: %PLATFORM%
    echo Use: railway, render, or heroku
    exit /b 1
)

echo 📝 After backend deployment:
echo    1. Copy the backend URL
echo    2. Deploy frontend to Vercel:
echo       npm i -g vercel
echo       vercel
echo    3. Set environment variables in Vercel:
echo       NEXT_PUBLIC_BACKEND_URL=^<your-backend-url^>
echo       NEXT_PUBLIC_WS_URL=wss://^<your-backend-url^>
echo.
echo ✅ Done! Your app will be live at the Vercel URL
echo.
