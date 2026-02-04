import streamlit as st

st.title("Tabuada Simples")

valor = st.number_input("Deseja consultar a tabuada de qual número?", step = 0)

if st.button("Exibir Tabuada"):
    st.subheader(f"Tabuada do {valor}")
    for i in range (1,11):
        resultado = valor * i
        st.write(f"**{valor}** x **{i}** = {resultado}")
