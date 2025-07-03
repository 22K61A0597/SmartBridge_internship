
import streamlit as st
from langchain.llms import OpenAI

#st.set_page_config(page_title="SmartSDLC - ChatBot", layout="wide")
st.title("💬 SDLC Chatbot")

st.markdown("Ask anything about the Software Development Life Cycle (SDLC)")

query = st.text_input("❓ Your question:")

if "history" not in st.session_state:
    st.session_state.history = []

if query:
    llm = OpenAI(temperature=0.7)
    answer = llm(query)
    st.session_state.history.append((query, answer))

for i, (q, a) in enumerate(reversed(st.session_state.history)):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")
