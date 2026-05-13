# Deployment Checklist

## Pre-Deployment

- [ ] Code is working locally
- [ ] All dependencies are in requirements.txt
- [ ] Frontend loads without errors
- [ ] Hand tracking works
- [ ] Drawing works
- [ ] OCR works
- [ ] WebSocket connects

## GitHub Setup

- [ ] GitHub account created
- [ ] Repository created
- [ ] Code pushed to main branch
- [ ] .gitignore is configured
- [ ] No sensitive data in repo

## Backend Deployment (Railway)

### Account Setup
- [ ] Railway account created
- [ ] GitHub connected to Railway
- [ ] Railway CLI installed (optional)

### Configuration
- [ ] Build command set: `pip install -r backend/requirements.txt`
- [ ] Start command set: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
- [ ] Environment variables set (if needed)
- [ ] Dockerfile exists and is correct

### Deployment
- [ ] Backend deployed successfully
- [ ] Deployment shows "Running" status
- [ ] Backend URL copied (e.g., `https://your-backend.railway.app`)
- [ ] Health endpoint responds: `https://your-backend.railway.app/health`

### Verification
- [ ] Backend logs show no errors
- [ ] Model is downloading/loaded
- [ ] No CORS errors in logs

## Frontend Deployment (Vercel)

### Account Setup
- [ ] Vercel account created
- [ ] GitHub connected to Vercel
- [ ] Vercel CLI installed (optional)

### Configuration
- [ ] Framework set to "Other"
- [ ] Root directory set to `./frontend`
- [ ] Build command: (leave empty)
- [ ] Output directory: (leave empty)

### Environment Variables
- [ ] `NEXT_PUBLIC_BACKEND_URL` set to Railway URL
- [ ] `NEXT_PUBLIC_WS_URL` set to Railway URL with `wss://`
- [ ] Variables saved and redeployed

### Deployment
- [ ] Frontend deployed successfully
- [ ] Deployment shows "Ready" status
- [ ] Frontend URL copied (e.g., `https://your-app.vercel.app`)

### Verification
- [ ] Frontend loads without errors
- [ ] No 404 errors for static files
- [ ] No CORS errors in browser console

## Integration Testing

### Frontend → Backend Connection
- [ ] Open frontend URL in browser
- [ ] Browser console shows no errors
- [ ] WebSocket connects (check console)
- [ ] Connection status shows "Connected"

### Hand Tracking
- [ ] Camera permission granted
- [ ] Webcam feed visible
- [ ] Hand tracking working
- [ ] Gestures recognized

### Drawing
- [ ] Can draw with index finger
- [ ] Drawing appears on canvas
- [ ] Eraser works (fist gesture)
- [ ] Undo/Redo works
- [ ] Clear canvas works

### OCR
- [ ] Draw some text
- [ ] Click "Run OCR"
- [ ] Text is recognized
- [ ] Result appears in "Recognized:" bar
- [ ] No errors in browser console

### WebSocket
- [ ] Open browser DevTools (F12)
- [ ] Go to Network tab
- [ ] Filter by "WS"
- [ ] WebSocket connection shows "101 Switching Protocols"
- [ ] Connection is active (not closed)

## Performance Testing

- [ ] First OCR request completes (may take 30-60 seconds)
- [ ] Subsequent OCR requests are fast (<5 seconds)
- [ ] Drawing is smooth (no lag)
- [ ] Hand tracking is responsive
- [ ] No memory leaks (check DevTools)

## Error Handling

- [ ] Backend error returns proper JSON
- [ ] Frontend handles errors gracefully
- [ ] WebSocket reconnects on disconnect
- [ ] No unhandled exceptions in console
- [ ] Error messages are helpful

## Monitoring

- [ ] Railway logs accessible
- [ ] Vercel logs accessible
- [ ] Health endpoint monitored
- [ ] Error tracking enabled (optional)
- [ ] Performance monitoring enabled (optional)

## Documentation

- [ ] README.md updated with deployment info
- [ ] Environment variables documented
- [ ] Troubleshooting guide created
- [ ] API documentation available
- [ ] Deployment guide linked

## Security

- [ ] No API keys in code
- [ ] No passwords in code
- [ ] CORS properly configured
- [ ] HTTPS enforced
- [ ] WebSocket uses WSS (secure)

## Final Checks

- [ ] App works on desktop browser
- [ ] App works on mobile browser
- [ ] App works on different networks
- [ ] App works after 24 hours (no timeouts)
- [ ] Logs show no errors
- [ ] Performance is acceptable
- [ ] All features working

## Post-Deployment

- [ ] Share URL with team
- [ ] Get feedback from users
- [ ] Monitor logs for errors
- [ ] Monitor performance metrics
- [ ] Plan for scaling if needed

## Optional Enhancements

- [ ] Add custom domain
- [ ] Add error tracking (Sentry)
- [ ] Add analytics (Google Analytics)
- [ ] Add authentication
- [ ] Add database for persistent storage
- [ ] Add CI/CD pipeline
- [ ] Add automated tests
- [ ] Add API documentation

---

## Deployment Status

| Component | Status | URL |
|-----------|--------|-----|
| Backend (Railway) | ⬜ | |
| Frontend (Vercel) | ⬜ | |
| WebSocket | ⬜ | |
| OCR Model | ⬜ | |
| Hand Tracking | ⬜ | |

**Legend**: ⬜ = Not Started, 🟨 = In Progress, 🟩 = Complete, 🔴 = Failed

---

## Troubleshooting Quick Links

| Issue | Solution |
|-------|----------|
| WebSocket fails | Check backend URL in env vars |
| Model timeout | Wait 60 seconds on first request |
| CORS error | Check backend CORS config |
| Drawing lag | Check browser performance |
| Hand tracking fails | Check camera permissions |
| Samples not saving | Use S3 or database |

---

## Support Contacts

- Railway Support: https://railway.app/support
- Vercel Support: https://vercel.com/support
- GitHub Support: https://support.github.com

---

**Last Updated**: May 13, 2026

**Deployment Date**: _______________

**Deployed By**: _______________

**Notes**: 
```
_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
```

---

**Ready to deploy? Start with QUICK_DEPLOY.md! 🚀**
