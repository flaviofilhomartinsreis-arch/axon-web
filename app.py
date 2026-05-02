import streamlit as st
import pandas as pd
from supabase import create_client, Client

# --- 1. CONFIGURAÇÕES DE PÁGINA E IDENTIDADE VISUAL ---
st.set_page_config(page_title="Axon - Engenharia e SST", layout="wide", page_icon="⚡")

# Cores extraídas da sua logo: Azul (#1d4363) e Verde (#84bd00)
st.markdown("""
    <style>
    /* Esconde elementos nativos para um visual de software profissional */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Estilização da Hero Section (Cabeçalho) */
    .hero-container {
        background-color: #1d4363;
        padding: 40px;
        text-align: center;
        color: white;
        border-radius: 0 0 30px 30px;
        margin-bottom: 30px;
    }
    
    /* Customização dos botões e campos */
    .stButton>button {
        background-color: #84bd00 !important;
        color: white !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        border: none !important;
        height: 3em !important;
    }
    
    /* Centralização do formulário */
    [data-testid="stVerticalBlock"] > div:has(div.stForm) {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. CONEXÃO COM O BANCO DE DADOS ---
# Certifique-se de que estas chaves estão no seu Streamlit Secrets
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# --- 3. GESTÃO DE SESSÃO ---
if "user_data" not in st.session_state:
    st.session_state.user_data = None

# --- 4. FUNÇÕES DE BUSCA (LÓGICA NACIONAL) ---
def buscar_dados(nivel, vinculo):
    query = supabase.table("clientes_conformidade").select("*")
    
    # Filtros baseados no perfil logado
    if nivel == 'cliente':
        query = query.eq("empresa", vinculo)
    elif nivel == 'contador':
        query = query.eq("contador_responsavel", vinculo)
    # Admin não recebe filtro (vê tudo - Abrangência Nacional)
    
    res = query.execute()
    return pd.DataFrame(res.data)

# --- 5. INTERFACE: TELA DE LOGIN ---
if st.session_state.user_data is None:
    # Cabeçalho do Site
    st.markdown("""
        <div class="hero-container">
            <h1 style='margin:0;'>AXON</h1>
            <p style='font-size:1.2rem; opacity:0.9;'>Abrangência nacional em SST para sua empresa e contabilidade.</p>
        </div>
    """, unsafe_allow_html=True)

    # Formulário centralizado conforme image_0536fc.png
    _, col_login, _ = st.columns([1, 1.5, 1])
    with col_login:
        with st.form("login_axon"):
            st.markdown("### 🔐 Acesse a Plataforma")
            email_input = st.text_input("E-mail cadastrado")
            senha_input = st.text_input("Senha", type="password")
            
            if st.form_submit_button("Entrar no Sistema", use_container_width=True):
                # Consulta a tabela de usuários que criamos na Etapa 2
                res = supabase.table("usuarios_axon").select("*").eq("email", email_input).eq("senha_acesso", senha_input).execute()
                
                if res.data:
                    st.session_state.user_data = res.data[0]
                    st.success("Acesso autorizado!")
                    st.rerun()
                else:
                    st.error("Credenciais inválidas para o sistema Axon.")

# --- 6. INTERFACE: ÁREA LOGADA (DASHBOARD) ---
else:
    user = st.session_state.user_data
    
    # Barra Lateral de Navegação
    with st.sidebar:
        st.markdown(f"### Bem-vindo(a),<br>{user['email']}", unsafe_allow_html=True)
        st.markdown(f"**Perfil:** {user['nivel_acesso'].upper()}")
        st.markdown("---")
        if st.button("Sair / Logoff"):
            st.session_state.user_data = None
            st.rerun()

    # Título Principal Dinâmico
    st.title(f"Painel de Gestão - {user['empresa_vinculada']}")
    
    # Carregamento dos dados com filtro de permissão
    df = buscar_dados(user['nivel_acesso'], user['empresa_vinculada'])
    
    # Visualização
    tab1, tab2 = st.tabs(["📊 BI e Indicadores", "📋 Matriz de Documentos"])
    
    with tab1:
        if not df.empty:
            st.subheader("Saúde Ocupacional e Segurança")
            # Gráfico de Status (PGR, LTCAT, etc)
            stats = df['status'].value_counts().reset_index()
            st.bar_chart(data=stats, x='status', y='count', color="#1d4363")
        else:
            st.info("Aguardando lançamentos técnicos para esta unidade.")

    with tab2:
        st.subheader("Documentação de Engenharia")
        st.dataframe(df, use_container_width=True, hide_index=True)
        
    # Ferramentas exclusivas para o Administrador (Você)
    if user['nivel_acesso'] == 'admin':
        with st.expander("🛠️ Ferramentas do Engenheiro"):
            st.write("Aqui você poderá cadastrar novos laudos e gerenciar usuários em breve.")
