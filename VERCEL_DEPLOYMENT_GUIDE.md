# Complete Vercel Deployment Guide

This guide walks you through deploying the Air Drawing app to production using Vercel (frontend) + Railway (backend).

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Your Browser                             │
│  (Frontend: HTML/CSS/JS - Hand tracking, Drawing)           │
└────────────────────┬────────────────────────────────────────┘
                     │ WebSocket + HTTP
                     │
        ┌────────────▼────────────┐
        │   Vercel (Frontend)     │
        │  https://your-app.vercel.app
        └────────────┬────────────┘
                     │
                     │ CORS + WebSocket
                     │
        ┌────────────▼────────────┐
        │  Railway (Backend)      │
        │  https://your-backend.railway.app
        │  - FastAPI Server       │
        │  - TrOCR Model          │
        │  - WebSocket Handler    │
        └────────────────────────┘
```

---

## Step 1: Prepare Your Repository

### 1.1 Initialize Git (if not already done)

```bash
cd "D:\projects\BTP full final project\Virtual_paint_and_handwritten-text-recognizer-main"
git init
git add .
git commit -m "Initial commit: Air Drawing App"
```

### 1.2 Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository (e.g., `air-drawing-app`)
3. Push your code:

```bash
git remote add origin https://github.com/YOUR_USERNAME/air-drawing-app.git
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy Backend to Railway

### 2.1 Create Railway Account

1. Go to https://railway.app
2. Click "Start Project"
3. Sign up with GitHub (recommended)

### 2.2 Deploy Backend

**Option A: Using Railway CLI (Recommended)**

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# From your project root, initialize Railway
railway init

# Deploy
railway up
```

**Option B: Using Railway Dashboard**

1. Go to https://railway.app/dashboard
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Select your repository
5. Configure:
   - **Root Directory**: (leave empty)
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

### 2.3 Get Backend URL

After deployment:
1. Go to Railway Dashboard
2. Click your project
3. Click "Deployments"
4. Copy the URL (e.g., `https://air-drawing-backend.railway.app`)

### 2.4 Set Environment Variables (Optional)

In Railway Dashboard → Variables:
- `PORT=8000`
- `PYTHONUNBUFFERED=1`

---

## Step 3: Deploy Frontend to Vercel

### 3.1 Create Vercel Account

1. Go to https://vercel.com
2. Sign up with GitHub

### 3.2 Deploy Frontend

**Option A: Using Vercel CLI**

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# When prompted:
# - Project name: air-drawing-app
# - Framework: Other
# - Root directory: ./frontend
```

**Option B: Using Vercel Dashboard**

1. Go to https://vercel.com/dashboard
2. Click "Add New..." → "Project"
3. Import your GitHub repository
4. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: `./frontend`
   - **Build Command**: (leave empty)
   - **Output Directory**: (leave empty)

### 3.3 Set Environment Variables

In Vercel Dashboard → Settings → Environment Variables:

```
NEXT_PUBLIC_BACKEND_URL=https://your-backend.railway.app
NEXT_PUBLIC_WS_URL=wss://your-backend.railway.app
```

Replace `your-backend.railway.app` with your actual Railway URL.

### 3.4 Redeploy

After setting environment variables:
1. Go to Deployments
2. Click the latest deployment
3. Click "Redeploy"

---

## Step 4: Test Your Deployment

### 4.1 Test Frontend

1. Open your Vercel URL in browser
2. You should see the Air Drawing app
3. Check browser console for errors (F12)

### 4.2 Test Backend Connection

1. Open browser DevTools (F12)
2. Go to Console tab
3. You should see: `WebSocket connected`
4. Try drawing and running OCR

### 4.3 Test Health Endpoint

```bash
curl https://your-backend.railway.app/health
```

Should return:
```json
{
  "status": "ok",
  "frontend": true,
  "model": true,
  "ocr": {...}
}
```

---

## Step 5: Troubleshooting

### Issue: WebSocket Connection Failed

**Symptoms**: Drawing works but OCR doesn't, console shows WebSocket error

**Solution**:
1. Check backend is running: `https://your-backend.railway.app/health`
2. Verify environment variables in Vercel are set correctly
3. Check Railway logs for errors:
   ```bash
   railway logs
   ```
4. Ensure backend URL doesn't have trailing slash

### Issue: Model Download Timeout

**Symptoms**: First OCR request times out (>30 seconds)

**Solution**:
1. This is normal on first request (model downloads ~2GB)
2. Wait 60 seconds for first request
3. Subsequent requests are fast
4. To speed up: use smaller model in `backend/ocr.py`:
   ```python
   DEFAULT_TROCR_MODEL_ID = "microsoft/trocr-base-handwritten"
   ```

### Issue: CORS Error

**Symptoms**: Console shows CORS error

**Solution**:
- Backend already has CORS enabled
- Check that frontend URL matches Vercel domain
- Clear browser cache and reload

### Issue: Training Samples Not Saving

**Symptoms**: Samples save but disappear after restart

**Solution**:
- This is expected on Railway (no persistent storage)
- To fix: Use S3 or database for storage
- Or use Railway with persistent volumes

---

## Step 6: Custom Domain (Optional)

### Add Custom Domain to Vercel

1. Go to Vercel Dashboard → Settings → Domains
2. Add your domain
3. Follow DNS configuration instructions
4. Wait for DNS propagation (5-30 minutes)

### Add Custom Domain to Railway

1. Go to Railway Dashboard → Settings → Domains
2. Add your domain
3. Configure DNS records

---

## Step 7: Monitoring & Logs

### View Backend Logs

**Railway**:
```bash
railway logs
```

**Vercel**:
1. Dashboard → Deployments → Click deployment → Logs

### Monitor Performance

**Railway**:
- Dashboard → Metrics tab

**Vercel**:
- Dashboard → Analytics tab

---

## Step 8: Updates & Redeployment

### Update Backend

```bash
git add backend/
git commit -m "Update backend"
git push origin main
```

Railway will automatically redeploy.

### Update Frontend

```bash
git add frontend/
git commit -m "Update frontend"
git push origin main
```

Vercel will automatically redeploy.

---

## Production Checklist

- [ ] GitHub repository created and pushed
- [ ] Backend deployed to Railway
- [ ] Frontend deployed to Vercel
- [ ] Environment variables set in Vercel
- [ ] WebSocket connection working
- [ ] OCR model loading successfully
- [ ] Hand tracking working
- [ ] Drawing and OCR functioning
- [ ] Health endpoint responding
- [ ] Logs accessible and monitored
- [ ] Custom domain configured (optional)
- [ ] Error tracking enabled (optional)

---

## Cost Estimation

| Service | Free Tier | Cost |
|---------|-----------|------|
| Vercel | 100GB bandwidth/month | Free for most projects |
| Railway | $5 credit/month | $5-50/month depending on usage |
| Total | - | ~$5-10/month |

---

## Next Steps

1. **Add Error Tracking**: Sentry, LogRocket
2. **Add Analytics**: Google Analytics, Vercel Analytics
3. **Add Database**: MongoDB, PostgreSQL for persistent storage
4. **Add Authentication**: Auth0, Firebase
5. **Add CI/CD**: GitHub Actions for automated testing

---

## Support

For issues:
1. Check Railway logs: `railway logs`
2. Check Vercel logs: Dashboard → Deployments
3. Check browser console: F12 → Console
4. Test health endpoint: `https://your-backend.railway.app/health`
5. Verify environment variables are set correctly

---

## Quick Reference

| Task | Command |
|------|---------|
| View backend logs | `railway logs` |
| Deploy backend | `railway up` |
| Deploy frontend | `vercel` |
| Test health | `curl https://your-backend.railway.app/health` |
| View Vercel logs | Dashboard → Deployments → Logs |

---

**Your Air Drawing app is now live! 🎉**
