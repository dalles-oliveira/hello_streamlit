import streamlit as st

st.title("Minha primeira aplicação")

st.text('Agora vai um texto explicando a aplicação')

nome_usuario = st.text_input("Digite seu nome:", "")

if(nome_usuario != ""): 
    st.text("Olá {}!!!".format(nome_usuario))