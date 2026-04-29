import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="AXON Intelligence", page_icon="🛡️")

# --- CSS PREMIUM (UI/UX INDUSTRIAL) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;500;700&display=swap');
    
    /* Global */
    .stApp { background-color: #0d1117; color: #e6edf3; font-family: 'Roboto', sans-serif; }
    
    /* Sidebar Dark */
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    
    /* Header Comand Center */
    .header-box {
        background: linear-gradient(135deg, #064e3b 0%, #042f24 100%);
        padding: 2rem;
        border-radius: 12px;
        border-left: 8px solid #d4af37;
        margin-bottom: 25px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }
    
    /* Cartões de Monitoramento */
    .stat-card {
        background: #1c2128;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #30363d;
        text-align: center;
        transition: 0.3s ease;
    }
    .stat-card:hover { border-color: #d4af37; transform: translateY(-5px); }
    .stat-val { font-size: 2.5rem; font-weight: 700; color: #d4af37; }
    .stat-label { color: #8b949e; text-transform: uppercase; letter-spacing: 1px; font-size: 0.8rem; }
    
    /* Tabelas Modernas */
    .stDataFrame { border-radius: 10px; overflow: hidden; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR E NAVEGAÇÃO ---
with st.sidebar:
    st.markdown("<h1 style='color: #d4af37; font-size: 22px;'>AXON <span style='color:#fff; font-weight:300;'>INTELLIGENCE</span></h1>", unsafe_allow_html=True)
    st.markdown("---")
    menu = st.radio("SISTEMA OPERACIONAL", ["COMMAND CENTER", "HUMAN RISK MAP", "ENGINEERING DOCS"])
    st.markdown("---")
    st.caption("Engenheiro Responsável")
    st.markdown("**Flávio Filho Martins Reis**")

# --- CABEÇALHO ---
st.markdown("""
    <div class="header-box">
        <h2 style='margin:0; color:#d4af37;'>AXON CONTROL PANEL</h2>
        <p style='margin:0; color:#fff; opacity:0.8;'>Monitoramento em Tempo Real | Planta: Argo 8 - Deluz</p>
    </div>
    """, unsafe_allow_html=True)

# --- COMAND CENTER (DASHBOARD) ---
if menu == "COMMAND CENTER":
    # KPIs Superiores
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="stat-card"><div class="stat-label">Ativos Ativos</div><div class="stat-val">142</div></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="stat-card"><div class="stat-label">HHT S/ Acidentes</div><div class="stat-val">4.2k</div></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="stat-card"><div class="stat-label">Alertas Críticos</div><div class="stat-val" style="color:#ff7b72;">02</div></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="stat-card"><div class="stat-label">Compliance</div><div class="stat-val">98%</div></div>', unsafe_allow_html=True)

    st.markdown("---")
    
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.markdown("### 📋 Status da Força de Trabalho")
        df = pd.DataFrame({
            "Profissional": ["ADRIANO SILVA", "CARLOS OLIVEIRA", "MARIANA SANTOS", "JOÃO PEDRO"],
            "Especialidade": ["Téc. Redes", "Eletricista SEP", "SST", "Eng. Campo"],
            "Risco Humano": ["Baixo", "Médio", "Baixo", "Crítico"],
            "Check-in": ["07:45", "08:12", "07:30", "09:05"]
        })
        st.table(df) # Tabela limpa para contraste no dark mode

    with col_right:
        st.markdown("### 📊 Disponibilidade")
        # Gráfico Donut de Eficiência
        fig = go.Figure(go.Pie(
            values=[98.4, 1.6],
            labels=['Operacional', 'Manutenção'],
            hole=.7,
            marker_colors=['#d4af37', '#30363d']
        ))
        fig.update_layout(showlegend=False, margin=dict(t=0, b=0, l=0, r=0), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)

# --- MAPA DE RISCO ---
elif menu == "HUMAN RISK MAP":
    st.subheader("🔥 Análise de Calor Preditiva")
    st.markdown("Probabilidade de Erro Humano por setor (Baseado em fadiga acumulada).")
    
    # Simulação de Gráfico de Calor
    data = [[1, 20, 30], [20, 1, 60], [30, 60, 1]]
    fig_heat = px.imshow(data, 
                         labels=dict(x="Turno", y="Setor", color="Nível de Risco"),
                         x=['Manhã', 'Tarde', 'Noite'],
                         y=['Rede Elétrica', 'Subestação', 'Administrativo'],
                         color_continuous_scale=['#064e3b', '#d4af37', '#ff7b72'])
    st.plotly_chart(fig_heat, use_container_width=True)

# --- PROPOSTAS ---
elif menu == "ENGINEERING DOCS":
    st.markdown("### 📝 Emissão de Documentos Técnicos")
    with st.container():
        st.markdown('<div class="stat-card">', unsafe_allow_html=True)
        cli = st.text_input("NOME DO CLIENTE / PROJETO")
        tipo = st.selectbox("TIPO DE LAUDO", ["NR-10", "Prontuário Elétrico", "Análise de Risco SEP"])
        if st.button("GERAR PROTOCOLO"):
            st.success(f"Protocolo AXON-{cli[:3].upper()}-2024 gerado.")
        st.markdown('</div>', unsafe_allow_html=True)
