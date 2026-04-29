import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="AXON | Gestão de Riscos", page_icon="🛡️")

# --- CSS CORPORATIVO (DESIGN SOBRIO) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@300;400;600;700&display=swap');
    
    .stApp {
        background-color: #f8fafc;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #1e293b;
    }

    /* Barra Lateral */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
        color: white;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Cabeçalho de Autoridade */
    .header-painel {
        background-color: #ffffff;
        padding: 1.5rem 2rem;
        border-radius: 8px;
        border-bottom: 3px solid #059669;
        margin-bottom: 2rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }

    /* Cartões de Indicadores */
    .card-metrica {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 6px;
        border: 1px solid #e2e8f0;
        text-align: left;
    }
    .titulo-metrica {
        color: #64748b;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
    }
    .valor-metrica {
        color: #0f172a;
        font-size: 1.8rem;
        font-weight: 700;
    }

    /* Botão Profissional */
    .stButton>button {
        background-color: #059669;
        color: white !important;
        border-radius: 4px;
        border: none;
        font-weight: 600;
        padding: 0.5rem 1.5rem;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #047857;
    }

    /* Ajuste de Tabelas */
    div[data-testid="stTable"] {
        background-color: white;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    st.markdown("## AXON CONSULTORIA")
    st.markdown("---")
    opcao = st.radio(
        "MÓDULOS DE GESTÃO",
        ["Painel de Controle", "Análise de Risco Humano", "Emissão de Documentos"]
    )
    st.markdown("---")
    st.caption("Engenheiro Responsável:")
    st.markdown("**Flávio Filho Martins Reis**")

# --- CONTEÚDO PRINCIPAL ---

# Cabeçalho Fixo
st.markdown(f"""
    <div class="header-painel">
        <h2 style='margin:0; color:#0f172a;'>{opcao.upper()}</h2>
        <p style='margin:0; color:#64748b;'>Sistema Integrado de Engenharia e Segurança Operacional</p>
    </div>
    """, unsafe_allow_html=True)

if opcao == "Painel de Controle":
    # Linha de Indicadores (KPIs)
    col1, col2, col3, col4 = st.columns(4)
    
    metricas = [
        ("Equipamentos Ativos", "142"),
        ("Horas Sem Acidentes", "4.210"),
        ("Alertas de Segurança", "02"),
        ("Conformidade Legal", "98,4%")
    ]
    
    for i, (titulo, valor) in enumerate(metricas):
        with [col1, col2, col3, col4][i]:
            st.markdown(f"""
                <div class="card-metrica">
                    <div class="titulo-metrica">{titulo}</div>
                    <div class="valor-metrica">{valor}</div>
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Área de Dados
    c_esq, c_dir = st.columns([2, 1])

    with c_esq:
        st.markdown("### 📋 Status da Equipe em Campo")
        dados_equipe = {
            "Profissional": ["Adriano Silva", "Carlos Oliveira", "Mariana Santos", "João Pedro"],
            "Especialidade": ["Téc. de Redes", "Eletricista SEP", "Sup. SST", "Eng. de Campo"],
            "Nível de Risco": ["Baixo", "Médio", "Baixo", "Crítico"],
            "Jornada Atual": ["08h 15min", "04h 30min", "06h 00min", "10h 45min"]
        }
        st.table(pd.DataFrame(dados_equipe))

    with c_dir:
        st.markdown("### 📊 Disponibilidade Operacional")
        fig = go.Figure(go.Pie(
            values=[98.4, 1.6],
            labels=['Operacional', 'Manutenção'],
            hole=.6,
            marker_colors=['#059669', '#e2e8f0']
        ))
        fig.update_layout(
            showlegend=True,
            legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
            margin=dict(t=0, b=0, l=10, r=10),
            height=280
        )
        st.plotly_chart(fig, use_container_width=True)

elif opcao == "Emissão de Documentos":
    st.markdown("### 📝 Gerador de Propostas e Laudos Técnicos")
    with st.container():
        st.markdown('<div class="card-metrica">', unsafe_allow_html=True)
        cliente = st.text_input("NOME DO CLIENTE / CONTRATANTE")
        tipo_doc = st.selectbox("TIPO DE DOCUMENTO", ["Laudo NR-10", "Prontuário Elétrico", "Análise de Risco", "Proposta Comercial"])
        if st.button("GERAR DOCUMENTO OFICIAL"):
            st.success(f"Documento para {cliente} preparado para exportação.")
        st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Análise de Risco Humano":
    st.info("Módulo de análise preditiva baseado em dados de jornada e fadiga.")
    st.warning("Aguardando integração com sensores biométricos ou logs de entrada.")
