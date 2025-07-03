import streamlit as st
import requests

st.header("📥 Requirement Classifier")
st.markdown("Upload a PDF file containing software requirements. The app will classify them into SDLC phases and generate user stories.")

uploaded_file = st.file_uploader("📄 Upload Requirements PDF", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("🔍 Analyzing and classifying..."):
        files = {"file": uploaded_file.getvalue()}
        response = requests.post("http://127.0.0.1:8000/upload-requirements", files=files)

        if response.status_code == 200:
            result = response.json()["result"]
            st.markdown("### 🧠 AI-Generated SDLC Classification and User Stories:")
            st.text_area("Result", value=result, height=400)
        else:
            st.error("❌ Failed to process the file. Please try again.")
