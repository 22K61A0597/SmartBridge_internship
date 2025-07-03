
import streamlit as st
import requests

#st.set_page_config(page_title="SmartSDLC - Test Case Generator", layout="wide")
st.title("🧪 Test Case Generator")

backend_url = "http://localhost:8000/generate-test-cases"

code = st.text_area("🧾 Code to test", height=300)

if st.button("🧬 Generate Test Cases"):
    if code.strip():
        with st.spinner("Generating test cases..."):
            try:
                response = requests.post(backend_url, data={"code": code})
                st.subheader("✅ Generated Test Cases:")
                st.code(response.json().get("result", ""), language="python")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter some code first.")
