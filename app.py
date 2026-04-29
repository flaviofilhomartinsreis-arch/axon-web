import streamlit as st
import pandas as pd
from fpdf import FPDF
from datetime import datetime

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(layout="wide", page_title="Axon Consultoria e Engenharia", page_icon="🛡️")

# --- CLASSE PDF PROFISSIONAL ---
class AxonPDF(FPDF):
    def header(self):
        # Logo ou Nome da Empresa
        self.set_font('Helvetica', 'B', 15)
        self.set_text_color(15, 23, 42)
        self.cell(0, 10, 'AXON CONSULTORIA E ENGENHARIA', 0, 1, 'L')
        self.set_font('Helvetica', '', 9)
        self.set_text_color(100)
        self.cell(0, 5, 'Soluções Integradas em Segurança do Trabalho e Engenharia Elétrica', 0, 1, 'L')
        self.ln(5)
        # Linha de separação
        self.set_draw_color(5, 150, 105)
        self.set_line_width(0.8)
        self.line(10, 28, 200, 28)
        self.ln(10)

    def footer(self):
        self.set_y(-20)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128)
        self.set_draw_color(200)
        self.line(10, 275, 200, 275)
        self.cell(0, 10, f'Relatório Gerado via Sistema SIGOS - Página {self.page_no()}', 0, 0, 'L')
        self.cell(0, 10, f'Emitido em: {datetime.now().strftime("%d/%m/%Y")}', 0, 0, 'R')

# --- ESTILO STREAMLIT ---
st.markdown("""
    <style>
    .stApp { background-color: #f1f5f9; }
    .main-card { background-color: white; padding: 2rem; border-radius: 12px; shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1063/1063302.png", width=80) # Ícone genérico de engenharia
    st.title("Painel Axon")
    menu = st.radio("Navegação", ["Auditoria de NRs", "Configurações"])

if menu == "Auditoria de NRs":
    st.markdown('<div class="main-card">', unsafe_allow_html=True)
    st.title("📝 Emissão de Laudo de Conformidade")
    
    col1, col2 = st.columns(2)
    with col1:
        cliente = st.text_input("Empresa/Cliente", placeholder="Ex: Deluz Energia")
        unidade = st.text_input("Unidade/Planta", placeholder="Ex: Subestação Norte")
    with col2:
        nr_lista = {
            "NR-10 (Elétrica)": ["Prontuário das Instalações Elétricas (PIE)", "Esquemas Unifilares Atualizados", "Laudo de Aterramento e SPDA", "Treinamento Básico/SEP", "Equipamentos de Proteção (EPI/EPC)"],
            "NR-12 (Máquinas)": ["Inventário de Máquinas e Equipamentos", "Análise de Risco por Máquina", "Sistemas de Segurança/Intertravamento", "Manuais de Operação em Português"],
            "NR-35 (Altura)": ["Análise de Risco (AR)", "Permissão de Trabalho (PT)", "Pontos de Ancoragem Projetados", "Certificação de Treinamento", "Inspeção de Equipamentos (Cintos/Cordas)"]
        }
        nr_sel = st.selectbox("Selecione a Norma", list(nr_lista.keys()))

    st.divider()
    
    st.subheader("Checklist de Verificação")
    itens = nr_lista[nr_sel]
    checks = []
    
    # Criando checklist em duas colunas para o formulário
    c_check1, c_check2 = st.columns(2)
    for i, item in enumerate(itens):
        if i % 2 == 0:
            checks.append(c_check1.checkbox(item, key=f"ch_{i}"))
        else:
            checks.append(c_check2.checkbox(item, key=f"ch_{i}"))

    if st.button("🚀 GERAR RELATÓRIO PROFISSIONAL"):
        pdf = AxonPDF()
        pdf.add_page()
        
        # Resumo Executivo
        pdf.set_font('Helvetica', 'B', 12)
        pdf.set_fill_color(240, 240, 240)
        pdf.cell(0, 10, f'LAUDO TÉCNICO: {nr_sel.upper()}', 0, 1, 'L', True)
        pdf.ln(2)
        
        pdf.set_font('Helvetica', '', 10)
        pdf.cell(40, 7, 'Cliente:', 0, 0); pdf.set_font('Helvetica', 'B', 10); pdf.cell(0, 7, cliente.upper(), 0, 1)
        pdf.set_font('Helvetica', '', 10)
        pdf.cell(40, 7, 'Unidade:', 0, 0); pdf.set_font('Helvetica', 'B', 10); pdf.cell(0, 7, unidade.upper(), 0, 1)
        pdf.set_font('Helvetica', '', 10)
        pdf.cell(40, 7, 'Status Geral:', 0, 0)
        
        conf = (sum(checks)/len(itens))*100
        pdf.set_font('Helvetica', 'B', 10)
        color = (5, 150, 105) if conf == 100 else (220, 38, 38)
        pdf.set_text_color(*color)
        pdf.cell(0, 7, f'{conf:.1f}% DE CONFORMIDADE', 0, 1)
        pdf.set_text_color(0)
        pdf.ln(10)

        # Cabeçalho da Tabela
        pdf.set_fill_color(15, 23, 42)
        pdf.set_text_color(255)
        pdf.set_font('Helvetica', 'B', 10)
        pdf.cell(140, 10, ' ITEM DE AUDITORIA', 1, 0, 'L', True)
        pdf.cell(50, 10, ' STATUS TÉCNICO', 1, 1, 'C', True)

        # Itens da Tabela
        pdf.set_text_color(0)
        pdf.set_font('Helvetica', '', 9)
        for i, item in enumerate(itens):
            status = "CONFORME" if checks[i] else "NÃO CONFORME"
            bg = True if i % 2 == 0 else False
            pdf.set_fill_color(245, 247, 250)
            
            # Limpar caracteres especiais para evitar erro no PDF padrão
            txt = item.encode('latin-1', 'replace').decode('latin-1')
            
            pdf.cell(140, 9, f' {txt}', 1, 0, 'L', bg)
            if not checks[i]: pdf.set_text_color(200, 0, 0)
            pdf.cell(50, 9, status, 1, 1, 'C', bg)
            pdf.set_text_color(0)

        # Assinatura
        pdf.ln(30)
        pdf.line(65, pdf.get_y(), 145, pdf.get_y())
        pdf.set_font('Helvetica', 'B', 10)
        pdf.cell(0, 7, 'Eng. Flávio Filho Martins Reis', 0, 1, 'C')
        pdf.set_font('Helvetica', '', 8)
        pdf.cell(0, 5, 'Responsável Técnico - CREA/TO', 0, 1, 'C')

        # Download
        pdf_out = pdf.output(dest='S').encode('latin-1')
        st.download_button(
            label="⬇️ Baixar Laudo Oficial (PDF)",
            data=pdf_out,
            file_name=f"LAUDO_AXON_{cliente.replace(' ','_')}.pdf",
            mime="application/pdf"
        )
    st.markdown('</div>', unsafe_allow_html=True)
