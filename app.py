import streamlit as st
from openai import OpenAI

# Page title
st.title("🤖 AI Smart Chatbot")

# Initialize client (API key from secrets)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Input box
user_input = st.text_input("Ask me anything:")

if st.button("Submit"):
    if user_input:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=user_input
        )

        st.write(response.output_text)
