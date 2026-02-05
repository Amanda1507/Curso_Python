import streamlit as st

def somar(n1, n2):
        return(n1 + n2)

def subtracao(n1, n2):
        return(n1 - n2)

def multiplicacao(n1, n2): 
        return(n1 * n2)

def divisao(n1, n2):
        if n2 == 0:
            return "Erro: Divisão por zero"
        return(n1 / n2)

st.title("Calculadora simples")
st.subheader("Feito com Streamlit😎")

n1 = st.number_input("Digite o primeiro número: ",value=0.0)
n2 = st.number_input("Digite o segundo número: ",value=0.0)

opcao = st.selectbox(
      "Qual operação deseja realizar?",
      ("+","-","x","/"))

if st.button("Calcular"):
    if opcao == "+":
        resultado = (somar(n1, n2))

    elif opcao == "-":
        resultado = (subtracao(n1, n2)) 

    elif opcao == "x":
        resultado = (multiplicacao(n1, n2))

    elif opcao == "/":
        resultado = (divisao(n1, n2))
    st.text("Resultado:")

    if isinstance(resultado,str):
          st.error(resultado)

    else:
          st.success(f"O resultado é: {resultado}")