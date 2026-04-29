    import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from fpdf import FPDF
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Axon Consultoria e Engenharia", page_icon="🛡️")

# --- CLASSE PARA GERAR PDF ---
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'AXON CONSULTORIA E ENGENHARIA - RELATÓRIO TÉCNICO', 0, 1, 'C')
        self.set_font('Arial', '', 8)
        self.cell(0, 5, f'Gerado em: {datetime.now().strftime("%d/%m/%Y %H:%M")}', 0, 1, 'R')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

# --- ESTILIZAÇÃO CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@300;400;600;700&display=swap');
    .stApp { background-color: #f8fafc; font-family: 'Segoe UI', sans-serif; color: #1e293b; }
    [data-testid="stSidebar"] { background-color: #0f172a; }
    [data-testid="stSidebar"] * { color: white !important; }
    .header-axon { background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border-bottom: 4px solid #059669; margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .card-nr { background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 1rem; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    st.markdown("### AXON")
    st.markdown("<p style='font-size:0.85rem; opacity:0.8;'>Consultoria e Engenharia</p>", unsafe_allow_html=True)
    st.markdown("---")
    opcao = st.radio("MENU DE GESTÃO", ["Painel Operacional", "Auditoria 15 NRs"])
    st.markdown("---")
    st.caption("Engenheiro Responsável:")
    st.markdown("**Flávio Filho Martins Reis**")

# --- CABEÇALHO ---
st.markdown(f"""<div class="header-axon"><h1 style='margin:0; font-size: 1.8rem;'>AXON <span style='font-weight:300;'>CONSULTORIA E ENGENHARIA</span></h1><p style='margin:0; color:#059669; font-weight:600;'>{opcao.upper()}</p></div>""", unsafe_allow_html=True)

if opcao == "Auditoria 15 NRs":
    nrs = {
        "NR-01 - GRO/PGR": ["Inventário de riscos detalhado?", "Plano de ação com prazos e responsáveis?", "Procedimentos de emergência escritos?", "Análise de acidentes e doenças do trabalho?"],
        "NR-05 - CIPA": ["Processo eleitoral protocolado no Sindicato?", "Treinamento de cipeiros atualizado?", "Atas de reuniões mensais disponíveis?", "Designado de CIPA nomeado (se aplicável)?"],
        "NR-06 - EPI": ["Ficha de entrega com CA e data?", "Higienização e guarda adequadas?", "Treinamento de uso e conservação?", "Substituição imediata de itens danificados?"],
        "NR-07 - PCMSO": ["ASO com indicação de aptidão específica?", "Cronograma de exames complementares?", "Relatório analítico anual assinado?", "Primeiros socorros (caixa e treinamento)?"],
        "NR-09 - Riscos Ambientais": ["Monitoramento de ruído/calor atualizado?", "Metodologia de amostragem certificada?", "Medidas de controle para riscos químicos?", "Registros históricos mantidos?"],
        "NR-10 - Elétrica": ["Prontuário (PIE) com RTI atualizado?", "Esquemas unifilares assinados por Eng. Eletricista?", "Ensaios dielétricos de luvas/ferramentas?", "LOTO (Bloqueio e Etiquetagem) ativo?", "Sinalização de impedimento em quadros?"],
        "NR-12 - Máquinas": ["Inventário com classificação de risco (SIL/PL)?", "Proteções fixas/móveis intertravadas?", "Botões de emergência monitorados por relé?", "Manual em português disponível?", "Distâncias de segurança (NBR 13857)?"],
        "NR-13 - Pressão": ["Livro de registro de segurança?", "Placa de identificação legível?", "Relatório de inspeção interna/externa?", "Teste de estanqueidade e calibração de válvulas?"],
        "NR-15 - Insalubridade": ["Laudo de Insalubridade assinado por Eng/Médico?", "Medições de agentes físicos/químicos?", "Comprovação de entrega de EPIs específicos?", "Pagamento de adicional conforme grau?"],
        "NR-16 - Periculosidade": ["Laudo de periculosidade (Elétrica/Inflamáveis)?", "Delimitação de áreas de risco?", "Controle de acesso a áreas perigosas?", "Anotação de Responsabilidade Técnica (ART)?"],
        "NR-17 - Ergonomia": ["Análise Ergonômica do Trabalho (AET)?", "Adequação de postos de trabalho (cadeiras/mesas)?", "Treinamento de levantamento de peso?", "Organização de pausas e ritmos?"],
        "NR-18 - Construção": ["PCMAT/PGR da obra atualizado?", "Áreas de vivência (refeitório/sanitário) adequadas?", "Proteção periférica contra quedas?", "Aterramento temporário de canteiro?"],
        "NR-23 - Incêndio": ["Auto de Vistoria do Corpo de Bombeiros (AVCB)?", "Extintores com carga e inspeção em dia?", "Sinalização de rotas de fuga fotoluminescente?", "Treinamento de brigada de incêndio?"],
        "NR-33 - Confinado": ["PET (Permissão de Entrada e Trabalho)?", "Monitor de gases calibrado?", "Vigia capacitado na entrada?", "Sistema de resgate e ventilação montado?"],
        "NR-35 - Altura": ["Análise de Risco (AR) e Permissão de Trabalho (PT)?", "Projeto e cálculo de linha de vida/ancoragem?", "Inspeção trimestral de cintos e trava-quedas?", "ASO com aptidão específica para altura?"]
    }

    cliente = st.text_input("NOME DO CLIENTE / UNIDADE VISITADA", "Ex: Usina Delta")
    nr_sel = st.selectbox("Selecione a Norma Regulamentadora para Auditoria:", list(nrs.keys()))
    
    st.markdown('<div class="card-nr">', unsafe_allow_html=True)
    itens = nrs[nr_sel]
    respostas = []
    
    for item in itens:
        respostas.append(st.checkbox(item))
            
    pontos = sum(respostas)
    conformidade = (pontos / len(itens)) * 100
    st.metric("Nível de Adequação Técnica", f"{conformidade:.1f}%")
    st.progress(conformidade / 100)

    # --- LÓGICA DE GERAÇÃO DO PDF ---
    if st.button("GERAR E BAIXAR RELATÓRIO PDF"):
        pdf = PDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(0, 10, f'Relatório de Auditoria: {nr_sel}', 0, 1)
        pdf.set_font('Arial', '', 12)
        pdf.cell(0, 10, f'Cliente: {cliente}', 0, 1)
        pdf.cell(0, 10, f'Responsável Técnico: Eng. Flávio Filho Martins Reis', 0, 1)
        pdf.ln(5)
        
        pdf.set_font('Arial', 'B', 11)
        pdf.cell(0, 10, 'Itens Auditados:', 0, 1)
        pdf.set_font('Arial', '', 10)
        
        for idx, item in enumerate(itens):
            status = "[OK]" if respostas[idx] else "[PENDENTE]"
            pdf.multi_cell(0, 8, f'{status} {item}')
        
        pdf.ln(5)
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(0, 10, f'Índice Final de Conformidade: {conformidade:.1f}%', 0, 1)
        
        # Salva o PDF em memória para o Streamlit
        pdf_output = pdf.output(dest='S').encode('latin-1')
        st.download_button(
            label="Clique aqui para baixar o PDF",
            data=pdf_output,
            file_name=f"Relatorio_{nr_sel.split(' ')[0]}_{cliente}.pdf",
            mime="application/pdf"
        )
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Painel Operacional":
    st.info("Utilize o módulo de Auditoria para gerar relatórios técnicos.")

# --- RODAPÉ ---
st.markdown("---")
st.markdown("<p style='text-align:center; color:#64748b; font-size:0.8rem;'>Axon Consultoria e Engenharia</p>", unsafe_allow_html=True)
