import streamlit as st
import requests
import os
import strip_markdown
import json
from dotenv import load_dotenv
from infrastructure.repositories.data_loader import load_json
from application.use_cases.send_prompt import send_to_debate_api, send_to_sequencial_api
import streamlit as st

load_dotenv()

arquivo = open("data.json", "r", encoding="utf-8")
data_json = load_json("data.json")

# Função para exibir o histórico da conversa
def display_chat_history(messages, column):
    for message in messages:
        with column:
            st.write(f"**Usuário:** {message['user']}")
            if 'llama' in message:
                st.write(f"**Debate:** {message['debate']}")
            if 'gemini' in message:
                st.write(f"**Sequencial:** {message['sequencial']}")

# Inicializando o histórico de mensagens na sessão do Streamlit
st.set_page_config(layout='wide')
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

#st.title("ConnectAI War V0: Llama 3.1 (localhost) Vs Gemini (web)")

st.title("LEDS Battle AI - ConnectAI (V0)                 \n |____Debate VS Sequencial____|")

# st.write("Converse com as IAs LLaMA e Gemini ao mesmo tempo.")

st.markdown("""
    <style>
    .main {
        max-width: 100%;  /* Aumenta a largura da página para 100% */
        padding-left: 0rem;
        padding-right: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)


col1, col2 = st.columns([1, 1])


if st.session_state['messages']:
    with col1:
        st.header("Respostas Debate")
        #display_chat_history(st.session_state['messages'], col1)
    with col2:
        st.header("Respostas Sequencial")
        #display_chat_history(st.session_state['messages'], col2)
    
    

# Caixa de entrada para o usuário
user_input = data_json['payload']

# Botão para enviar a mensagem
if st.button("Enviar"):
    if user_input:
        with st.spinner("Aguardando resposta..."):
           
            st.session_state['messages'].append({'user': user_input, 'debate': '', 'sequencial': ''})
            debate_response = send_message_to_api_debate()
            sequencial_responsse = send_message_to_api_sequencial()

            with col1:
                for message in st.session_state['messages']:
                    st.session_state['messages'][-1]['debate'] = debate_response
                    st.write(f"**Usuário:** {user_input}")
                    st.write(f"**Resultado debate:** {debate_response}")  # Conteúdo gerado
            with col2:
                for message in st.session_state['messages']:
                    st.session_state['messages'][-1]['sequencial'] = sequencial_responsse
                    st.write(f"**Usuário:** {user_input}")
                    st.write(f"**Resultado sequencial:** {sequencial_responsse}")
    else:
        st.warning("Por favor, digite uma mensagem antes de enviar.")


if st.button("Limpar Conversa"):
    st.session_state['messages'] = []
    st.experimental_rerun()