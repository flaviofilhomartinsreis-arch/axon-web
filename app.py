# --- MÓDULO: GESTÃO DE PROFISSIONAIS (ESTILO DATA LIFE) ---
elif opcao == "Painel Operacional":
    st.markdown('<div class="header-axon">', unsafe_allow_html=True)
    col_t1, col_t2 = st.columns([3, 1])
    with col_t1:
        st.subheader("Relatório de Profissionais")
    with col_t2:
        if st.button("➕ Cadastrar profissional"):
            st.info("Funcionalidade de cadastro em desenvolvimento.")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- BARRA DE FILTROS DE STATUS ---
    status_opcoes = ["Todos", "Habilitados", "Em análise", "Reprovados", "Rascunhos", "Desmobilizados"]
    tabs = st.tabs(status_opcoes) # Simula os botões superiores do modelo
    
    # --- FILTROS DE PESQUISA ---
    with st.expander("🔍 Filtros de Busca", expanded=True):
        c1, c2, c3, c4 = st.columns(4)
        with c1: st.selectbox("Tipo de atuação/Polo", ["Todos", "Argo 6", "Argo 8", "Argo 9"])
        with c2: st.selectbox("SubContratadas", ["Todas", "DELUZ PRESTADORA", "Outras"])
        with c3: st.selectbox("Unidade operacional", ["Todas", "Norte", "Sul"])
        with c4: st.text_input("Pesquisa de profissional", placeholder="Nome do colaborador...")

    # --- DADOS EXEMPLO (SIMULANDO A TABELA DA IMAGEM) ---
    dados_profissionais = [
        {"Profissional": "ADAM BRUNO SILVA SANTOS", "Cargo": "Encarregado de Equipe", "Polo": "Argo 8", "Status": "Desmobilizado", "Data": "15/12/2025"},
        {"Profissional": "ADRYAN MIKAUE ALMEIDA FERNANDES", "Cargo": "Operador de Moto Serra", "Polo": "Argo 8", "Status": "Desmobilizado", "Data": "15/12/2025"},
        {"Profissional": "ALISSON FILGUEIRA DA SILVA", "Cargo": "Operador de Moto Serra", "Polo": "Argo 8", "Status": "Desmobilizado", "Data": "15/12/2025"},
        {"Profissional": "ANTONIO AUGUSTO MENDES VIEIRA", "Cargo": "Encarregado de Equipe", "Polo": "Argo 8", "Status": "Rascunhos", "Data": "16/09/2025"},
    ]

    # --- RENDERIZAÇÃO DA TABELA ESTILIZADA ---
    st.markdown("""
        <style>
        .tabela-header { background-color: #f8fafc; font-weight: bold; padding: 10px; border-bottom: 2px solid #e2e8f0; }
        .tabela-linha { padding: 12px 10px; border-bottom: 1px solid #f1f5f9; transition: 0.3s; }
        .tabela-linha:hover { background-color: #f1f5f9; }
        .status-badge { padding: 4px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: 600; }
        .status-desmobilizado { color: #64748b; background-color: #f1f5f9; }
        .status-rascunho { color: #f59e0b; background-color: #fef3c7; }
        </style>
    """, unsafe_allow_html=True)

    # Cabeçalho da Tabela
    h1, h2, h3, h4, h5 = st.columns([3, 2, 2, 2, 1])
    h1.markdown("**Profissional**")
    h2.markdown("**Tipo de atuação/Polo**")
    h3.markdown("**Status do Cadastro**")
    h4.markdown("**Última atualização**")
    h5.markdown("**Ficha**")
    st.divider()

    # Linhas da Tabela
    for p in dados_profissionais:
        l1, l2, l3, l4, l5 = st.columns([3, 2, 2, 2, 1])
        
        # Coluna 1: Nome e Cargo
        l1.markdown(f"**{p['Profissional']}**<br><span style='font-size:0.8rem; color:#64748b;'>{p['Cargo']}</span>", unsafe_allow_html=True)
        
        # Coluna 2: Polo
        l2.write(p['Polo'])
        
        # Coluna 3: Status com Badge
        status_class = "status-rascunho" if p['Status'] == "Rascunhos" else "status-desmobilizado"
        l3.markdown(f"<span class='status-badge {status_class}'>{p['Status']}</span>", unsafe_allow_html=True)
        
        # Coluna 4: Data
        l4.write(p['Data'])
        
        # Coluna 5: Ícone PDF (Botão funcional)
        if l5.button("📝", key=p['Profissional']):
            st.toast(f"Abrindo ficha de {p['Profissional']}...")

    st.markdown(f"<p style='color:#64748b; font-size:0.8rem; margin-top:20px;'>Mostrando {len(dados_profissionais)} Profissionais</p>", unsafe_allow_html=True)
