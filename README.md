# AI Proxy Traffic Analyzer

## Overview

An **AI-assisted proxy log analyzer** that identifies behavioral patterns, traffic anomalies, suspicious domain characteristics, and potential risk indicators using LLM-based log interpretation.

This system focuses on **traffic pattern analysis and anomaly detection**, NOT security threat confirmation or malware detection.

## What This System Does

### ✅ Demonstrates:
- **Proxy traffic monitoring** - Analyze request patterns and volumes
- **Behavioral pattern detection** - Identify user access behaviors
- **Anomaly hints** - Flag unusual traffic patterns for investigation
- **Domain risk scoring** - Evaluate domain characteristics
- **HTTP vs HTTPS analysis** - Track protocol usage patterns
- **Traffic clustering** - Group related requests
- **Automation detection** - Identify bot-like behaviors

### ❌ Does NOT:
- Detect or confirm malware infections
- Identify botnets or C2 servers
- Confirm cyberattacks or intrusions
- Attribute traffic to threat actors
- Provide definitive security verdicts

> **Important:** This tool provides pattern insights and indicators for further investigation, not security threat detection.

## Fixed Issues

### Previous Errors:
1. ❌ **UnicodeDecodeError** - File encoding issues with non-UTF8 characters
2. ❌ **Token Limit Exceeded** - Large files exceeded API token limits
3. ❌ **No Error Handling** - Crashes with no user-friendly error messages
4. ❌ **Memory Issues** - Loading entire large files into memory
5. ❌ **API Safety Blocks** - Content being blocked by safety filters

### Solutions Implemented:
1. ✅ **Multiple Encoding Support** - Tries UTF-8 first, falls back to latin-1
2. ✅ **Smart Chunking** - Limits data to 30K characters with beginning + end sampling
3. ✅ **Comprehensive Error Handling** - Try-catch blocks with user-friendly messages
4. ✅ **File Size Validation** - Warns users about large files (>10MB)
5. ✅ **Safety Settings** - Configured to handle security log content
6. ✅ **Better UX** - Progress indicators, file info, line counts, download reports

## How to Use

### 🚀 Quick Start (3 Steps!)

**Step 1:** Get your API key from https://aistudio.google.com/app/apikey

**Step 2:** Open `.env` file and replace `your-gemini-api-key-here` with your actual key

**Step 3:** Double-click `run.bat` (or run `streamlit run app.py`)

That's it! 🎉

### 📝 Detailed Steps

#### 1. Install Dependencies (First time only)
```bash
pip install -r requirements.txt
```

#### 2. Set Up API Key
Open `.env` file and edit:
```
GEMINI_API_KEY=your-actual-api-key-here
```

#### 3. Run the App
**Option A (Easiest):** Double-click `run.bat`

**Option B (Manual):**
```bash
streamlit run app.py
```
- Click "Browse files" button
- Select your proxy.log file (supports .txt and .log)
- Review the preview
- Click "🔬 Analyze Logs"

## Features

- 📁 **File Size Detection** - Shows file size and line count
- 🔍 **Smart Preview** - Preview first 500 characters
- 🤖 **AI-Powered Pattern Analysis** - Comprehensive traffic analysis including:
  - Traffic summary and statistics
  - Domain risk scoring
  - Behavioral pattern detection
  - Anomaly hints and indicators
  - HTTP/HTTPS usage analysis
  - Traffic clustering insights
  - Automation detection
  - Traffic monitoring recommendations
- 📥 **Export Results** - Download analysis report as text file
- ⚠️ **Smart Warnings** - Alerts for large files or encoding issues
- ℹ️ **Clear Disclaimer** - Explains analysis limitations

## Supported File Types
- `.log` files
- `.txt` files

## Best Practices
- Keep log files under 10MB for optimal performance
- Ensure logs are in text format (UTF-8 or Latin-1 encoding)
- For very large files, consider splitting them into smaller chunks

## Troubleshooting

### "GEMINI_API_KEY not set"
Make sure you've set the environment variable before running the app.

### "Failed to decode file"
Try saving your log file with UTF-8 encoding, or the app will automatically try latin-1.

### "Large file detected"
The app will process the first 30K characters and last 5K characters to stay within API limits.
