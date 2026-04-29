import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Axon - Gestão de Profissionais", page_icon="🛡️")

# --- ESTILIZAÇÃO CSS (PARA FICAR IGUAL À DATA LIFE) ---
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    /* Topo Azul Estilo Data Life */
    .main-header {
        background-color: #1e40af;
        padding: 10px 20px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .tabela-bg {
        background-color: #f8fafc;
        border-radius: 10px;
        padding: 20px;
    }
    .badge {
        padding: 4px 10px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: bold;
        text-transform: uppercase;
    }
    .status-desmobilizado { background-color: #e2e8f0; color: #64748b; }
    .status-rascunho { background-color: #fef3c7; color: #d97706; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1063/1063302.png", width=50)
    st.title("Painel Axon")
    opcao = st.radio("Menu", ["Relatório de Profissionais", "Auditoria de NRs", "Risco Humano"])

# --- CONTEÚDO PRINCIPAL ---

if opcao == "Relatório de Profissionais":
    # Cabeçalho Superior
    st.markdown("""
        <div class="main-header">
            <span style="font-weight: bold;">DATALIFE GLOBAL | AXON</span>
            <span style="font-size: 12px;">VITTORIA DA SILVA BRITO - deluzps@gmail.com</span>
        </div>
    """, unsafe_allow_html=True)

    col_tit, col_btn = st.columns([3, 1])
    with col_tit:
        st.subheader("Relatório de Profissionais")
    with col_btn:
        st.button("Cadastrar profissional", use_container_width=True)

    # --- BOTÕES DE STATUS (TABS) ---
    st.tabs(["Todos", "Habilitados", "Em análise", "Reprovados", "Rascunhos", "Desmobilizados"])

    # --- FILTROS DE BUSCA ---
    with st.container():
        c1, c2, c3 = st.columns(3)
        with c1: st.selectbox("Tipo de atuação/Polo", ["Todos", "Argo 6", "Argo 8", "Argo 9"])
        with c2: st.selectbox("SubContratadas", ["Todas", "DELUZ PRESTADORA", "Outras"])
        with c3: st.text_input("Pesquisa de profissional", placeholder="Nome do colaborador...")
        st.button("Pesquisar", type="primary")

    st.markdown("---")

    # --- TABELA DE PROFISSIONAIS (ESTILO WHATSAPP IMAGE) ---
    # Simulando os dados da imagem enviada
    dados = [
        {"nome": "ADAM BRUNO SILVA SANTOS", "cargo": "Encarregado de Equipe", "polo": "Argo 8", "status": "Desmobilizado", "data": "15/12/2025"},
        {"nome": "ADRYAN MIKAUE ALMEIDA FERNANDES", "cargo": "Operador de Moto Serra", "polo": "Argo 8", "status": "Desmobilizado", "data": "15/12/2025"},
        {"nome": "ALISSON FILGUEIRA DA SILVA", "cargo": "Operador de Moto Serra", "polo": "Argo 8", "status": "Desmobilizado", "data": "15/12/2025"},
        {"nome": "ANTONIO AUGUSTO MENDES VIEIRA", "cargo": "Encarregado de Equipe", "polo": "Argo 8", "status": "Rascunhos", "data": "16/09/2025"},
    ]

    # Cabeçalho da Tabela
    t1, t2, t3, t4, t5 = st.columns([3, 2, 2, 2, 1])
    t1.markdown("**Profissional**")
    t2.markdown("**Tipo de atuação/Polo**")
    t3.markdown("**Status do Cadastro**")
    t4.markdown("**Data da última atualização**")
    t5.markdown("**Ficha**")
    st.divider()

    # Linhas da Tabela
    for p in dados:
        l1, l2, l3, l4, l5 = st.columns([3, 2, 2, 2, 1])
        
        # Coluna 1: Nome e Empresa Sublinhada
        l1.markdown(f"**{p['nome']}**<br><span style='font-size:10px; color:gray;'>{p['cargo']}<br>ARGO ENERGIA | DELUZ PRESTADORA</span>", unsafe_allow_html=True)
        
        l2.write(p['polo'])
        
        # Status com Badge Colorida
        cor_badge = "status-rascunho" if p['status'] == "Rascunhos" else "status-desmobilizado"
        l3.markdown(f"<span class='badge {cor_badge}'>{p['status']}</span>", unsafe_allow_html=True)
        
        l4.write(p['data'])
        
        # Ícone de PDF
        l5.button("📄", key=p['nome'])

    st.caption(f"Mostrando {len(dados)} de 81 Profissionais")

elif opcao == "Auditoria de NRs":
    st.title("Auditoria Técnica de NRs")
    st.info("Módulo de checklists configurado conforme normas vigentes.")

elif opcao == "Risco Humano":
    st.title("Análise de Risco Humano")
    st.warning("Monitoramento de fadiga em tempo real.")
