# 🚀 Deployment Guide - Streamlit Community Cloud

## Prerequisites
- GitHub account
- Gemini API key from https://aistudio.google.com/app/apikey
- Code pushed to GitHub repository

## Step-by-Step Deployment

### 1. Push to GitHub
```bash
git add .
git commit -m "AI Proxy Traffic Analyzer - Ready for deployment"
git push origin main
```

### 2. Deploy to Streamlit Cloud

1. **Go to:** https://share.streamlit.io/

2. **Sign in** with your GitHub account

3. **Click "New app"**

4. **Fill in deployment settings:**
   - Repository: `your-username/AI_Network_Log_Analyser`
   - Branch: `main`
   - Main file path: `app.py`

5. **Add Secret (IMPORTANT!):**
   - Click "Advanced settings"
   - Go to "Secrets" section
   - Add this:
     ```toml
     GEMINI_API_KEY = "your-actual-api-key-here"
     ```
   - Replace with your real API key from Google AI Studio

6. **Click "Deploy"**

7. **Wait 2-3 minutes** for deployment to complete

8. **Your app will be live at:** `https://your-app-name.streamlit.app`

## Alternative: Deploy Button

Add this badge to your README.md for one-click deployment:

```markdown
[![Deploy to Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy)
```

## Configuration Files

Your repo includes:
- `.streamlit/config.toml` - Theme and server settings
- `requirements.txt` - Python dependencies
- `.gitignore` - Excludes .env (API key protected)

## After Deployment

1. Test the live app with `sample_proxy.log`
2. Share the URL with others
3. Monitor usage in Streamlit Cloud dashboard

## Free Tier Limits

Streamlit Community Cloud free tier includes:
- Unlimited public apps
- 1GB resources per app
- Automatic sleep after inactivity (wakes on visit)

Perfect for this traffic analyzer! 🎉

## Troubleshooting

**App won't start:**
- Check that `GEMINI_API_KEY` is set in secrets
- Verify requirements.txt is correct
- Check deployment logs

**API errors:**
- Verify API key is valid
- Check key has Gemini API access enabled

**Slow performance:**
- Free tier has limited resources
- Consider upgrading if needed
- App auto-sleeps when inactive (normal behavior)
