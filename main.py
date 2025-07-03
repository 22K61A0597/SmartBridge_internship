import streamlit as st

st.set_page_config(page_title="SmartSDLC", layout="wide")  # ✅ Only here!

st.sidebar.title("🔧 SmartSDLC Menu")
option = st.sidebar.radio("Go to", [
    "🏠 Home",
    "🛠️ Code Generator",
    "🐞 Bug Fixer",
    "🧪 Test Generator",
    "📜 Code Summarizer",
   
    
])


if option == "🏠 Home":
    st.title("💡 SmartSDLC - AI-Enhanced Software Development Lifecycle")
    st.markdown("Welcome to **SmartSDLC**, your AI companion for software development tasks.")

elif option == "🛠️ Code Generator":
    exec(open("CodeGenerator.py", encoding="utf-8").read())

elif option == "🐞 Bug Fixer":
    exec(open("BugFixer.py", encoding="utf-8").read())

elif option == "🧪 Test Generator":
    exec(open("TestCaseGen.py", encoding="utf-8").read())

elif option == "📜 Code Summarizer":
    exec(open("CodeSummarizer.py", encoding="utf-8").read())

