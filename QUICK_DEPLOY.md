# Quick Deploy in 10 Minutes

## Prerequisites

- GitHub account
- Railway account (https://railway.app)
- Vercel account (https://vercel.com)
- Node.js installed

## Step 1: Push to GitHub (2 min)

```bash
git init
git add .
git commit -m "Air Drawing App"
git remote add origin https://github.com/YOUR_USERNAME/air-drawing-app.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy Backend to Railway (3 min)

```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

**Copy the Railway URL** (e.g., `https://air-drawing-backend.railway.app`)

## Step 3: Deploy Frontend to Vercel (3 min)

```bash
npm install -g vercel
vercel
```

When prompted:
- Project name: `air-drawing-app`
- Framework: `Other`
- Root directory: `./frontend`

**Copy the Vercel URL** (e.g., `https://air-drawing-app.vercel.app`)

## Step 4: Set Environment Variables (2 min)

In Vercel Dashboard:
1. Go to Settings → Environment Variables
2. Add:
   ```
   NEXT_PUBLIC_BACKEND_URL=https://your-railway-url.railway.app
   NEXT_PUBLIC_WS_URL=wss://your-railway-url.railway.app
   ```
3. Redeploy

## Done! 🎉

Your app is live at: `https://your-app.vercel.app`

---

## Troubleshooting

### WebSocket not connecting?
- Check backend is running: `https://your-railway-url.railway.app/health`
- Verify environment variables in Vercel
- Check browser console for errors

### Model taking too long?
- First request downloads model (~2GB), takes 30-60 seconds
- Subsequent requests are fast
- This is normal

### Need to update code?
```bash
git add .
git commit -m "Your changes"
git push origin main
```

Both Railway and Vercel will auto-redeploy.

---

## Useful Commands

```bash
# View backend logs
railway logs

# Redeploy frontend
vercel --prod

# Check backend health
curl https://your-railway-url.railway.app/health
```

---

**Questions? See VERCEL_DEPLOYMENT_GUIDE.md for detailed instructions.**
