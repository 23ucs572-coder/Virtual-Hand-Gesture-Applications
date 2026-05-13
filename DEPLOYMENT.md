# Deployment Guide

This project consists of two parts:
- **Frontend**: Static HTML/CSS/JS (deploy to Vercel)
- **Backend**: FastAPI with TrOCR (deploy to Railway, Render, or Heroku)

## Option 1: Vercel Frontend + Railway Backend (Recommended)

### Backend Deployment on Railway

1. **Create Railway Account**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Deploy Backend**
   ```bash
   # Install Railway CLI
   npm i -g @railway/cli
   
   # Login
   railway login
   
   # Create new project
   railway init
   
   # Deploy
   railway up
   ```

3. **Get Backend URL**
   - After deployment, Railway will provide a URL like: `https://your-project.railway.app`
   - Copy this URL

4. **Set Environment Variables in Railway**
   - Go to Railway Dashboard → Your Project → Variables
   - Add: `PORT=8000`

### Frontend Deployment on Vercel

1. **Create Vercel Account**
   - Go to https://vercel.com
   - Sign up with GitHub

2. **Deploy Frontend**
   ```bash
   # Install Vercel CLI
   npm i -g vercel
   
   # Deploy
   vercel
   ```

3. **Configure Environment Variables**
   - In Vercel Dashboard → Settings → Environment Variables
   - Add:
     ```
     NEXT_PUBLIC_BACKEND_URL=https://your-railway-backend.railway.app
     NEXT_PUBLIC_WS_URL=wss://your-railway-backend.railway.app
     ```

4. **Update Frontend Config**
   - The frontend will automatically use the backend URL from environment variables

---

## Option 2: Vercel Frontend + Render Backend

### Backend Deployment on Render

1. **Create Render Account**
   - Go to https://render.com
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository

3. **Configure Service**
   - **Name**: `air-drawing-backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free (or Paid for better performance)

4. **Set Environment Variables**
   - Add `PORT=8000`

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy

6. **Get Backend URL**
   - After deployment, Render provides a URL like: `https://your-project.onrender.com`

### Frontend Deployment on Vercel

Same as Option 1, but use the Render URL instead of Railway URL.

---

## Option 3: Vercel Frontend + Heroku Backend

### Backend Deployment on Heroku

1. **Create Heroku Account**
   - Go to https://www.heroku.com
   - Sign up

2. **Install Heroku CLI**
   ```bash
   # Windows
   choco install heroku-cli
   
   # Or download from https://devcenter.heroku.com/articles/heroku-cli
   ```

3. **Deploy**
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

4. **Get Backend URL**
   - Heroku provides: `https://your-app-name.herokuapp.com`

---

## Important Notes

### WebSocket Configuration

The frontend automatically detects the backend URL:
- If running on `localhost` → uses `ws://localhost:8000`
- If running on production → uses `wss://your-backend-url` (secure WebSocket)

### CORS Configuration

The backend already has CORS enabled for all origins:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### File Storage Limitations

**Important**: Vercel and serverless platforms don't have persistent storage.

- Training samples saved to `custom_dataset/` will be **lost** after deployment
- For persistent storage, use:
  - **AWS S3** for image storage
  - **MongoDB** or **PostgreSQL** for labels
  - **Railway/Render** persistent volumes

### Model Loading

The first request will be slow (30-60 seconds) because:
1. TrOCR model downloads from HuggingFace (~2GB)
2. Model loads into memory
3. Subsequent requests are fast

To speed this up:
- Use a smaller model: `microsoft/trocr-base-handwritten` (400MB)
- Pre-download the model during build

---

## Quick Start: Deploy in 5 Minutes

### 1. Deploy Backend to Railway

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login and deploy
railway login
railway init
railway up
```

Copy the Railway URL (e.g., `https://your-project.railway.app`)

### 2. Deploy Frontend to Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# When prompted for environment variables:
# NEXT_PUBLIC_BACKEND_URL = https://your-project.railway.app
# NEXT_PUBLIC_WS_URL = wss://your-project.railway.app
```

### 3. Done!

Your app is now live at the Vercel URL provided.

---

## Troubleshooting

### WebSocket Connection Fails

**Problem**: `WebSocket connection failed`

**Solution**:
1. Check backend is running: `https://your-backend-url/health`
2. Verify CORS is enabled
3. Use `wss://` (secure) for HTTPS frontends
4. Check firewall/proxy settings

### Model Download Timeout

**Problem**: First request times out

**Solution**:
1. Use smaller model in `backend/ocr.py`:
   ```python
   DEFAULT_TROCR_MODEL_ID = "microsoft/trocr-base-handwritten"
   ```
2. Pre-download model during build
3. Increase timeout in frontend

### Training Samples Not Saving

**Problem**: Samples saved but disappear after restart

**Solution**:
- This is expected on serverless platforms
- Use S3 or database for persistent storage
- Or use Railway/Render with persistent volumes

---

## Production Checklist

- [ ] Backend deployed and running
- [ ] Frontend deployed and running
- [ ] WebSocket connection working
- [ ] OCR model loading successfully
- [ ] Hand tracking working in browser
- [ ] Drawing and OCR functioning
- [ ] Environment variables set correctly
- [ ] CORS configured properly
- [ ] Error logging enabled
- [ ] Performance monitoring enabled

---

## Support

For issues:
1. Check backend logs: `railway logs` or Render/Heroku dashboard
2. Check browser console for frontend errors
3. Test health endpoint: `https://your-backend-url/health`
4. Verify WebSocket connection in browser DevTools
