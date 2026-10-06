import streamlit as st

st.set_page_config(
    page_title="Attendance Chatbot",
    page_icon="📚"
)

st.title("📚 Attendance Rules Chatbot")

st.write("The application is working!")

st.success("Streamlit app loaded successfully.")

question = st.chat_input("Ask an attendance question...")

if question:
    st.write("You asked:", question)
