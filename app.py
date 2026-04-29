import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from fpdf import FPDF
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Axon Consultoria e Engenharia", page_icon="🛡️")

# --- CLASSE PARA GERAR PDF (VERSÃO MELHORADA) ---
class PDF(FPDF):
    def header(self):
        # Título Principal
        self.set_font('Helvetica', 'B', 16)
        self.set_text_color(15, 23, 42) # Azul Escuro Axon
        self.cell(0, 10, 'AXON CONSULTORIA E ENGENHARIA', 0, 1, 'C')
        self.set_font('Helvetica', 'B', 10)
        self.cell(0, 5, 'SISTEMA INTEGRADO DE GESTÃO OPERACIONAL E SEGURANÇA', 0, 1, 'C')
        self.ln(10)
        # Linha verde decorativa
        self.set_draw_color(5, 150, 105) # Verde Axon
        self.set_line_width(1)
        self.line(10, 32, 200, 32)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(100)
        self.cell(0, 10, f'Página {self.page_no()} | RT: Eng. Flávio Filho Martins Reis', 0, 0, 'C')

# --- ESTILIZAÇÃO CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@300;400;600;700&display=swap');
    .stApp { background-color: #f8fafc; font-family: 'Segoe UI', sans-serif; }
    .header-axon { background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border-bottom: 4px solid #059669; margin-bottom: 2rem; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .card-nr { background-color: #ffffff; padding: 1.5rem; border-radius: 8px; border: 1px solid #e2e8f0; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO LATERAL ---
with st.sidebar:
    st.markdown("### AXON")
    st.markdown("---")
    opcao = st.radio("MENU DE GESTÃO", ["Painel Operacional", "Auditoria 15 NRs"])
    st.markdown("---")
    st.caption("Engenheiro Responsável:")
    st.markdown("**Flávio Filho Martins Reis**")

# --- CABEÇALHO ---
st.markdown(f"""<div class="header-axon"><h1 style='margin:0; font-size: 1.8rem; color:#0f172a;'>AXON CONSULTORIA E ENGENHARIA</h1><p style='margin:0; color:#059669; font-weight:600;'>{opcao.upper()}</p></div>""", unsafe_allow_html=True)

if opcao == "Auditoria 15 NRs":
    nrs = {
        "NR-01 - GRO/PGR": ["Inventário de riscos detalhado?", "Plano de ação com prazos e responsáveis?", "Procedimentos de emergência?", "Análise de acidentes?"],
        "NR-10 - Elétrica": ["Prontuário (PIE) atualizado?", "Esquemas unifilares assinados?", "Ensaios dielétricos?", "LOTO ativo?", "Sinalização de impedimento?"],
        "NR-12 - Máquinas": ["Inventário de máquinas?", "Proteções intertravadas?", "Botões de emergência monitorados?", "Manual em português?"],
        "NR-17 - Ergonomia": ["Análise Ergonômica (AET)?", "Adequação de postos?", "Treinamento de levantamento de peso?", "Organização de pausas?"],
        "NR-35 - Altura": ["Análise de Risco (AR)?", "Projeto de linha de vida?", "Inspeção de EPIs?", "ASO apto para altura?"]
    }

    c1, c2 = st.columns(2)
    with c1: cliente = st.text_input("NOME DO CLIENTE / UNIDADE", "Ex: Usina Delta")
    with c2: nr_sel = st.selectbox("NORMA AUDITADA", list(nrs.keys()))
    
    st.markdown('<div class="card-nr">', unsafe_allow_html=True)
    itens = nrs[nr_sel]
    respostas = []
    
    st.write(f"### Checklist: {nr_sel}")
    for item in itens:
        respostas.append(st.checkbox(item))
            
    pontos = sum(respostas)
    conformidade = (pontos / len(itens)) * 100
    st.metric("Conformidade Técnica", f"{conformidade:.1f}%")
    st.progress(conformidade / 100)

    if st.button("GERAR LAUDO TÉCNICO PDF"):
        # Usando 'latin-1' para compatibilidade de acentos no FPDF sem fontes externas
        pdf = PDF()
        pdf.add_page()
        
        # Informações Gerais
        pdf.set_font('Helvetica', 'B', 12)
        pdf.cell(0, 10, f'LAUDO TÉCNICO DE CONFORMIDADE: {nr_sel}', 0, 1)
        pdf.set_font('Helvetica', '', 10)
        pdf.cell(0, 7, f'Cliente: {cliente}', 0, 1)
        pdf.cell(0, 7, f'Data da Auditoria: {datetime.now().strftime("%d/%m/%Y")}', 0, 1)
        pdf.ln(5)
        
        # Tabela de Itens
        pdf.set_fill_color(241, 245, 249)
        pdf.set_font('Helvetica', 'B', 10)
        pdf.cell(150, 10, ' Item Auditado', 1, 0, 'L', True)
        pdf.cell(40, 10, ' Status', 1, 1, 'C', True)
        
        pdf.set_font('Helvetica', '', 9)
        for idx, item in enumerate(itens):
            status = "CONFORME" if respostas[idx] else "NAO CONFORME"
            # Tratamento de acentos manual para evitar erro de encoding no PDF
            item_pdf = item.replace('ã','a').replace('õ','o').replace('ç','c').replace('é','e').replace('ê','e').replace('í','i')
            
            pdf.cell(150, 8, f' {item_pdf}', 1)
            if status == "CONFORME":
                pdf.set_text_color(5, 150, 105)
            else:
                pdf.set_text_color(220, 38, 38)
            pdf.cell(40, 8, f' {status}', 1, 1, 'C')
            pdf.set_text_color(0)

        pdf.ln(10)
        pdf.set_font('Helvetica', 'B', 11)
        pdf.cell(0, 10, f'INDICE FINAL DE ADEQUACAO: {conformidade:.1f}%', 0, 1)
        
        # Rodapé de Assinatura
        pdf.ln(20)
        pdf.line(60, pdf.get_y(), 150, pdf.get_y())
        pdf.cell(0, 10, 'Eng. Flavio Filho Martins Reis', 0, 1, 'C')
        pdf.set_font('Helvetica', 'I', 8)
        pdf.cell(0, 5, 'Responsavel Tecnico - AXON', 0, 1, 'C')

        pdf_output = pdf.output(dest='S').encode('latin-1', errors='replace')
        st.download_button(
            label="⬇️ BAIXAR LAUDO OFICIAL (PDF)",
            data=pdf_output,
            file_name=f"Laudo_Axon_{cliente}_{nr_sel.split(' ')[0]}.pdf",
            mime="application/pdf"
        )
    st.markdown('</div>', unsafe_allow_html=True)

elif opcao == "Painel Operacional":
    st.info("Acesse 'Auditoria 15 NRs' para gerar documentos.")
