import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    layout="wide", 
    page_title="Axon - BI & Inteligência em SST", 
    page_icon="📊"
)

# --- ESTILO CUSTOMIZADO AXON (CSS) ---
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    
    /* Cabeçalho do Dashboard */
    .header-axon {
        background-color: #ffffff;
        padding: 15px 25px;
        border-radius: 10px;
        border-bottom: 4px solid #00838f;
        margin-bottom: 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Cards de Métricas */
    .metric-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08);
        text-align: center;
        border: 1px solid #e1e8ed;
    }
    .metric-label { font-size: 14px; color: #424242; font-weight: bold; text-transform: uppercase; margin-bottom: 10px;}
    .metric-value { font-size: 32px; color: #00838f; font-weight: bold; }
    
    /* Estilo do Certificado */
    .cert-box {
        border: 8px double #00838f; 
        padding: 30px; 
        text-align: center; 
        background-color: white; 
        color: #424242; 
        font-family: serif;
    }
    </style>
""", unsafe_allow_html=True)

# --- LÓGICA DE CARREGAMENTO DA LOGO ---
def exibir_logo():
    # Nome exato do arquivo que está no seu GitHub (Ref. image_11fc7e.png)
    logo_path = "nova_logo_axon.png"
    
    if os.path.exists(logo_path):
        st.sidebar.image(logo_path, use_column_width=True)
    else:
        st.sidebar.markdown("<h1 style='text-align: center; color: #00838f;'>AXON</h1>", unsafe_allow_html=True)
        st.sidebar.error(f"Arquivo '{logo_path}' não detectado no repositório.")

# --- BARRA LATERAL (NAVEGAÇÃO) ---
with st.sidebar:
    exibir_logo()
    st.markdown("---")
    menu = st.radio("MÓDULOS ESTRATÉGICOS", [
        "📊 Painel de Indicadores", 
        "🛡️ Matriz de Conformidade", 
        "🧠 Análise IA & Validação", 
        "✍️ Biblioteca de Modelos (NRs)",
        "📥 Portal do Contador (XML)",
        "🎓 Axon Academy (EAD)",
        "📄 Proposta Comercial Inteligente"
    ])
    st.markdown("---")
    st.info("**Responsável Técnico:**\n\nEng. Flávio Filho Martins Reis\n\nSST & Engenharia Elétrica")

# --- MÓDULO 1: PAINEL DE INDICADORES ---
if menu == "📊 Painel de Indicadores":
    st.markdown("""
        <div class="header-axon">
            <div>
                <h2 style="color: #00838f; margin:0;">BI - INTELIGÊNCIA EM SST</h2>
                <p style="color: gray; margin:0;">Gestão Operacional Axon</p>
            </div>
            <div style="text-align: right;"><b>Outubro / 2023</b></div>
        </div>
    """, unsafe_allow_html=True)

    # Métricas Principais
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="metric-container"><p class="metric-label">Total ASOs</p><p class="metric-value">329</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="metric-container"><p class="metric-label">Alterados</p><p class="metric-value" style="color:#d32f2f;">42</p></div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="metric-container"><p class="metric-label">Treinamentos OK</p><p class="metric-value">91%</p></div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="metric-container"><p class="metric-label">Conformidade NR</p><p class="metric-value">78%</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # Gráficos
    g1, g2 = st.columns([1, 2])
    with g1:
        df_p = pd.DataFrame({"Tipo": ["Admissional", "Demissional", "Periódico"], "Qtd": [45, 32, 252]})
        fig_p = px.pie(df_p, values='Qtd', names='Tipo', hole=.5, color_discrete_sequence=['#00838f', '#00acc1', '#4dd0e1'])
        st.plotly_chart(fig_p, use_container_width=True)
    with g2:
        df_b = pd.DataFrame({"Mês": ["Ago", "Set", "Out"], "Exames": [55, 62, 85]})
        fig_b = px.bar(df_b, x='Mês', y='Exames', color_discrete_sequence=['#00838f'])
        st.plotly_chart(fig_b, use_container_width=True)

# --- MÓDULO 6: AXON ACADEMY (CERTIFICADOS) ---
elif menu == "🎓 Axon Academy (EAD)":
    st.subheader("📜 Emissão de Certificados Validados")
    
    st.markdown(f"""
        <div class="cert-box">
            <h1 style="color: #00838f; margin-bottom: 5px;">CERTIFICADO DE PROFICIÊNCIA TÉCNICA</h1>
            <p style="font-size: 18px;">Certificamos que o colaborador concluiu com êxito o treinamento técnico.</p>
            <br><br>
            <div style="display: flex; justify-content: space-around; align-items: flex-end;">
                <div style="width: 45%;">
                    <hr style="border: 0; border-top: 1px solid black; margin-bottom: 5px;">
                    <p style="font-size: 11px; line-height: 1.3;">
                        <b>FLÁVIO FILHO MARTINS REIS</b><br>
                        Engenheiro Eletricista<br>
                        Engenheiro de Segurança do Trabalho
                    </p>
                </div>
                <div style="width: 45%;">
                    <hr style="border: 0; border-top: 1px solid black; margin-bottom: 5px;">
                    <p style="font-size: 11px; line-height: 1.3;">
                        <b>SÓCIA CONSULTORA</b><br>
                        Técnica de Segurança do Trabalho
                    </p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.button("📥 Baixar Certificado Oficial (PDF)")

# --- DEMAIS MÓDULOS (PLACEHOLDERS) ---
else:
    st.title(f"Módulo: {menu}")
    st.info("Este módulo está integrado à base de dados da Axon e pronto para processamento.")

# --- RODAPÉ ---
st.markdown(f"""
    <p style='text-align:center; color:gray; font-size:10px; margin-top:50px;'>
        Axon Engenharia e Segurança do Trabalho © {datetime.now().year} | Santa Fé do Sul - SP
    </p>
""", unsafe_allow_html=True)
