import streamlit as st

st.set_page_config(page_title="AI Smart Chatbot")

st.title("🤖 AI Smart Chatbot")

user_input = st.text_input("Ask me anything:")

if st.button("Submit"):
    if user_input:
        st.write("You asked:", user_input)
        st.write("Response will come here...")
    else:
        st.write("Please enter a question")
