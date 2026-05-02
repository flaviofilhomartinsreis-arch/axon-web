import streamlit as st
import pandas as pd
from supabase import create_client, Client

# --- 1. CONFIGURAÇÕES INICIAIS ---
st.set_page_config(page_title="Axon - Inteligência em SST", layout="wide")

# --- 2. CONEXÃO COM SUPABASE (Via Secrets) ---
# O Streamlit lerá automaticamente as chaves que você salvou nas 'Secrets'
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# --- 3. LÓGICA DE ACESSO RESTRITO ---
def verificar_login():
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    with st.sidebar:
        st.markdown("### 🔐 Área Restrita")
        if not st.session_state.autenticado:
            senha = st.text_input("Senha Admin Axon:", type="password")
            if st.button("Acessar"):
                if senha == st.secrets["SENHA_ADMIN"]:
                    st.session_state.autenticado = True
                    st.success("Acesso liberado!")
                    st.rerun()
                else:
                    st.error("Senha incorreta.")
        else:
            if st.button("Sair / Logoff"):
                st.session_state.autenticado = False
                st.rerun()
    
    return st.session_state.autenticado

# --- 4. FUNÇÕES DE BANCO DE DADOS ---
def buscar_dados():
    # Busca os dados reais que você inseriu no Supabase
    response = supabase.table("clientes_conformidade").select("*").execute()
    return pd.DataFrame(response.data)

def salvar_novo_laudo(empresa, estado, doc, status, vencimento):
    dados = {
        "empresa": empresa,
        "estado": estado,
        "documento": doc,
        "status": status,
        "vencimento": str(vencimento),
        "tecnico_responsavel": "Eng. Flávio Filho"
    }
    supabase.table("clientes_conformidade").insert(dados).execute()

# --- 5. INTERFACE PRINCIPAL ---
if verificar_login():
    st.header("📊 Painel de Gestão Axon (SP & MS)")
    
    # Carrega os dados do banco
    df = buscar_dados()
    
    tab1, tab2, tab3 = st.tabs(["Dashboard BI", "Matriz de Conformidade", "Novo Lançamento"])
    
    with tab1:
        st.subheader("Indicadores por Estado")
        if not df.empty:
            # Gráfico comparativo entre SP e MS
            contagem_estado = df['estado'].value_counts().reset_index()
            st.bar_chart(data=contagem_estado, x='estado', y='count', color="#003366")
        else:
            st.info("Nenhum dado encontrado para gerar o BI.")

    with tab2:
        st.subheader("Monitoramento de Prazos")
        st.dataframe(df, use_container_width=True)

    with tab3:
        st.subheader("Cadastrar Novo Laudo Técnico")
        with st.form("form_laudo"):
            col1, col2 = st.columns(2)
            with col1:
                emp = st.text_input("Nome da Empresa")
                est = st.selectbox("Estado", ["SP", "MS"])
            with col2:
                doc = st.selectbox("Documento/NR", ["PGR", "LTCAT", "NR-10", "NR-12", "PCMSO"])
                venc = st.date_input("Vencimento")
            
            status = st.select_slider("Status", options=["❌ Pendente", "⚠️ Em Prazo", "✅ Concluído"])
            
            if st.form_submit_button("Salvar no Supabase"):
                salvar_novo_laudo(emp, est, doc, status, venc)
                st.success(f"Empresa {emp} cadastrada com sucesso!")
                st.rerun()
else:
    # Tela para quem não está logado
    st.info("Aguardando login na barra lateral para exibir dados de engenharia.")
