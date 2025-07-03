
import streamlit as st
import requests

#st.set_page_config(page_title="SmartSDLC - Bug Fixer", layout="wide")
st.title("🐞 Bug Fixer")
st.write("Paste your Python code with bugs below. The AI will analyze and return the fixed version.")

backend_url = "http://localhost:8000/fix-bugs"

code_input = st.text_area("🧾 Buggy Code", height=300)

if st.button("🔧 Fix Bugs"):
    if code_input.strip():
        with st.spinner("Fixing bugs..."):
            try:
                response = requests.post(backend_url, data={"code": code_input})
                st.subheader("✅ Fixed Code:")
                st.code(response.json().get("result", ""), language="python")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please paste some code before clicking 'Fix Bugs'.")
