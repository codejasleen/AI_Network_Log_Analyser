# AI Proxy Traffic Analyzer

<div align="center">

**AI-powered proxy log analysis for traffic pattern detection and behavioral anomaly identification**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ainetworkloganalyser-83azuhi3sqcwwtwxvmi3jw.streamlit.app)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[Live Demo](https://ainetworkloganalyser-83azuhi3sqcwwtwxvmi3jw.streamlit.app) • [Documentation](DEPLOYMENT.md) • [Report Bug](../../issues)

</div>

---

## What is This?

An **AI-assisted proxy log analyzer** that uses Google's Gemini AI to identify behavioral patterns, traffic anomalies, domain risk characteristics, and unusual network behaviors from proxy server logs.

### Educational Focus

This tool demonstrates:
- **Proxy traffic monitoring** - Analyze request patterns and volumes
- **Behavioral pattern detection** - Identify user access behaviors  
- **Anomaly hints** - Flag unusual traffic for investigation
- **Domain risk scoring** - Evaluate domain characteristics
- **HTTP/HTTPS analysis** - Track protocol usage patterns
- **Traffic clustering** - Group related network requests
- **Automation detection** - Identify bot-like behaviors

### What This is NOT

This system does **NOT**:
- Detect or confirm malware infections
- Identify botnets or C2 servers
- Confirm cyberattacks or intrusions
- Attribute traffic to specific threat actors
- Provide definitive security verdicts

> **Note:** This tool provides pattern insights and indicators for further investigation, not security threat detection.

---

## Features

### Core Capabilities

- **AI-Powered Analysis** - Uses Google Gemini 2.5 Flash for intelligent pattern recognition
- **Real-time Streaming** - See analysis results appear word-by-word (3-4x faster than traditional methods)
- **Comprehensive Insights** - 5 analysis sections covering all aspects of traffic patterns
- **Multi-Encoding Support** - Handles UTF-8 and Latin-1 log files automatically
- **Smart File Processing** - Optimized chunking for large files (up to 15K chars analyzed)
- **Export Results** - Download analysis reports as text files
- **Modern UI** - Beautiful Streamlit interface with dark theme

### Analysis Sections

1. **Traffic Summary** - Request counts, domains, timeframe, HTTP/HTTPS ratios
2. **Domain Risk Scoring** - Unusual TLDs, suspicious patterns, non-standard naming
3. **Behavioral Pattern Detection** - Access patterns, frequency analysis, peak times
4. **Anomaly Hints** - Unusual patterns, automation indicators, clustering
5. **Monitoring Recommendations** - Investigation leads and monitoring suggestions

---

## Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/) - Interactive web application
- **AI/ML**: [Google Gemini 2.5 Flash](https://ai.google.dev/) - Large Language Model
- **Language**: Python 3.8+
- **Deployment**: Streamlit Community Cloud

---

## Quick Start

### Option 1: Use Live Demo

Try the app instantly without any setup:

**[Launch Live Demo](https://ainetworkloganalyser-83azuhi3sqcwwtwxvmi3jw.streamlit.app)**

1. Click the link above
2. Upload a proxy log file (or use the sample)
3. Click "Analyze Logs"
4. View real-time streaming results

### Option 2: Run Locally

#### Prerequisites
- Python 3.8 or higher
- Gemini API key ([Get one free](https://aistudio.google.com/app/apikey))

#### Installation

```bash
# Clone the repository
git clone https://github.com/codejasleen/AI_Network_Log_Analyser.git
cd AI_Network_Log_Analyser

# Install dependencies
pip install -r requirements.txt

# Set up API key
# Create .env file and add:
# GEMINI_API_KEY=your-api-key-here

# Run the app
streamlit run app.py
```

**Windows Quick Start:**
```bash
# Double-click run.bat
# Or run:
python -m streamlit run app.py
```

---

## Usage

### 1. Upload Log File

- Click "Browse files" button
- Select your `.log` or `.txt` proxy log file
- See file preview and statistics

### 2. Analyze

- Click "Analyze Logs" button
- Watch real-time streaming analysis
- Progress bar shows analysis status

### 3. Review Results

- Read the 5 analysis sections
- Identify patterns and anomalies
- Download report for record-keeping

### Supported Log Formats

The analyzer works with standard proxy log formats:
```
timestamp ip_address status size method url - direct/ip content_type
```

**Example:**
```
1641024000.123 192.168.1.100 TCP_MISS/200 5432 GET http://example.com/ - DIRECT/1.2.3.4 text/html
```

---

## System Scope

For detailed information about what this system does and doesn't do, see [SYSTEM_SCOPE.md](SYSTEM_SCOPE.md).

### Key Points

**Provides:**
- Traffic pattern analysis
- Behavioral observations
- Anomaly indicators
- Domain risk scoring
- Investigation leads

**Does NOT Provide:**
- Malware detection
- Threat attribution
- Security verdicts
- Intrusion confirmation

---

## Deployment

Deploy your own instance to Streamlit Cloud:

[![Deploy to Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy)

### Quick Deploy Steps

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Sign in with GitHub
4. Click "New app"
5. Select your fork
6. Set main file: `app.py`
7. Add secret: `GEMINI_API_KEY = "your-key"`
8. Deploy

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## Performance

- **Analysis Speed**: 5-10 seconds for typical logs (3-4x faster with streaming)
- **File Size**: Optimized for files up to 10MB
- **Processing**: Intelligent chunking for large files
- **Real-time**: Streaming responses for immediate feedback

---

## Contributing

Contributions are welcome! Feel free to:

- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

---

## Acknowledgments

- **Google AI Studio** - For Gemini API access
- **Streamlit** - For the amazing web framework
- **Python Community** - For excellent libraries

---

## Contact

**Developer**: Jasleen  
**GitHub**: [@codejasleen](https://github.com/codejasleen)  
**Project**: [AI_Network_Log_Analyser](https://github.com/codejasleen/AI_Network_Log_Analyser)

---

<div align="center">

**Star this repo if you find it helpful!**

Made with Streamlit and Google Gemini AI

[Back to Top](#ai-proxy-traffic-analyzer)

</div>
