import streamlit as st
import pandas as pd
from supabase import create_client, Client

# --- 1. CONFIGURAÇÕES DE PÁGINA ---
st.set_page_config(page_title="Axon Nacional - Engenharia & SST", layout="wide")

# --- 2. CONEXÃO SUPABASE (Via Secrets) ---
url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(url, key)

# --- 3. LISTA NACIONAL DE ESTADOS ---
UFS_BRASIL = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 
    'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 
    'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
]

# --- 4. LÓGICA DE ACESSO ---
def verificar_login():
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False
    with st.sidebar:
        st.title("🛡️ Axon Admin")
        st.markdown("---")
        if not st.session_state.autenticado:
            senha = st.text_input("Senha de Acesso Nacional:", type="password")
            if st.button("Liberar Sistema"):
                if senha == st.secrets["SENHA_ADMIN"]:
                    st.session_state.autenticado = True
                    st.rerun()
                else:
                    st.error("Senha inválida.")
        else:
            st.success("Sessão Ativa")
            if st.button("Encerrar Sessão"):
                st.session_state.autenticado = False
                st.rerun()
    return st.session_state.autenticado

# --- 5. FUNÇÕES DE BANCO DE DADOS ---
def buscar_dados():
    response = supabase.table("clientes_conformidade").select("*").execute()
    return pd.DataFrame(response.data)

def salvar_no_banco(empresa, uf, doc, status, vencimento):
    dados = {
        "empresa": empresa,
        "estado": uf,
        "documento": doc,
        "status": status,
        "vencimento": str(vencimento),
        "tecnico_responsavel": "Eng. Flávio Filho"
    }
    supabase.table("clientes_conformidade").insert(dados).execute()

# --- 6. INTERFACE PRINCIPAL ---
if verificar_login():
    st.title("🌐 Axon - Gestão Nacional de SST")
    
    # Busca dados reais
    df_original = buscar_dados()
    
    # --- FILTRO GLOBAL ---
    st.sidebar.markdown("---")
    st.sidebar.subheader("🔍 Filtros de Escala")
    filtro_uf = st.sidebar.multiselect("Filtrar por UF:", options=UFS_BRASIL)

    if filtro_uf:
        df = df_original[df_original['estado'].isin(filtro_uf)]
    else:
        df = df_original

    # --- NAVEGAÇÃO POR ABAS ---
    tab1, tab2, tab3 = st.tabs(["📊 BI Nacional", "📋 Matriz de Conformidade", "➕ Novo Cadastro"])

    with tab1:
        st.subheader("Indicadores por Região")
        if not df.empty:
            col_graph1, col_graph2 = st.columns(2)
            with col_graph1:
                # Volume por Estado
                stats_uf = df['estado'].value_counts().reset_index()
                st.write("**Distribuição por Estado**")
                st.bar_chart(data=stats_uf, x='estado', y='count', color="#003366")
            with col_graph2:
                # Status Geral
                stats_status = df['status'].value_counts().reset_index()
                st.write("**Status de Conformidade**")
                st.bar_chart(data=stats_status, x='status', y='count', color="#008080")
        else:
            st.info("Nenhum dado disponível para os filtros selecionados.")

    with tab2:
        st.subheader("Visualização de Documentos")
        st.dataframe(df, use_container_width=True, hide_index=True)

    with tab3:
        st.subheader("Lançamento de Novo Cliente Nacional")
        with st.form("form_nacional"):
            c1, c2 = st.columns(2)
            with c1:
                nome = st.text_input("Nome da Empresa")
                uf_sel = st.selectbox("Estado (UF)", UFS_BRASIL)
            with c2:
                doc_tipo = st.selectbox("Documento Técnico", ["PGR", "LTCAT", "NR-10", "NR-12", "PCMSO", "PPP"])
                venc_data = st.date_input("Vencimento")
            
            status_sel = st.select_slider("Status de Entrega", options=["❌ Pendente", "⚠️ Em Prazo", "✅ Concluído"])
            
            if st.form_submit_button("Registrar na Base Nacional"):
                if nome:
                    salvar_no_banco(nome, uf_sel, doc_tipo, status_sel, venc_data)
                    st.success(f"Empresa {nome} (UF: {uf_sel}) salva com sucesso!")
                    st.rerun()
                else:
                    st.warning("Por favor, preencha o nome da empresa.")
else:
    st.warning("⚠️ Sistema Protegido. Realize o login na barra lateral para acessar a base nacional.")
