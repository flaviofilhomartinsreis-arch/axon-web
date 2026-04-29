import streamlit as st
import pandas as pd

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="AXON | Intelligence", page_icon="🛡️")

# --- CSS CUSTOMIZADO (O "BANHO DE LOJA") ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #f0f2f6;
    }

    /* Cabeçalho Premium */
    .main-header {
        background: linear-gradient(90deg, #064e3b 0%, #0a3d31 100%);
        padding: 40px;
        border-radius: 15px;
        color: #d4af37;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        border-bottom: 4px solid #d4af37;
    }

    /* Cartões de Métricas */
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #d4af37;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }

    /* Estilização de Botões */
    .stButton>button {
        width: 100%;
        background: #064e3b;
        color: #d4af37 !important;
        border: 2px solid #d4af37;
        border-radius: 8px;
        height: 3em;
        font-weight: bold;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background: #d4af37;
        color: #064e3b !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<div class="main-header"><h1>AXON SYSTEM</h1><p>INTEGRATED RISK MANAGEMENT & ENGINEERING</p></div>', unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color: #064e3b;'>Navegação</h2>", unsafe_allow_html=True)
    menu = st.radio("", ["📊 Dashboard Operacional", "🔥 Mapa de Calor Humano", "📝 Propostas Lux", "📋 Auditoria"])
    st.markdown("---")
    st.info("Logado como: **Flávio Filho**")

# --- MÓDULOS ---
if menu == "📊 Dashboard Operacional":
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="metric-card"><h3>Ativos</h3><h2>142</h2><p style="color:green">↑ 12% este mês</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>Incidentes</h3><h2>0</h2><p style="color:blue">Meta atingida</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><h3>Eficiência</h3><h2>98.4%</h2><p style="color:gold">Padrão Ouro</p></div>', unsafe_allow_html=True)

    st.write("### 📋 Status da Equipe (Deluz)")
    df = pd.DataFrame({
        "Profissional": ["ADRIANO SILVA", "CARLOS OLIVEIRA", "MARIANA SANTOS"],
        "Risco": ["Baixo", "Médio", "Baixo"],
        "Status": ["✅ Em Campo", "⚠️ Em Análise", "✅ Em Campo"]
    })
    st.dataframe(df, use_container_width=True)

elif menu == "🔥 Mapa de Calor Humano":
    st.subheader("🛡️ Análise Preditiva de Erro Humano")
    st.warning("Monitoramento em tempo real baseado em COPSOQ II.")
    # Aqui entrará o gráfico de calor real
    st.image("https://raw.githubusercontent.com/streamlit/fluent-ui-components/master/docs/heat-map.png", caption="Exemplo de Concentração de Fadiga por Polo")

elif menu == "📝 Propostas Lux":
    st.markdown("### 💼 Geração de Documentos de Autoridade")
    with st.expander("Nova Proposta Comercial", expanded=True):
        cliente = st.text_input("Nome do Cliente")
        servico = st.selectbox("Serviço", ["Consultoria NR-10", "Prontuário de Instalações", "Treinamento SEP"])
        if st.button("GERAR PROPOSTA PREMIUM"):
            st.success("Documento gerado com sucesso!")
            st.markdown(f"""
                <div style="padding:20px; border:1px solid #d4af37; background:white;">
                    <h2 style="color:#064e3b">PROPOSTA COMERCIAL AXON</h2>
                    <p><b>Cliente:</b> {cliente}</p>
                    <p><b>Serviço:</b> {servico}</p>
                    <hr>
                    <p><i>Este documento possui certificação digital de engenharia.</i></p>
                </div>
            """, unsafe_allow_html=True)
