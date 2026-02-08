import streamlit as st
import os
import google.generativeai as genai
import sys

# Try to load .env file (optional - works without it too)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, will use system environment variables

st.set_page_config(page_title="AI Proxy Traffic Analyzer", layout="wide")

st.title("AI Proxy Traffic Analyzer")
st.markdown("Upload your proxy.log file to analyze traffic patterns, behavioral anomalies, and domain characteristics using AI-powered pattern detection")

# Configure API key with error handling
try:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        st.error("⚠️ GEMINI_API_KEY environment variable not set. Please configure your API key.")
        st.stop()
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"⚠️ Failed to configure API: {str(e)}")
    st.stop()

# Initialize model with fallback
model = None
try:
    # Try gemini-2.5-flash first (recommended stable model as of Feb 2026)
    model = genai.GenerativeModel("gemini-2.5-flash")
    st.success("✅ Using model: gemini-2.5-flash")
except Exception as e:
    st.warning(f"⚠️ gemini-2.5-flash not available, trying alternatives...")
    
    # Fallback: Auto-detect available models
    try:
        available_models = genai.list_models()
        compatible_models = [m for m in available_models 
                           if 'generateContent' in m.supported_generation_methods]
        
        if compatible_models:
            # Try models in order of preference
            preferred_order = ['gemini-2.5-pro', 'gemini-3-flash-preview', 'gemini-1.5-pro']
            
            for pref_model in preferred_order:
                for available in compatible_models:
                    if pref_model in available.name:
                        model_name = available.name.replace('models/', '')
                        model = genai.GenerativeModel(model_name)
                        st.info(f"ℹ️ Using fallback model: {model_name}")
                        break
                if model:
                    break
            
            # If no preferred model found, use first available
            if not model and compatible_models:
                model_name = compatible_models[0].name.replace('models/', '')
                model = genai.GenerativeModel(model_name)
                st.info(f"ℹ️ Using available model: {model_name}")
        
        if not model:
            raise Exception("No compatible models found")
            
    except Exception as fallback_error:
        st.error(f"⚠️ Failed to initialize any model")
        st.error(f"Primary error: {str(e)}")
        st.error(f"Fallback error: {str(fallback_error)}")
        st.info("💡 Try these model names: gemini-2.5-flash, gemini-2.5-pro, gemini-1.5-pro")
        st.stop()

# File uploader
uploaded_file = st.file_uploader(
    "Upload proxy.log file", 
    type=["txt", "log"],
    help="Upload a proxy log file (max 10MB recommended)"
)

if uploaded_file is not None:
    try:
        # Get file size
        file_size = uploaded_file.size
        file_size_mb = file_size / (1024 * 1024)
        
        st.info(f"📁 File: **{uploaded_file.name}** ({file_size_mb:.2f} MB)")
        
        # Check file size (warn if > 10MB)
        if file_size_mb > 10:
            st.warning("⚠️ Large file detected. Processing may take longer or fail due to API limits.")
        
        # Read file with proper error handling
        try:
            # Try UTF-8 first
            log_data = uploaded_file.read().decode("utf-8")
        except UnicodeDecodeError:
            # Fallback to latin-1 if UTF-8 fails
            uploaded_file.seek(0)
            try:
                log_data = uploaded_file.read().decode("latin-1")
                st.info("ℹ️ File decoded using latin-1 encoding")
            except Exception as e:
                st.error(f"❌ Failed to decode file: {str(e)}")
                st.stop()
        
        # Count lines
        line_count = log_data.count('\n')
        st.info(f"📊 Total log entries: **{line_count:,}** lines")
        
        # Show preview
        st.subheader("📄 Log Preview (first 500 characters)")
        st.code(log_data[:500], language="text")
        
        # Analyze button
        if st.button("🔬 Analyze Logs", type="primary"):
            # Create placeholder for streaming results
            result_placeholder = st.empty()
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            try:
                # For large files, use smaller chunk for faster processing
                MAX_CHARS = 15000  # Reduced from 30K for faster processing
                
                status_text.text("📊 Preparing log sample...")
                progress_bar.progress(10)
                
                if len(log_data) > MAX_CHARS:
                    st.warning(f"⚠️ Large file detected. Analyzing {MAX_CHARS:,} characters for faster results.")
                    # Take beginning and end samples
                    log_sample = log_data[:MAX_CHARS]
                else:
                    log_sample = log_data
                
                status_text.text("🤖 Sending to AI model...")
                progress_bar.progress(20)
                
                # Simplified, more concise prompt for faster processing
                prompt = f"""Analyze this proxy log and provide CONCISE insights:

**1. Traffic Summary** (2-3 lines): Requests, domains, timeframe, HTTP/HTTPS ratio

**2. Domain Risk Scoring** (top 3-5): Flag unusual TLDs, suspicious patterns

**3. Behavioral Patterns** (2-3 key patterns): Peak times, frequency, automation hints

**4. Anomaly Hints** (top 3): Most notable unusual patterns

**5. Monitoring Recommendations** (2-3 items): What to watch

Keep analysis brief and focused. No definitive malware/botnet claims.

Log sample:
{log_sample}
"""
                
                status_text.text("⚡ Generating analysis (streaming)...")
                progress_bar.progress(30)
                
                # Use streaming for real-time feedback
                response = model.generate_content(prompt, stream=True)
                
                # Display results with streaming
                st.subheader("📊 Traffic Pattern Analysis Results")
                st.info("ℹ️ **Note:** This analysis provides traffic pattern insights and anomaly indicators. It does NOT detect malware, confirm intrusions, or attribute attacks.")
                
                # Stream the response
                full_response = ""
                response_container = st.empty()
                
                for chunk in response:
                    if chunk.text:
                        full_response += chunk.text
                        response_container.markdown(full_response + "▌")  # Add cursor
                        progress_bar.progress(min(90, 30 + len(full_response) // 10))
                
                # Final display without cursor
                response_container.markdown(full_response)
                progress_bar.progress(100)
                status_text.text("✅ Analysis complete!")
                
                # Hide progress after 2 seconds
                import time
                time.sleep(2)
                progress_bar.empty()
                status_text.empty()
                
                # Add download button
                if full_response:
                    st.download_button(
                        label="📥 Download Traffic Analysis Report",
                        data=full_response,
                        file_name="traffic_analysis_report.txt",
                        mime="text/plain"
                    )
                
            except Exception as e:
                progress_bar.empty()
                status_text.empty()
                st.error(f"❌ Analysis failed: {str(e)}")
                st.write("Error details:", sys.exc_info())
                    
    except Exception as e:
        st.error(f"❌ Error processing file: {str(e)}")
        st.write("Please ensure the file is a valid proxy log file.")

# Add footer
st.markdown("---")
st.markdown("💡 **Tip**: For best results, use proxy.log files under 10MB")
