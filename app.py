import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# --- 1. CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    layout="wide", 
    page_title="Axon - BI & Inteligência em SST", 
    page_icon="⚡"
)

# --- 2. SOLUÇÃO DEFINITIVA DE TRANSPARÊNCIA E ESTILO (CSS) ---
st.markdown("""
    <style>
    /* Remove o fundo de xadrez ou qualquer cor sólida da logo na sidebar */
    [data-testid="stSidebar"] [data-testid="stImage"] {
        background-color: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    /* Estilização Geral do App */
    .stApp { background-color: #f8f9fa; }
    
    /* Cabeçalho do Dashboard Axon */
    .header-axon {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border-left: 8px solid #003366; /* Azul Escuro Axon */
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Cards de BI */
    .metric-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        text-align: center;
        border: 1px solid #e9ecef;
    }
    .metric-label { font-size: 13px; color: #6c757d; font-weight: bold; text-transform: uppercase; }
    .metric-value { font-size: 30px; color: #003366; font-weight: bold; margin-top: 5px; }
    .metric-delta { font-size: 14px; color: #28a745; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

# --- 3. LÓGICA DE CARREGAMENTO DA LOGO ---
def carregar_logo_axon():
    # O código vai procurar exatamente pelo nome que está no seu GitHub
    caminho_logo = "nova_logo_axon.png" 
    
    if os.path.exists(caminho_logo):
        return caminho_logo
    return None

# --- 4. BARRA LATERAL (NAVEGAÇÃO) ---
with st.sidebar:
    logo = carregar_logo_axon()
    if logo:
        # Exibe a logo - o CSS acima garante a transparência no navegador
        st.image(logo, use_column_width=True)
    else:
        st.error("⚠️ Arquivo 'nova_logo_axon.png' não encontrado.")
        st.title("AXON")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    menu = st.radio("SISTEMA DE GESTÃO ESTRATÉGICA", [
        "📊 Dashboard de BI (SST)", 
        "🛡️ Matriz de Conformidade", 
        "🧠 Análise de Laudos (IA)", 
        "📥 Portal eSocial (XML)",
        "🎓 Certificados & Treinamentos",
        "📄 Propostas de Engenharia"
    ])
    
    st.markdown("---")
    st.caption(f"**RT:** Eng. Flávio Filho Martins Reis")
    st.caption(f"CREA: SP-0000000 | SST & Elétrica")

# --- 5. MÓDULO PRINCIPAL: DASHBOARD DE BI ---
if menu == "📊 Dashboard de BI (SST)":
    st.markdown("""
        <div class="header-axon">
            <h2 style="color: #003366; margin:0;">BI - INTELIGÊNCIA EM SEGURANÇA E ENGENHARIA</h2>
            <p style="color: #28a745; margin:0; font-weight: 500;">Monitoramento de Conformidade e Gestão Axon</p>
        </div>
    """, unsafe_allow_html=True)

    # Fileiras de Indicadores (KPIs)
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card"><p class="metric-label">Total ASOs</p><p class="metric-value">329</p><p class="metric-delta">↑ 12% vs mês ant.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><p class="metric-label">ASOs Vencidos</p><p class="metric-value" style="color: #dc3545;">08</p><p class="metric-delta" style="color: #dc3545;">Ação Crítica</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="metric-card"><p class="metric-label">Treinamentos OK</p><p class="metric-value">94%</p><p class="metric-delta">Meta: 90%</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="metric-card"><p class="metric-label">Laudos Válidos</p><p class="metric-value">12</p><p class="metric-delta">PGR / PCMSO / LTCAT</p></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Gráficos de Gestão
    g1, g2 = st.columns([1, 1.5])
    
    with g1:
        st.subheader("Distribuição de Exames")
        df_pizza = pd.DataFrame({"Tipo": ["Admissional", "Periódico", "Demissional"], "Qtd": [45, 250, 34]})
        fig_pizza = px.pie(df_pizza, values='Qtd', names='Tipo', hole=.4, 
                           color_discrete_sequence=['#003366', '#28a745', '#6c757d'])
        st.plotly_chart(fig_pizza, use_container_width=True)
        
    with g2:
        st.subheader("Evolução de Eventos eSocial (S-2220 / S-2240)")
        df_bar = pd.DataFrame({
            "Mês": ["Jan", "Fev", "Mar", "Abr"], 
            "Enviados": [120, 150, 180, 210]
        })
        fig_bar = px.bar(df_bar, x="Mês", y="Enviados", color_discrete_sequence=['#003366'])
        st.plotly_chart(fig_bar, use_container_width=True)

# --- 6. MÓDULO DE CERTIFICADOS ---
elif menu == "🎓 Certificados & Treinamentos":
    st.subheader("Emissão de Certificados Profissionais")
    st.info("Utilize este módulo para gerar certificados com validade jurídica assinados digitalmente.")
    
    # Exemplo de visualização de certificado
    st.markdown("""
        <div style="border: 5px solid #003366; padding: 40px; text-align: center; background-color: white;">
            <h1 style="color: #003366;">CERTIFICADO DE TREINAMENTO</h1>
            <p style="font-size: 20px;">NR-10 SEGURANÇA EM INSTALAÇÕES ELÉTRICAS</p>
            <br>
            <p>Certificamos que o colaborador concluiu com aproveitamento o treinamento técnico.</p>
            <br><br>
            <div style="display: flex; justify-content: space-around;">
                <div style="border-top: 1px solid black; width: 200px; font-size: 12px;">
                    Eng. Flávio Filho Martins Reis<br>Engenheiro de Seg. do Trabalho
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- RODAPÉ ---
st.markdown(f"""
    <div style="text-align: center; margin-top: 50px; color: #6c757d; font-size: 12px;">
        Axon Engenharia e Segurança do Trabalho © {datetime.now().year} | Inteligência em SST
    </div>
""", unsafe_allow_html=True)
