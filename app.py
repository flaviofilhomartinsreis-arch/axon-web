import streamlit as st
import pandas as pd
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Axon - Inteligência Híbrida em SST", page_icon="🛡️")

# --- ESTILO CORPORATIVO AXON ---
st.markdown("""
    <style>
    .stApp { background-color: #f8fafc; }
    .main-header { background-color: #0f172a; padding: 20px; border-radius: 10px; color: white; margin-bottom: 20px; }
    .card-axon { background-color: white; border-radius: 10px; padding: 20px; border-left: 5px solid #1e3a8a; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .status-aprovado { color: #16a34a; font-weight: bold; }
    .status-alerta { color: #dc2626; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZAÇÃO DE DADOS (SIMULANDO BANCO DE DADOS) ---
if 'historico_propostas' not in st.session_state:
    st.session_state.historico_propostas = []

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    try:
        st.image("nova_logo_axon.png.png", width=160)
    except:
        st.title("AXON SST")
    st.markdown("---")
    menu = st.radio("NÚCLEOS DE OPERAÇÃO", [
        "📊 Painel de Controle", 
        "🛡️ Matriz de Conformidade", 
        "🧠 Análise IA & Validação", 
        "✍️ Biblioteca de Modelos (NRs)",
        "📥 Portal do Contador (XML)",
        "🎓 Axon Academy (EAD)",
        "📄 Proposta Comercial Inteligente"
    ])
    st.markdown("---")
    st.markdown("**Corpo Técnico:**")
    st.write("🔹 **Flávio Filho Martins Reis**")
    st.caption("Eng. Eletricista | Eng. de Seg. do Trabalho")
    st.write("🔹 **Sócia Consultora**")
    st.caption("Técnica de Segurança do Trabalho")

# --- 1. PAINEL DE CONTROLE ---
if menu == "📊 Painel de Controle":
    st.markdown("## 📊 Painel de Controle Estratégico")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.metric("Vidas Ativas", "81", "Regional SP/MS")
    with c2: st.metric("Índice de Conformidade", "78%", "+5%")
    with c3: st.metric("Habilitação Técnica", "92%", "EAD Ativo")
    with c4: st.metric("Propostas em Aberto", len(st.session_state.historico_propostas))

# --- 2. MATRIZ DE CONFORMIDADE ---
elif menu == "🛡️ Matriz de Conformidade":
    st.markdown("## 🛡️ Matriz de Conformidade com Normas Regulamentadoras")
    normas = {
        "NR-01 (PGR)": 100, "NR-10 (Elétrica)": 70, "NR-12 (Máquinas)": 55, 
        "NR-17 (Ergonomia)": 85, "NR-35 (Altura)": 95, "NR-07 (PCMSO)": 80
    }
    for nr, prog in normas.items():
        col1, col2 = st.columns([1, 4])
        col1.write(f"**{nr}**")
        col2.progress(prog/100)

# --- 3. ANÁLISE IA & VALIDAÇÃO ---
elif menu == "🧠 Análise IA & Validação":
    st.markdown("## 🧠 Núcleo de Inteligência e Validação Técnica")
    u1, u2 = st.columns([2, 1])
    with u1:
        doc = st.file_uploader("Upload de Documento para Revisão IA", type=['pdf', 'docx'])
        if doc:
            st.info("🔍 IA Analisando conformidade técnica...")
            st.error("⚠️ Falta item 10.2.4 na NR-10 (Laudo de Aterramento).")
    with u2:
        st.subheader("Validação Humana")
        st.checkbox("Validado por Eng. Flávio Filho")
        st.checkbox("Validado por Sócia Consultora")
        st.button("Aprovar e Publicar Documento")

# --- 4. BIBLIOTECA DE MODELOS (NRs) ---
elif menu == "✍️ Biblioteca de Modelos (NRs)":
    st.markdown("## ✍️ Biblioteca de Modelos Validados Axon")
    biblioteca = {
        "NR-01": ["PGR completo", "Inventário de Riscos"],
        "NR-10": ["Prontuário (PIE)", "RTI - Relatório Técnico"],
        "NR-12": ["Inventário de Máquinas", "Análise de Risco HRN"]
    }
    sel_nr = st.selectbox("Selecione a NR:", list(biblioteca.keys()))
    sel_doc = st.selectbox("Modelo:", biblioteca[sel_nr])
    st.button(f"📥 Baixar Template Validado - {sel_doc}")

# --- 5. PORTAL DO CONTADOR ---
elif menu == "📥 Portal do Contador (XML)":
    st.markdown("## 📥 Central de Integração eSocial")
    st.write("Auditoria de XMLs para evitar multas por divergência.")
    col_x1, col_x2 = st.columns(2)
    with col_x1:
        st.button("📦 Gerar XML S-2240 (Riscos)")
        st.button("📦 Gerar XML S-2220 (Saúde)")
    with col_x2:
        if st.button("🤖 Auditoria de Divergência SST-Folha"):
            st.warning("⚠️ Divergência: CBO do colaborador X exige NR-35 não identificada na folha.")

# --- 6. AXON ACADEMY (EAD) ---
elif menu == "🎓 Axon Academy (EAD)":
    st.markdown("## 🎓 Axon Academy - Portal EAD")
    aba1, aba2 = st.tabs(["👤 Portal do Aluno", "📜 Emissão de Certificado"])
    
    with aba1:
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Exemplo
        if st.button("Concluir Prova Final"):
            st.session_state.nota = "9.5"
            st.success("Aprovado!")

    with aba2:
        if 'nota' in st.session_state:
            st.markdown(f"""
                <div style="border: 5px solid #1e3a8a; padding: 20px; text-align: center; background-color: white;">
                    <h3>CERTIFICADO DE PROFICIÊNCIA</h3>
                    <p>Certificamos que o colaborador concluiu o treinamento de NR-10.</p>
                    <hr>
                    <p style="font-size: 10px;">
                        <b>Flávio Filho Martins Reis</b><br>
                        Eng. Eletricista | Eng. de Segurança do Trabalho<br><br>
                        <b>Sócia Consultora</b><br>
                        Técnica de Segurança do Trabalho
                    </p>
                </div>
            """, unsafe_allow_html=True)
            st.button("📥 Baixar PDF com QR Code")

# --- 7. PROPOSTA COMERCIAL & CRM ---
elif menu == "📄 Proposta Comercial Inteligente":
    tab1, tab2 = st.tabs(["🆕 Nova Proposta", "📜 Histórico/CRM"])
    
    with tab1:
        with st.form("prop"):
            cliente = st.text_input("Empresa")
            n_func = st.number_input("Funcionários", min_value=1)
            nrs = st.multiselect("NRs Pendentes", ["NR-01", "NR-10", "NR-12", "NR-35"])
            valor = st.number_input("Valor R$")
            if st.form_submit_button("Gerar e Salvar"):
                multa = len(nrs) * n_func * 150.00
                st.session_state.historico_propostas.append({
                    "Cliente": cliente, "Risco": multa, "Valor": valor, "Status": "Pendente"
                })
                st.write(f"**Diagnóstico:** Risco de multa estimado em R$ {multa:,.2f}")
    
    with tab2:
        if st.session_state.historico_propostas:
            st.table(pd.DataFrame(st.session_state.historico_propostas))

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray; font-size:10px;'>Axon - Engenharia e Segurança do Trabalho | Santa Fé do Sul - SP | Aparecida do Taboado - MS</p>", unsafe_allow_html=True)
