import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Axon - BI & Inteligência em SST", page_icon="📊")

# --- ESTILO CUSTOMIZADO (INSPIRADO NO SOC INDICADORES E NOVA LOGO) ---
# Cores da Logo: Teal (#00838f), Grafite (#424242)
st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    
    # /* Remove padding extra do Streamlit para focar no conteúdo */
    .block-container { padding-top: 1rem; padding-bottom: 0rem; }

    /* Cabeçalho Estilo Dashboard BI */
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
    .header-title { color: #00838f; margin:0; font-size: 24px; font-weight: bold; }
    .header-subtitle { color: #424242; font-size: 14px; }

    /* Cards de Métricas Principais */
    .metric-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.08);
        text-align: center;
        border: 1px solid #e1e8ed;
    }
    .metric-label { font-size: 14px; color: #424242; font-weight: bold; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 10px;}
    .metric-value { font-size: 36px; color: #00838f; font-weight: bold; line-height: 1; }
    .metric-delta { font-size: 14px; color: #16a34a; } /* Verde para positivo */
    
    /* Estilo para a Tabela do CRM e Matriz */
    .styled-table { font-size: 14px; }
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZAÇÃO DE ESTADOS (BANCO DE DADOS SIMULADO) ---
if 'historico_propostas' not in st.session_state:
    st.session_state.historico_propostas = [
        {"Data": "01/10/2023", "Cliente": "Usina Delta S/A", "Risco": 150000.00, "Investimento": 12500.00, "Status": "Aprovado"},
        {"Data": "15/10/2023", "Cliente": "Indústria Taboado LTDA", "Risco": 75000.00, "Investimento": 8900.00, "Status": "Pendente"},
    ]

# --- NAVEGAÇÃO LATERAL (BARRA DE FERRAMENTAS) ---
with st.sidebar:
    # --- INTEGRAÇÃO DA LOGO ---
    # Tenta carregar a logo se o arquivo existir
    logo_path = "logo_axon.png"
    if os.path.exists(logo_path):
        st.image(logo_path, use_column_width=True)
    else:
        # Fallback caso a imagem não seja encontrada
        st.markdown("<h1 style='text-align: center; color: #00838f;'>AXON</h1>", unsafe_allow_html=True)
        st.caption("Engenharia e Segurança do Trabalho")
        st.error(f"Arquivo '{logo_path}' não encontrado. Salve a logo na mesma pasta.")

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
    
    # Responsáveis Técnicos em destaque
    st.markdown("**Corpo Técnico Responsável:**")
    col_t1, col_t2 = st.columns([1, 4])
    col_t1.markdown("⚡")
    col_t2.markdown("**Eng. Flávio Filho**\n<span style='font-size:12px; color:gray;'>Elétrica & Seg. do Trabalho</span>", unsafe_allow_html=True)
    
    col_t3, col_t4 = st.columns([1, 4])
    col_t3.markdown("🛡️")
    col_t4.markdown("**Sócia Consultora**\n<span style='font-size:12px; color:gray;'>Técnica de Seg. do Trabalho</span>", unsafe_allow_html=True)

# --- 📊 PAINEL DE INDICADORES (ESTILO SOC & BI) ---
if menu == "📊 Painel de Indicadores":
    # Cabeçalho do Dashboard
    st.markdown("""
        <div class="header-axon">
            <div>
                <h2 class="header-title">INDICADORES ESTRATÉGICOS DE SST</h2>
                <span class="header-subtitle">Gestão Unificada: Santa Fé do Sul | Aparecida do Taboado</span>
            </div>
            <div style="text-align: right;">
                <span class="header-subtitle">Mês de Referência</span><br>
                <b>Outubro / 2023</b>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Primeira Linha: Métricas de Exames e Status (Ref. image_0.png)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown('<div class="metric-container"><p class="metric-label">Total de Exames</p><p class="metric-value">329</p><p class="metric-delta">▲ 5% vs mês ant.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-container"><p class="metric-label">Exames Alterados</p><p class="metric-value" style="color:#d32f2f;">42</p><p class="metric-delta" style="color:#d32f2f;">▲ 2% (Risco)</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-container"><p class="metric-label">Treinamentos Válidos</p><p class="metric-value">91%</p><p class="metric-delta">▲ 1% (Academy)</p></div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<div class="metric-container"><p class="metric-label">Índice Conformidade</p><p class="metric-value">78%</p><p class="metric-delta">▲ 3% (Matriz)</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    # Segunda Linha: Gráficos de Pizza e Barras (Ref. image_0.png)
    g1, g2 = st.columns([1, 2])

    with g1:
        st.markdown('<div class="card-axon"><h4>Tipos de Exames (ASO)</h4>', unsafe_allow_html=True)
        df_pizza = pd.DataFrame({
            "Tipo": ["Admissional", "Demissional", "Mudança Fun.", "Outros", "Periódico"],
            "Qtd": [45, 32, 12, 18, 222]
        })
        # Usando as cores da Axon (Teal e variantes)
        fig_pizza = px.pie(df_pizza, values='Qtd', names='Tipo', hole=.5, 
                           color_discrete_sequence=['#00838f', '#00acc1', '#4dd0e1', '#80deea', '#b2ebf2'])
        fig_pizza.update_layout(margin=dict(t=10, b=10, l=10, r=10), legend=dict(orientation="h", y=-0.1))
        st.plotly_chart(fig_pizza, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with g2:
        st.markdown('<div class="card-axon"><h4>Evolução de Exames Realizados / Mês</h4>', unsafe_allow_html=True)
        df_barras = pd.DataFrame({
            "Mês": ["Mai", "Jun", "Jul", "Ago", "Set", "Out"],
            "Realizados": [65, 78, 41, 55, 62, 85]
        })
        fig_barras = px.bar(df_barras, x='Mês', y='Realizados', 
                            color='Realizados', color_continuous_scale=['#b2ebf2', '#00838f'])
        fig_barras.update_layout(margin=dict(t=10, b=10, l=10, r=10), showlegend=False)
        fig_barras.update_coloraxes(showscale=False) # Remove a barra de cores
        st.plotly_chart(fig_barras, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 2. MATRIZ DE CONFORMIDADE (As 15 NRs) ---
elif menu == "🛡️ Matriz de Conformidade":
    st.markdown("## 🛡️ Matriz de Conformidade Legal (Índice NRs)")
    st.info("Acompanhamento técnico do percentual de adequação das 15 NRs prioritárias.")
    
    # Simulação expandida das NRs
    normas_data = {
        "NR-01 (PGR/Gestão)": 100, "NR-05 (CIPA)": 100, "NR-06 (EPI)": 90,
        "NR-07 (PCMSO)": 85, "NR-09 (Agentes A.)": 80, "NR-10 (Elétrica)": 70,
        "NR-11 (Transporte)": 60, "NR-12 (Máquinas)": 55, "NR-13 (Vasos P.)": 100,
        "NR-17 (Ergonomia)": 85, "NR-18 (Construção)": 100, "NR-23 (Incêndio)": 90,
        "NR-26 (Sinalização)": 75, "NR-33 (E. Confinado)": 100, "NR-35 (Altura)": 95
    }
    
    for nr, prog in normas_data.items():
        with st.container():
            col_n, col_p, col_s = st.columns([2, 5, 1])
            col_n.markdown(f"**{nr}**")
            col_p.progress(prog/100)
            
            if prog == 100:
                col_s.markdown('<span class="status-aprovado">✅ 100%</span>', unsafe_allow_html=True)
            elif prog >= 80:
                col_s.markdown('<span style="color:#f97316; font-weight:bold;">⚠️ {prog}%</span>'.format(prog=prog), unsafe_allow_html=True)
            else:
                col_s.markdown('<span class="status-alerta">❌ {prog}%</span>'.format(prog=prog), unsafe_allow_html=True)

# --- 3. ANÁLISE IA & VALIDAÇÃO DUPLA ---
elif menu == "🧠 Análise IA & Validação":
    st.markdown("## 🧠 Núcleo de Inteligência Híbrida")
    st.write("Análise automatizada por IA com validação final do Corpo Técnico Axon.")
    
    u1, u2 = st.columns([2, 1])
    with u1:
        st.markdown('<div class="card-axon">', unsafe_allow_html=True)
        st.subheader("🔍 Pré-Análise Digital (IA)")
        doc = st.file_uploader("Upload de Laudo ou Programa (PGR, LTCAT, NR-10)", type=['pdf', 'docx'])
        if doc:
            with st.spinner("IA Axon analisando estrutura técnica..."):
                st.markdown("---")
                st.markdown("**Resultado do Diagnóstco:**")
                st.success("✅ Estrutura básica da norma identificada.")
                st.error("❌ Falta de Análise de Risco (HRN) para a máquina 'Prensa 02' (Ref. NR-12).")
                st.warning("⚠️ CAs dos EPIs de eletricista vencem em 60 dias (Ref. NR-06/NR-10).")
        st.markdown('</div>', unsafe_allow_html=True)
            
    with u2:
        st.markdown('<div class="card-axon">', unsafe_allow_html=True)
        st.subheader("✍️ Validação Técnica")
        st.write("Status: **Aguardando Revisão Humana**")
        st.text_area("Notas e recomendações do Engenheiro/Técnico:")
        
        c_v1, c_v2 = st.columns(2)
        c_v1.checkbox("Aprovação Eng. Flávio", help="Eng. Eletricista e Segurança")
        c_v2.checkbox("Aprovação Sócia", help="Técnica de Segurança")
        
        st.button("✅ Publicar e Notificar Cliente", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 4. BIBLIOTECA DE MODELOS (As 15 NRs) ---
elif menu == "✍️ Biblioteca de Modelos (NRs)":
    st.markdown("## ✍️ Biblioteca de Modelos Técnicos Validados")
    st.info("Templates oficiais exigidos pela legislação, prontos para uso da equipe Axon.")
    
    # Mapeamento expandido de documentos por NR
    biblioteca = {
        "NR-01 (PGR/Gestão)": ["PGR Estruturado", "Inventário de Riscos BR", "Plano de Ação Dinâmico"],
        "NR-06 (EPI)": ["Ficha de Entrega Digital", "Termo de Responsabilidade"],
        "NR-07 (PCMSO)": ["Relatório Analítico Anual", "Modelo de ASO Digital"],
        "NR-10 (Elétrica)": ["Prontuário (PIE)", "Laudo de Aterramento/SPDA", "RTI - Relatório Técnico"],
        "NR-12 (Máquinas)": ["Inventário de Máquinas", "Análise de Risco (HRN)", "Plano de Manutenção"],
        "NR-17 (Ergonomia)": ["AET - Análise Ergonômica", "Avaliação Preliminar"],
        "NR-35 (Altura)": ["APR - Análise de Risco", "Plano de Resgate Técnico"]
    }
    
    c_nr, c_doc = st.columns(2)
    with c_nr:
        sel_nr = st.selectbox("Selecione a NR:", list(biblioteca.keys()))
    with c_doc:
        sel_doc = st.selectbox("Selecione o Modelo:", biblioteca[sel_nr])
        
    st.markdown("---")
    st.markdown(f"Modelo Selecionado: **{sel_doc}**")
    c_b1, c_b2, c_b3 = st.columns(3)
    c_b1.button(f"📥 Baixar Template Validado (.docx)", use_container_width=True)
    c_b2.markdown("**Padrão:** Corporativo Axon")
    c_b3.markdown("**Última Revisão:** Out/2023")

# --- 5. PORTAL DO CONTADOR (XML/eSocial) ---
elif menu == "📥 Portal do Contador (XML)":
    st.markdown("## 📥 Central de Integração eSocial (Contabilidade)")
    st.write("Gerencie e audite os envios de SST para evitar multas por divergência com a Folha.")
    
    aba_gerar, aba_auditar = st.tabs(["📦 Gerar Arquivos XML", "🤖 Auditoria SST-Folha"])
    
    with aba_gerar:
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.selectbox("Empresa Cliente:", ["Usina Delta S/A", "Indústria Taboado LTDA"])
            st.date_input("Mês de Referência", datetime.now())
        with col_g2:
            st.multiselect("Eventos Requeridos:", ["S-2210 (CAT)", "S-2220 (Saúde)", "S-2240 (Riscos)"])
            st.button("📦 Gerar e Validar Lote XML", use_container_width=True)

    with aba_auditar:
        st.subheader("Auditor de Convergência SST-Folha (IA)")
        st.write("Suba o XML da Folha de Pagamento (S-1200) para cruzar com o laudo Axon.")
        upl_folha = st.file_uploader("Upload XML da Folha", type=['xml'])
        if upl_folha:
            st.error("⚠️ Divergência Detectada: Colaborador 'Adryan Mikaue' exposto a Risco Elétrico (NR-10) no laudo Axon, mas XML da contabilidade não contém tributação de aposentadoria especial correspondente.")
            st.button("Enviar Alerta Corretivo para o Contador")

# --- 6. AXON ACADEMY (EAD/Treinamentos) ---
elif menu == "🎓 Axon Academy (EAD)":
    st.markdown("## 🎓 Axon Academy - Portal de Treinamento EAD")
    aba_aluno, aba_certificado = st.tabs(["👤 Portal do Aluno", "📜 Emissão de Certificados"])
    
    with aba_aluno:
        st.markdown("### Treinamento Ativo: NR-10 Básico")
        c_vid, c_prog = st.columns([2, 1])
        with c_vid:
            # Vídeo simulado de treinamento técnico
            st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 
            st.caption("Módulo 2: Riscos em Instalações Elétricas")
        with c_prog:
            st.write("**Seu Progresso:**")
            st.progress(85)
            st.write("Nota Prova Parcial: **9.0**")
            if st.button("Iniciar Avaliação Final"):
                st.success("Prova liberada. Boa sorte!")

    with aba_certificado:
        st.subheader("Certificados Disponíveis")
        st.write("Colaborador: **ADRYAN MIKAUE**")
        st.markdown("---")
        
        # Simulação visual do Certificado (Conforme regras de títulos)
        st.markdown(f"""
            <div style="border: 8px double #00838f; padding: 30px; text-align: center; background-color: white; color: #424242; font-family: 'Times New Roman', serif;">
                <h1 style="color: #00838f; margin-bottom: 5px;">CERTIFICADO DE PROFICIÊNCIA TÉCNICA</h1>
                <p style="font-size: 16px; margin-top: 0;">Treinamento Normativo - NR-10 Básico</p>
                
                <p style="font-size: 18px; margin-top: 25px;">Certificamos que o colaborador(a)</p>
                <h2 style="text-transform: uppercase; font-size: 26px; border-bottom: 1px solid #00838f; display: inline-block; padding: 0 15px;">ADRYAN MIKAUE</h2>
                
                <p style="font-size: 18px;">concluiu com aproveitamento de <b>98%</b> o treinamento de:</p>
                <h3 style="background-color: #f1f5f9; padding: 8px; border-radius: 5px; color: #00838f;">SEGURANÇA EM INSTALAÇÕES E SERVIÇOS COM ELETRICIDADE</h3>
                
                <p style="font-size: 16px;">Carga Horária: 08 Horas | Realizado em: 10/10/2023</p>
                
                <div style="margin-top: 40px; display: flex; justify-content: space-around; align-items: flex-end;">
                    <!-- Assinatura Flávio -->
                    <div style="width: 45%;">
                        <hr style="border: 0; border-top: 1px solid black; margin-bottom: 5px;">
                        <p style="font-size: 11px; line-height: 1.3; margin:0;">
                            <b>FLÁVIO FILHO MARTINS REIS</b><br>
                            Engenheiro Eletricista<br>
                            Engenheiro de Segurança do Trabalho<br>
                            CREA: SP-[SEU REGISTRO]
                        </p>
                    </div>
                    <!-- Assinatura Sócia -->
                    <div style="width: 45%;">
                        <hr style="border: 0; border-top: 1px solid black; margin-bottom: 5px;">
                        <p style="font-size: 11px; line-height: 1.3; margin:0;">
                            <b>[NOME DA SÓCIA]</b><br>
                            Técnica de Segurança do Trabalho<br>
                            MTE: [REGISTRO MTE]
                        </p>
                    </div>
                </div>
                
                <div style="margin-top: 30px; font-size: 9px; color: #64748b; text-align: center;">
                    Autenticidade verificável via QR-Code Axon ID: AXN-EAD-2023-10-10-AM<br>
                    Certificado gerado em {datetime.now().strftime('%d/%m/%Y %H:%M')}
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button("📥 Baixar Certificado Oficial (PDF)")

# --- 7. PROPOSTA COMERCIAL & CRM ---
elif menu == "📄 Proposta Comercial Inteligente":
    st.markdown("## 📄 Gestão Comercial e CRM Axon")
    aba_nova, aba_crm = st.tabs(["🆕 Nova Proposta (IA Vendas)", "📜 Histórico de Propostas (CRM)"])
    
    with aba_nova:
        st.markdown("### Gerador de Proposta de Impacto (Risco Financeiro)")
        with st.form("form_proposta"):
            col_p1, col_p2 = st.columns(2)
            with col_p1:
                p_cliente = st.text_input("Razão Social do Prospect")
                p_func = st.number_input("Nº de Funcionários", min_value=1, value=10)
                p_contato = st.text_input("WhatsApp do Decisor")
            with col_p2:
                p_nrs = st.multiselect("NRs para Adequação:", ["NR-01", "NR-10", "NR-12", "NR-17", "NR-35"])
                p_investimento = st.number_input("Valor da Proposta Axon (R$)", format="%.2f")

            if st.form_submit_button("📊 Calcular Risco e Salvar Proposta"):
                # Lógica de cálculo de risco financeiro (NR-28 simulada)
                multa_estimada = len(p_nrs) * p_func * 165.00
                st.session_state.historico_propostas.append({
                    "Data": datetime.now().strftime("%d/%m/%Y"),
                    "Cliente": p_cliente,
                    "Risco": multa_estimada,
                    "Investimento": p_investimento,
                    "Status": "Enviado"
                })
                
                st.markdown("---")
                st.markdown(f'<div class="card-axon">', unsafe_allow_html=True)
                st.subheader(f"📊 Diagnóstico de Risco: {p_cliente}")
                st.metric("Multa Potencial Estimada (NR-28)", f"R$ {multa_estimada:,.2f}", delta="Alto Risco", delta_color="inverse")
                st.write(f"Argumento de Venda: *\"Seu investimento de R$ {p_investimento:,.2f} protege sua empresa de uma perda de R$ {multa_estimada:,.2f}.\"*")
                st.button(f"📥 Baixar PDF Proposta para {p_cliente}")
                st.markdown('</div>', unsafe_allow_html=True)
    
    with aba_crm:
        st.markdown("### Pipeline de Vendas")
        if st.session_state.historico_propostas:
            df_crm = pd.DataFrame(st.session_state.historico_propostas)
            # Formatação de valores monetários
            df_crm["Risco"] = df_crm["Risco"].map("R$ {:,.2f}".format)
            df_crm["Investimento"] = df_crm["Investimento"].map("R$ {:,.2f}".format)
            st.dataframe(df_crm, use_container_width=True)
        else:
            st.info("Nenhuma proposta gerada.")

# --- RODAPÉ INSTITUCIONAL ---
st.markdown("---")
st.markdown(f"""
    <p style='text-align:center; color:#424242; font-size:12px;'>
        <b>Axon Consultoria e Engenharia</b> | Inteligência em Engenharia Elétrica e Segurança do Trabalho<br>
        Santa Fé do Sul - SP | Aparecida do Taboado - MS | © {datetime.now().year}
    </p>
""", unsafe_allow_html=True)
