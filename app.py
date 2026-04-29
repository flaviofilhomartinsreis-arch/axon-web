import streamlit as st
import pandas as pd

# --- CONFIGURAÇÕES BÁSICAS ---
NOME_EMPRESA = "NOME DA EMPRESA DA SÓCIA"
CNPJ_SÓCIA = "00.000.000/0001-00"
ENG_RESPONSAVEL = "Flávio Filho Martins Reis"
REGISTRO_ENG = "CREA-SP XXXXXX"

# --- CONFIGURAÇÃO DE CORES EXCLUSIVAS AXON ---
COLOR_PRIMARY = "#064e3b" # Verde Esmeralda
COLOR_ACCENT = "#d4af37"  # Dourado Champagne
COLOR_BG = "#f8fafc"      

st.set_page_config(layout="wide", page_title="Axon | Inteligência em Segurança")

st.markdown(f"""
    <style>
    .stApp {{ background-color: {COLOR_BG}; }}
    [data-testid="stHeader"] {{ background-color: {COLOR_PRIMARY}; }}
    .stButton>button {{
        background-color: {COLOR_PRIMARY};
        color: {COLOR_ACCENT};
        border: 1px solid {COLOR_ACCENT};
        border-radius: 8px;
        font-weight: bold;
    }}
    h1, h2, h3 {{ color: {COLOR_PRIMARY}; font-family: 'Inter', sans-serif; }}
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.image("https://via.placeholder.com/150x50?text=AXON+LOGO", use_column_width=True) # Substituir por sua logo depois
modo = st.sidebar.selectbox("Navegação", 
    ["Dashboard do Cliente", "Mapa de Calor (Humano)", "Gerador de Propostas", "Auditoria de Faturas"])

# --- MÓDULO 1: DASHBOARD (VISUAL DATA LIFE) ---
if modo == "Dashboard do Cliente":
    st.markdown(f"<h1 style='text-align: center;'>AXON</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: {COLOR_ACCENT}; font-weight: bold;'>PAINEL DE SUPERVISÃO OPERACIONAL</p>", unsafe_allow_html=True)
    
    st.subheader("📋 Gestão de Profissionais em Campo (Deluz)")
    
    # Exemplo de Tabela Estilizada
    dados = {
        "Profissional": ["ADRIANO SILVA SANTOS", "CARLOS OLIVEIRA", "MARIANA SANTOS"],
        "Cargo": ["Técnico de Redes", "Eletricista SEP", "Supervisora SST"],
        "Polo": ["Argo 8", "Argo 8", "Argo 8"],
        "Status": ["Mobilizado", "Em Análise", "Em Análise"],
        "Ações": ["👁️ Ver | 📄 PDF", "👁️ Ver | 📄 PDF", "👁️ Ver | 📄 PDF"]
    }
    df = pd.DataFrame(dados)
    st.table(df)

# --- MÓDULO 2: MAPA DE CALOR (PIONEIRISMO) ---
elif modo == "Mapa de Calor (Humano)":
    st.header("🛡️ Human Insight | Prevenção de Erro Humano")
    st.info("Monitoramento preditivo baseado em fadiga e estresse (COPSOQ II).")
    
    col_calor = st.columns(5)
    dias = ["SEG", "TER", "QUA", "QUI", "SEX"]
    for i, d in enumerate(dias):
        with col_calor[i]:
            st.metric(d, "🟢" if i < 3 else "🔴")
            st.caption("Risco " + ("Baixo" if i < 3 else "Crítico"))

# --- MÓDULO 3: GERADOR DE PROPOSTAS ---
elif modo == "Gerador de Propostas":
    st.header("💼 Gerador de Proposta Comercial")
    with st.form("prop_form"):
        cli = st.text_input("Empresa Cliente")
        val = st.number_input("Valor do Projeto (R$)", min_value=0.0)
        enviar = st.form_submit_button("Gerar Visualização")
        
        if enviar:
            st.success(f"Proposta para {cli} gerada com sucesso!")
            st.markdown(f"""
            <div style="border: 2px solid {COLOR_PRIMARY}; padding: 20px; border-radius: 10px;">
                <h3>PROPOSTA COMERCIAL AXON</h3>
                <p><b>Consultoria:</b> {NOME_EMPRESA} | <b>Engenheiro:</b> {ENG_RESPONSAVEL}</p>
                <p><b>Valor Total: R$ {val:,.2f}</b></p>
            </div>
            """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.caption(f"AXON v1.0 | {ENG_RESPONSAVEL}")
