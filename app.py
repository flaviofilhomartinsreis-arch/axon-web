import streamlit as st
import pandas as pd
from supabase import create_client, Client

# 1. Configurações de Página e Estilo Customizado (Inspirado na Data Life)
st.set_page_config(page_title="Axon - Engenharia e SST", layout="wide", page_icon="⚡")

# Aplicando as cores da sua logo via CSS
st.markdown("""
    <style>
    /* Esconde menus nativos do Streamlit para parecer um site real */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Navbar customizada */
    .nav-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 5%;
        background-color: #ffffff;
        border-bottom: 2px solid #84bd00; /* Verde da sua logo */
        position: sticky;
        top: 0;
        z-index: 999;
    }
    
    .hero-section {
        background: linear-gradient(135deg, #1d4363 0%, #2a5a82 100%); /* Azul da logo */
        padding: 80px 10%;
        color: white;
        text-align: left;
    }
    
    .stButton>button {
        background-color: #84bd00 !important; /* Verde vibrante */
        color: white !important;
        border-radius: 5px !important;
        border: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Conexão com Supabase
supabase: Client = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])

# 3. Lógica de Sessão e Login
if "user_data" not in st.session_state:
    st.session_state.user_data = None

def login_form():
    # Cabeçalho do Site Estilo Institucional
    st.markdown(f"""
        <div class="nav-container">
            <div style="font-size: 24px; font-weight: bold; color: #1d4363;">AXON</div>
            <div style="font-size: 14px; color: #666;">Engenharia e Segurança do Trabalho</div>
        </div>
        <div class="hero-section">
            <h1 style="font-size: 45px;">Gestão Inteligente de <br><span style="color: #84bd00;">Conformidade Técnica</span></h1>
            <p style="font-size: 18px; opacity: 0.9;">Abrangência nacional em SST para sua empresa e contabilidade.</p>
        </div>
    """, unsafe_allow_html=True)

    st.write("##") # Espaçamento
    
    # Formulário de Login centralizado
    col1, col2, col3 = st.columns([1, 1.5, 1])
    with col2:
        with st.container(border=True):
            st.subheader("🔐 Acesse a Plataforma")
            email = st.text_input("E-mail cadastrado")
            senha = st.text_input("Senha", type="password")
            if st.button("Entrar no Sistema", use_container_width=True):
                res = supabase.table("usuarios_axon").select("*").eq("email", email).eq("senha_acesso", senha).execute()
                if res.data:
                    st.session_state.user_data = res.data[0]
                    st.rerun()
                else:
                    st.error("Credenciais inválidas para o sistema Axon.")

# 4. Exibição Condicional
if st.session_state.user_data is None:
    login_form()
else:
    # --- ÁREA LOGADA (O QUE O CLIENTE/ADMIN VÊ) ---
    user = st.session_state.user_data
    st.sidebar.image("sua_logo_aqui.png") # Coloque o link da sua logo aqui
    st.sidebar.write(f"Conectado: **{user['email']}**")
    
    if st.sidebar.button("Sair"):
        st.session_state.user_data = None
        st.rerun()

    # Filtro de dados conforme o perfil (Admin, Cliente ou Contador)
    st.title(f"Painel de Gestão: {user['nivel_acesso'].capitalize()}")
    st.info(f"Visualizando dados de: {user['empresa_vinculada']}")
    
    # Aqui entra sua tabela de conformidade e gráficos de BI
    st.divider()
    st.write("### Matriz de Conformidade Nacional")
    # (Código dos gráficos e tabelas que já fizemos antes)
    
