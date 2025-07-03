
import streamlit as st
import requests

#st.set_page_config(page_title="SmartSDLC - Code Summarizer", layout="wide")
st.title("📜 Code Summarizer")

backend_url = "http://localhost:8000/summarize-code"

code = st.text_area("📘 Paste your code here", height=300)

if st.button("🧠 Summarize Code"):
    if code.strip():
        with st.spinner("Summarizing..."):
            try:
                response = requests.post(backend_url, data={"code": code})
                st.subheader("📝 Summary:")
                st.success(response.json().get("result", ""))
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please paste some code first.")
