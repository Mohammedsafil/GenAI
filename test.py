# import google.generativeai as genai
# from API import My_key
# genai.configure(api_key=My_key)
#
# model = genai.GenerativeModel('gemini-pro')
#
# response = model.generate_content("hey")
# print(response.text)
#
# import streamlit as st
# import google.generativeai as genai
# from API import My_key
#
# # Configure the API key
# genai.configure(api_key=My_key)
# model = genai.GenerativeModel('gemini-pro')
#
# # Streamlit app layout
# st.title("Chat with Generative AI")
#
# # Input text area for user messages
# user_input = st.text_input("You:", "")
#
# # Display the user's message
# if user_input:
#     # Generate a response from the AI
#     response = model.generate_content(user_input)
#     st.text_area("AI:", response.text, height=300, max_chars=1000)
#
# # Optionally, add a button to clear the chat
# if st.button('Clear'):
#     st.text_input("You:", "")
#     st.text_area("AI:", "", height=300, max_chars=1000)

import streamlit as st
import google.generativeai as genai
from API import My_key


genai.configure(api_key=My_key)
model = genai.GenerativeModel('gemini-pro')


st.title("Chat with My AI")


if 'messages' not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:
    if message['role'] == 'user':
        st.text_area("You:", value=message['content'], height=50, max_chars=1000, key=f"user_{message['id']}")
    else:
        st.text_area("AI:", value=message['content'], height=50, max_chars=1000, key=f"ai_{message['id']}")


with st.form(key='chat_form'):
    user_input = st.text_input("Type your message here:", "")
    submit_button = st.form_submit_button('Send')

    if submit_button and user_input:

        message_id = len(st.session_state.messages) + 1
        st.session_state.messages.append({'role': 'user', 'content': user_input, 'id': message_id})


        response = model.generate_content(user_input)
        st.session_state.messages.append({'role': 'ai', 'content': response.text, 'id': message_id})

if st.button('Clear'):
    st.session_state.messages = []


if 'chat_form' in st.session_state:
    st.session_state.chat_form = ""
