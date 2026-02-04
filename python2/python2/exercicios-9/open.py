import streamlit as st

st.title("Cadastro")
with st.form(key="meu_formulario", clear_on_submit=True):

    nome = st.text_input("Digite seu nome: ")
    email = st.text_input("Digite seu e-mail: ")
    senha = st.text_input("Digite sua senha: ",type='password')
    confirmar = st.text_input("Confirme sua senha: ",type='password')
    enviar = st.form_submit_button("Cadastrar")

    if enviar:
        if not (nome and email and senha and confirmar):
            st.error("Por favor preencha todos os campos.")

            if confirmar != senha:
                st.error("Senha errada!")

        else:
            with open("./pessoa.txt", "a") as arquivo:
                arquivo.write(f"Nome: {nome}\n E-mail: {email}") 
            st.toast("Usuário cadastrado com sucesso!",icon="✔️")   