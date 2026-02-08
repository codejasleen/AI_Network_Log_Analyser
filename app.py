import streamlit as st
import google.generativeai as genai

st.title("AI Network Log Analyzer")

st.write("Upload proxy log file to generate AI insights")

# upload file
uploaded_file = st.file_uploader("Upload proxy.log", type=["txt","log"])

# add your Gemini API key
genai.configure(api_key="AIzaSyCwyy1c9zL93RPqce_Abj-XFctfEuv36KU")

model = genai.GenerativeModel("gemini-1.5-flash")

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
