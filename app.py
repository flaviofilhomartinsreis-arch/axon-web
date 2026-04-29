import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    layout="wide", 
    page_title="Axon Consultoria e Engenharia", 
    page_icon="🛡️"
)

# --- ESTILIZAÇÃO CSS (VISUAL CORPORATIVO DE ALTO PADRÃO) ---
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
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Cabeçalho de Autoridade */
    .header-axon {
        background-color: #ffffff;
        padding: 1.5rem 2rem;
        border-radius: 8px;
        border-bottom: 4px solid #059669; /* Verde Esmeralda */
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
    }

    /* Cartões de Indicadores */
    .card-metrica {
        background-color: #ffffff;
        padding: 1.2rem;
        border-radius: 6px;
        border: 1px solid #e2e8f0;
        text-align: left;
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    .titulo-metrica {
        color: #64748b;
        font-size: 0.8rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
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
        padding: 0.6rem 1.5rem;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #047857;
        box-shadow: 0 4px 12px rgba(5, 150, 105, 0.2);
    }

    /* Tabelas */
    div[data-testid="stTable"] {
        background-color: white;
        border-radius: 4px;
        border: 1px solid #e2e8f0;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    st.markdown("### AXON")
    st.markdown("<p style='font-size:0.85rem; opacity:0.8;'>Consultoria e Engenharia</p>", unsafe_allow_html=True)
    st.markdown("---")
    opcao = st.radio(
        "MENU DE GESTÃO",
        ["Painel Operacional", "Análise de Risco Humano", "Auditoria (15 NRs)"]
    )
    st.markdown("---")
    st.caption("Engenheiro Responsável:")
    st.markdown("**Flávio Filho Martins Reis**")
    st.markdown("---")
    st.caption("Sistema SIGOS v1.2.5")

# --- CABEÇALHO PRINCIPAL ---
st.markdown(f"""
    <div class="header-axon">
        <h1 style='margin:0; color:#0f172a; font-size: 1.8rem; letter-spacing: -0.5px;'>
            AXON <span style='font-weight:300;'>CONSULTORIA E ENGENHARIA</span>
        </h1>
        <p style='margin:0; color:#059669; font-weight: 600; font-size: 0.9rem; text-transform: uppercase;'>
            {opcao} | Sistema Integrado de Gestão e Segurança
        </p>
    </div>
    """, unsafe_allow_html=True)

# --- CONTEÚDO POR MÓDULO ---

if opcao == "Painel Operacional":
    col1, col2, col3, col4 = st.columns(4)
    
    metricas = [
        ("Equipamentos Ativos", "142"),
        ("HHT Sem Acidentes", "4.210"),
        ("Alertas Pendentes", "02"),
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
    c_esq, c_dir = st.columns([2, 1])

    with c_esq:
        st.markdown("### 📋 Status da Equipe em Campo")
        dados_equipe = {
            "Colaborador": ["Adriano Silva", "Carlos Oliveira", "Mariana Santos", "João Pedro"],
            "Especialidade": ["Téc. de Redes", "Eletricista SEP", "Sup. SST", "Eng. de Campo"],
            "Risco": ["Baixo", "Médio", "Baixo", "Crítico"],
            "Status": ["Em Operação", "Em Pausa", "Em Operação", "Alerta de Fadiga"]
        }
        st.table(pd.DataFrame(dados_equipe))

    with c_dir:
        st.markdown("### 📊 Disponibilidade")
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
            height=280,
            paper_bgcolor='rgba(0,0,0,0)'
        )
        st.plotly_chart(fig, use_container_width=True)

elif opcao == "Análise de Risco Humano":
    st.subheader("🔥 Monitoramento Preditivo de Fadiga")
    st.info("Este módulo analisa a jornada acumulada para prevenir erros humanos em operações críticas.")
    st.warning("Dados sendo processados conforme logs de jornada (NR-10 / SEP).")

elif opcao == "Auditoria (15 NRs)":
    st.markdown("### 🔍 Diagnóstico de Conformidade Normativa")
    
    lista_nrs = [
        "NR-01 - Gerenciamento de Riscos Ocupacionais (GRO)", "NR-05 - CIPA", "NR-06 - EPI", 
        "NR-07 - PCMSO", "NR-09 - Avaliação e Controle de Exposições", 
        "NR-10 - Segurança em Instalações e Serviços em Eletricidade", 
        "NR-12 - Segurança em Máquinas e Equipamentos", "NR-13 - Caldeiras e Vasos", 
        "NR-15 - Atividades Insalubres", "NR-16 - Atividades Perigosas", 
        "NR-17 - Ergonomia", "NR-18 - Indústria da Construção",
        "NR-23 - Proteção Contra Incêndios", "NR-33 - Espaços Confinados", "NR-35 - Trabalho em Altura"
    ]
    
    nr_selecionada = st.selectbox("Selecione a NR para auditoria:", lista_nrs)
    
    st.markdown('<div class="card-metrica">', unsafe_allow_html=True)
    st.subheader(f"Avaliação Técnica: {nr_selecionada}")
    
    if "NR-10" in nr_selecionada:
        st.write("**Itens Críticos de Verificação (Carro-chefe Axon):**")
        col_a, col_b = st.columns(2)
        with col_a:
            q1 = st.checkbox("Prontuário de Instalações Elétricas (PIE) organizado?")
            q2 = st.checkbox("Esquemas Unifilares atualizados e assinados?")
            q3 = st.checkbox("Laudo de Inspeção do SPDA válido?")
        with col_b:
            q4 = st.checkbox("Certificações de treinamento (Básico/SEP) válidas?")
            q5 = st.checkbox("Procedimentos de LOTO (Bloqueio e Etiquetagem) ativos?")
            
        conformidade = sum([q1, q2, q3, q4, q5]) / 5
        st.markdown("---")
        st.write(f"**Índice de Adequação:** {conformidade*100:.0f}%")
        st.progress(conformidade)
        
        if st.button("GERAR RELATÓRIO DE AUDITORIA NR-10"):
            st.success("Relatório gerado com sucesso para exportação.")
    else:
        st.info(f"O checklist detalhado para a {nr_selecionada.split(' - ')[0]} está sendo integrado ao SIGOS.")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- RODAPÉ TÉCNICO ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
col_f1, col_f2 = st.columns([3, 1])

with col_f1:
    st.markdown("""
        <p style='color: #64748b; font-size: 0.8rem;'>
            &copy; 2024 <b>Axon Consultoria e Engenharia</b>. Todos os direitos reservados.<br>
            Responsabilidade Técnica: <b>Eng. Flávio Filho Martins Reis</b>
        </p>
    """, unsafe_allow_html=True)

with col_f2:
    st.markdown("""
        <p style='text-align: right; color: #64748b; font-size: 0.8rem;'>
            Ambiente Seguro 🛡️<br>
            <b>SIGOS v1.2.5-STABLE</b>
        </p>
    """, unsafe_allow_html=True)
