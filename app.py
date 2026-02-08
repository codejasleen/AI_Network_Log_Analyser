import streamlit as st
import google.generativeai as genai

st.title("AI Network Log Analyzer")

st.write("Upload proxy log file to generate AI insights")

# upload file
uploaded_file = st.file_uploader("Upload proxy.log", type=["txt","log"])

# add your Gemini API key
genai.configure("GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_logs(prompt):
    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": 0.3,
            "max_output_tokens": 800,
        }
    )
    return response.text

if uploaded_file is not None:
    log_data = uploaded_file.read().decode("utf-8")

    st.subheader("Log Preview")
    st.text(log_data[:500])

    if st.button("Analyze Logs"):
        prompt = f"""
        You are a cybersecurity analyst.

        Analyze the following network proxy logs and generate:
        1. Traffic summary
        2. Suspicious domains if any
        3. Behavioral pattern insights

        Logs:
        {log_data}
        """

        response = model.generate_content(prompt)
        st.subheader("AI Analysis")
        st.write(response.text)
