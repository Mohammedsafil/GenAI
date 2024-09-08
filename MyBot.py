import streamlit as st
from API import My_key
import  os
import google.generativeai as genai

genai.configure(api_key=My_key)


model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(input):
    try:
        response = chat.send_message(input,stream=True)
        return response
    except:
        return "You're request have some harmfull content"
st.set_page_config(page_title="My Bot")
st.header("Ask my Bot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("USER: ",key="input")
button = st.button("Sent")
button1 = st.button("Clear")


if button and input:
    response = get_gemini_response(input)
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The Response is ")
    for chunck in response:
        st.write(chunck.text)
        st.session_state['chat_history'].append(("Bot",chunck.text))


st.subheader("The Chat history is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
