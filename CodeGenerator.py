
import streamlit as st
import requests
#st.set_page_config(page_title="SmartSDLC - Code Generator", layout="wide")
st.title("🛠️ AI Code Generator")

backend_url = "http://localhost:8000/generate-code"

prompt = st.text_area("📋 Enter Requirement/User Story", height=200)

if st.button("🚀 Generate Code"):
    if prompt.strip():
        with st.spinner("Generating code..."):
            try:
                response = requests.post(backend_url, data={"prompt": prompt})
                st.subheader("✅ Generated Code:")
                st.code(response.json().get("result", ""), language="python")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a requirement to generate code.")
