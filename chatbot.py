
import streamlit as st
from streamlit_chat import message
from utils import get_initial_message, get_chatgpt_response, update_chat
import os
from dotenv import load_dotenv
load_dotenv()
import openai
import requests

api_key = "sk-...YTCE"
url = "https://platform.openai.com/account/api-keys"
username = "hind soubai"
password = "hindou2627"
openai.api_key = "sk-...YTCE"
session = requests.Session()
session.auth = (username, password)
session.headers.update({"Authorization": f"Bearer {api_key}"})

st.title("Chatbot")
st.subheader("AI:")

model = st.selectbox(
    "Select a model",
    ("gpt-3.5-turbo", "gpt-4")
)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

query = st.text_input("Query: ", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()
if query:
    with st.spinner("generating..."):
        messages = st.session_state['messages']
        messages = update_chat(messages, "user", query)
        response = get_chatgpt_response(messages, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)
if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

    with st.expander("Show Messages"):
        st.write(messages)
try:
    response = session.get(url)

    if response.status_code == 200:
        data = response.json()  
        print("Réponse de l'API :", data)
    else:
        print("La requête a échoué. Code de statut :", response.status_code)
except requests.exceptions.RequestException as e:
    print("Une erreur s'est produite lors de la requête :", str(e))