import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(page_title="Tabuada Pro", page_icon="🔢")

# --- INJEÇÃO DE CSS ---
st.markdown("""
    <style>
    /* Estiliza o fundo da página */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Estiliza o título principal */
    h1 {
        color: #1E3A8A;
        text-align: center;
        font-family: 'Helvetica', sans-serif;
    }

    /* Estiliza o container dos resultados */
    .resultado-box {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin-bottom: 10px;
        border-left: 5px solid #1E3A8A;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTEÚDO DO APP ---
st.title("🔢 Tabuada Simples")

# Centralizando o input em uma coluna
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    valor = st.number_input("Deseja consultar a tabuada de qual número?", step=1, value=1)
    botao = st.button("Gerar Tabuada", use_container_width=True)

if botao:
    st.markdown("---")
    st.subheader(f"Resultados para o número {valor}:")
    
    # Criando a exibição estilizada
    for i in range(1, 11):
        resultado = valor * i
        # Usando HTML dentro do st.markdown para aplicar a classe CSS
        st.markdown(f"""
            <div class="resultado-box">
                <strong>{valor}</strong> &times; {i} = <strong>{resultado}</strong>
            </div>
        """, unsafe_allow_html=True)