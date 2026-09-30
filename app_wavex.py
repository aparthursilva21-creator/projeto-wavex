import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Wavex Marketing | Plataforma de Vendas e Afiliados",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização Neon Futurist / Cyberpunk Profissional (Wavex Brand)
st.markdown("""
<style>
    .main { background-color: #0b0e14; color: #e6edf3; }
    .stApp { background-color: #0b0e14; }
    h1, h2, h3, h4 { color: #7928CA !important; font-family: 'Segoe UI', sans-serif; font-weight: 800; }
    
    .wavex-header {
        background: linear-gradient(90deg, #7928CA 0%, #FF0080 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.8rem;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0px;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #7928CA 0%, #FF0080 100%);
        color: #ffffff;
        font-weight: 800;
        border-radius: 8px;
        border: none;
        padding: 0.7rem 1.2rem;
        width: 100%;
        box-shadow: 0px 4px 15px rgba(255, 0, 128, 0.3);
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0px 6px 20px rgba(121, 40, 202, 0.6);
        color: #ffffff;
    }
    
    .card-produto {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 15px;
    }
    .badge-quente {
        background-color: #FF0080;
        color: white;
        padding: 3px 8px;
        border-radius: 5px;
        font-size: 12px;
        font-weight: bold;
    }
    .badge-comissao {
        background-color: #00ff66;
        color: black;
        padding: 3px 8px;
        border-radius: 5px;
        font-size: 12px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# BANCO DE DADOS SIMULADO - PRODUTOS EM ALTA
PRODUTOS_BASE = [
    {
        "id": 1, "plataforma": "Shopee", "categoria": "Feminino / Beleza", 
        "nome": "Kit Mini Liquidificador Portatil Recarregavel USB", 
        "preco": "R$ 39,90", "comissao": "14% (R$ 5,58)", "temperatura": "99° C (Alta Conversão)",
        "link_origem": "https://shopee.com.br"
    },
    {
        "id": 2, "plataforma": "Shopee", "categoria": "Feminino / Beleza", 
        "nome": "Escova Rotativa Modeladora de Cabelo 5 em 1 Multifuncional", 
        "preco": "R$ 89,90", "comissao": "12% (R$ 10,78)", "temperatura": "98° C (Tendência)",
        "link_origem": "https://shopee.com.br"
    },
    {
        "id": 3, "plataforma": "Mercado Livre", "categoria": "Masculino / Eletrônicos", 
        "nome": "Fone de Ouvido Sem Fio Bluetooth TWS Esportivo com LED", 
        "preco": "R$ 49,90", "comissao": "10% (R$ 4,99)", "temperatura": "95° C (Top Vendas)",
        "link_origem": "https://mercadolivre.com.br"
    },
    {
        "id": 4, "plataforma": "Mercado Livre", "categoria": "Masculino / Utilitários", 
        "nome": "Kit Maquina de Cortar Cabelo e Barba Sem Fio Vintage T9", 
        "preco": "R$ 35,00", "comissao": "13% (R$ 4,55)", "temperatura": "97° C (Viral no TikTok)",
        "link_origem": "https://mercadolivre.com.br"
    },
    {
        "id": 5, "plataforma": "Amazon", "categoria": "Casa / Utilidades", 
        "nome": "Lampada LED Inteligente Wi-Fi RGB Compativel com Alexa", 
        "preco": "R$ 54,90", "comissao": "9% (R$ 4,94)", "temperatura": "92° C (Procura Alta)",
        "link_origem": "https://amazon.com.br"
    },
    {
        "id": 6, "plataforma": "Shopee", "categoria": "Casa / Organização", 
        "nome": "Mop Esfregao Limpeza Giratorio 360 com Balde Centrifuga", 
        "preco": "R$ 69,90", "comissao": "15% (R$ 10,48)", "temperatura": "100° C (Recorde de Vendas)",
        "link_origem": "https://shopee.com.br"
    }
]

# GRUPOS CATEGORIZADOS PARA DIVULGAÇÃO
GRUPOS_DIVULGACAO = [
    {"nicho": "Feminino / Beleza", "tipo": "Facebook", "nome": "Achadinhos da Internet & Dicas de Beleza", "membros": "142.000", "link": "https://facebook.com/groups"},
    {"nicho": "Feminino / Beleza", "tipo": "Facebook", "nome": "Ofertas Dicas e Cuidado Feminino", "membros": "89.000", "link": "https://facebook.com/groups"},
    {"nicho": "Feminino / Beleza", "tipo": "WhatsApp", "nome": "Achados & Promos Femininas #04", "membros": "240/257", "link": "https://chat.whatsapp.com"},
    {"nicho": "Masculino / Eletrônicos", "tipo": "Facebook", "nome": "Importados Eletronicos & Gadgets Brasil", "membros": "210.000", "link": "https://facebook.com/groups"},
    {"nicho": "Masculino / Eletrônicos", "tipo": "WhatsApp", "nome": "Clube dos Achadinhos Tech & Promos", "membros": "250/257", "link": "https://chat.whatsapp.com"},
    {"nicho": "Casa / Utilidades", "tipo": "Facebook", "nome": "Mães e Donas de Casa Organizadas", "membros": "310.000", "link": "https://facebook.com/groups"},
    {"nicho": "Casa / Utilidades", "tipo": "WhatsApp", "nome": "Promocoes para Lar & Cozinha", "membros": "215/257", "link": "https://chat.whatsapp.com"}
]

# BARRA LATERAL DA WAVEX
st.sidebar.markdown("# WAVEX MARKETING")
st.sidebar.caption("SaaS de Automacao & Afiliados v2.0")
st.sidebar.write("---")

# SIMULADOR DE CONEXÃO DE CONFIGURAÇÃO DE AFILIADOS
st.sidebar.subheader("Minhas Credenciais de Afiliado")
tag_shopee = st.sidebar.text_input("ID / Tag Afiliado Shopee:", value="wavex_afiliado_123")
tag_ml = st.sidebar.text_input("ID Afiliado Mercado Livre:", value="ML_WAVEX_987")
tag_amazon = st.sidebar.text_input("ID Associate Amazon:", value="wavex-20")

if st.sidebar.button("SALVAR INTEGRACAO"):
    st.sidebar.success("APIs Conectadas com Sucesso!")

st.sidebar.write("---")
st.sidebar.info("Status da Conta: ASSINATURA VIP ATIVA\nPlano: Vitalicio Wavex")

# NAVEGAÇÃO PRINCIPAL
st.markdown('<div class="wavex-header">WAVEX MARKETING</div>', unsafe_allow_html=True)
st.caption("Plataforma Inteligente de Mineração de Produtos Virais, Copys e Grupos de Trafego Orgânico")

tab_tutorial, tab_minerador, tab_copys, tab_grupos, tab_planos = st.tabs([
    "Como Funciona (Passo a Passo)",
    "Minerador de Produtos Quentes",
    "Gerador de Textos Persuasivos",
    "Diretório de Grupos (Facebook / Whats)",
    "Planos & Assinatura (SaaS)"
])

# -----------------------------------------------------------------------------
# TAB 1: TUTORIAL E COMO FUNCIONA O PROJETO
# -----------------------------------------------------------------------------
with tab_tutorial:
    st.subheader("Como Funciona o Sistema Wavex Marketing")
    st.write("Aprenda em 4 passos simples como usar a estrutura para gerar comissões diárias no piloto automático.")
    
    col_t1, col_t2 = st.columns(2)
    
    with col_t1:
        st.markdown("""
        #### 1. Conecte suas Contas de Afiliado
        Insira suas Tags de Afiliado da Shopee, Mercado Livre e Amazon na barra lateral. O sistema usa esses dados para transformar automaticamente qualquer link de produto normal no seu **link de afiliado com comissão**.
        
        #### 2. Escolha Produtos Quentes
        Acesse a aba **Minerador de Produtos Quentes**. Nossa inteligência filtra os itens com maior volume de vendas e taxa de conversão do dia no mercado.
        """)
        
    with col_t2:
        st.markdown("""
        #### 3. Gere a Copy (Texto de Venda)
        Copie o texto gerado na aba **Gerador de Textos**. O algoritmo cria abordagens humanas e descontraídas para evitar bloqueios e spams.
        
        #### 4. Divulgue nos Grupos Certos
        Acesse o **Diretório de Grupos**, escolha o nicho correspondente e compartilhe. Quando comprarem, a comissão cai na sua conta.
        """)

# -----------------------------------------------------------------------------
# TAB 2: MINERADOR DE PRODUTOS QUENTES
# -----------------------------------------------------------------------------
with tab_minerador:
    st.subheader("Produtos Mais Vendidos do Dia (Produtos Quentes)")
    
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        plat_filtro = st.selectbox("Filtrar por Plataforma:", ["Todas", "Shopee", "Mercado Livre", "Amazon"])
    with col_f2:
        cat_filtro = st.selectbox("Filtrar por Nicho/Categoria:", ["Todas", "Feminino / Beleza", "Masculino / Eletrônicos", "Casa / Utilidades"])
    with col_f3:
        busca_termo = st.text_input("Buscar produto por nome:", "")

    prods_filtrados = PRODUTOS_BASE
    if plat_filtro != "Todas":
        prods_filtrados = [p for p in prods_filtrados if p["plataforma"] == plat_filtro]
    if cat_filtro != "Todas":
        prods_filtrados = [p for p in prods_filtrados if p["categoria"] == cat_filtro]
    if busca_termo:
        prods_filtrados = [p for p in prods_filtrados if busca_termo.lower() in p["nome"].lower()]

    st.write("---")
    
    for prod in prods_filtrados:
        if prod["plataforma"] == "Shopee":
            link_afiliado_gerado = f"{prod['link_origem']}/universal-link?sub_id={tag_shopee}&item={prod['id']}"
        elif prod["plataforma"] == "Mercado Livre":
            link_afiliado_gerado = f"{prod['link_origem']}/p/MLB{prod['id']}?matt_tool={tag_ml}"
        else:
            link_afiliado_gerado = f"{prod['link_origem']}/dp/B00{prod['id']}?tag={tag_amazon}"

        st.markdown(f"""
        <div class="card-produto">
            <span class="badge-quente">{prod['temperatura']}</span> 
            <span class="badge-comissao">Comissão: {prod['comissao']}</span>
            <h4 style="margin-top:10px;">{prod['nome']}</h4>
            <p><b>Plataforma:</b> {prod['plataforma']} | <b>Categoria:</b> {prod['categoria']} | <b>Preço Médio:</b> {prod['preco']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col_p1, col_p2 = st.columns([3, 1])
        with col_p1:
            st.text_input(f"Seu Link de Afiliado PRONTO ({prod['plataforma']}):", value=link_afiliado_gerado, key=f"link_{prod['id']}")
        with col_p2:
            st.write("")
            st.write("")
            if st.button(f"Usar no Gerador", key=f"btn_use_{prod['id']}"):
                st.session_state['produto_selecionado'] = prod['nome']
                st.session_state['link_selecionado'] = link_afiliado_gerado
                st.info("Produto selecionado! Vá até a aba 'Gerador de Textos'.")

# -----------------------------------------------------------------------------
# TAB 3: GERADOR DE TEXTOS PERSUASIVOS (COPYS)
# -----------------------------------------------------------------------------
with tab_copys:
    st.subheader("Gerador de Copys Virais para Grupos")
    
    prod_nome_input = st.text_input("Nome do Produto:", value=st.session_state.get('produto_selecionado', 'Kit Mini Liquidificador Portatil Recarregavel USB'))
    link_afiliado_input = st.text_input("Seu Link de Afiliado:", value=st.session_state.get('link_selecionado', 'https://shopee.com.br/universal-link?sub_id=wavex_afiliado_123'))
    
    estilo_copy = st.selectbox("Estilo de Abordagem:", [
        "Recomendação Pessoal / Achadinho (Mais Natural - Altíssima Conversão)",
        "Urgência / Desconto Surpresa (Foco em Clique Rápido)",
        "Pergunta Curiosa (Gera Engajamento nos Comentários)",
        "Direto ao Ponto (ideal para Grupos de Promoções)"
    ])
    
    if st.button("GERAR TEXTO PARA COMPARTILHAR"):
        st.markdown("#### Copie o texto abaixo e cole no seu grupo:")
        
        if "Recomendação Pessoal" in estilo_copy:
            texto_copy = f"""Gente, olha o que acabou de chegar pra mim! 😱😍
Comprei esse {prod_nome_input} e me surpreendeu demais a qualidade pelo preço. 

Pra quem sempre me pergunta onde eu compro essas coisas baratinhas, peguei em promoção nesse link oficial aqui:
👇👇
{link_afiliado_input}

Vale super a pena, a entrega foi rapidinha!"""

        elif "Urgência / Desconto" in estilo_copy:
            texto_copy = f"""🚨 ALERTA DE PROMOÇÃO / MENOR PREÇO DO ANO! 🚨

{prod_nome_input} tá com um desconto bizarro hoje no site oficial.

Deixe seu cupom applied acessando pelo link abaixo:
🛒 Clique aqui para pegar o desconto: {link_afiliado_input}

Corram porque esse valor costuma acabar em poucas horas! 🔥"""

        elif "Pergunta Curiosa" in estilo_copy:
            texto_copy = f"""Alguém aqui já testou esse {prod_nome_input}? 🤔
Tô doida pra pegar um porque vi todo mundo falando bem no TikTok. Achei o menor valor dele aqui com frete grátis:

👉 {link_afiliado_input}

Acham que compensa?"""

        else:
            texto_copy = f"""🔥 ACHADO DO DIA!
📦 {prod_nome_input}

✅ Frete Grátis disponível
✅ Garantia de entrega oficial
✅ Vendedor com nota máxima

Link com desconto exclusivo:
{link_afiliado_input}"""

        st.code(texto_copy, language="text")

# -----------------------------------------------------------------------------
# TAB 4: DIRETÓRIO DE GRUPOS CATEGORIZADOS
# -----------------------------------------------------------------------------
with tab_grupos:
    st.subheader("Diretório de Grupos para Divulgação de Links")
    st.write("Acesse grupos segmentados onde o público certo já está reunido esperando indicações de compras.")
    
    nicho_grupo_sel = st.selectbox("Escolha o Nicho dos Grupos:", ["Todos", "Feminino / Beleza", "Masculino / Eletrônicos", "Casa / Utilidades"])
    
    grupos_filtrados = GRUPOS_DIVULGACAO
    if nicho_grupo_sel != "Todos":
        grupos_filtrados = [g for g in grupos_filtrados if g["nicho"] == nicho_grupo_sel]
        
    for idx, grp in enumerate(grupos_filtrados):
        col_g1, col_g2, col_g3 = st.columns([3, 2, 1])
        with col_g1:
            st.markdown(f"**{grp['nome']}** ({grp['tipo']})")
            st.caption(f"Nicho: {grp['nicho']} | Membros / Ativos: {grp['membros']}")
        with col_g2:
            st.markdown(f"Status: <span style='color:#00ff66;'><b>Grupo Aberto</b></span>", unsafe_allow_html=True)
        with col_g3:
            st.markdown(f'<a href="{grp["link"]}" target="_blank" style="text-decoration:none;"><button style="background:#7928CA; color:white; border:none; padding:8px 12px; border-radius:5px; cursor:pointer;">Entrar no Grupo</button></a>', unsafe_allow_html=True)
        st.write("---")

# -----------------------------------------------------------------------------
# TAB 5: ÁREA DE VENDAS DA ASSINATURA DA WAVEX (SAAS)
# -----------------------------------------------------------------------------
with tab_planos:
    st.subheader("Monetização da Plataforma Wavex Marketing")
    st.write("Essa é a estrutura de planos pronta para você vender o acesso da sua plataforma para terceiros.")
    
    col_pl1, col_pl2 = st.columns(2)
    
    with col_pl1:
        st.markdown("""
        <div style="background-color:#161b22; border:1px solid #7928CA; border-radius:12px; padding:25px; text-align:center;">
            <h3>PLANO MENSAL</h3>
            <h1 style="color:#FF0080 !important;">R$ 19,90 <span style="font-size:16px;">/mês</span></h1>
            <p>Acesso completo à plataforma Wavex</p>
            <hr style="border-color:#30363d;">
            <p>✅ Minerador de Produtos Quentes</p>
            <p>✅ Gerador Automático de Copys</p>
            <p>✅ Conexão com Shopee, Mercado Livre e Amazon</p>
            <p>✅ Atualizações Semanais de Grupos</p>
            <br>
            <button style="width:100%; padding:10px; background:#7928CA; color:white; border:none; border-radius:6px; font-weight:bold;">Assinar Mensal</button>
        </div>
        """, unsafe_allow_html=True)

    with col_pl2:
        st.markdown("""
        <div style="background-color:#161b22; border:2px solid #FF0080; border-radius:12px; padding:25px; text-align:center;">
            <span style="background:#FF0080; color:white; padding:3px 10px; border-radius:20px; font-weight:bold; font-size:12px;">MAIS VENDIDO</span>
            <h3 style="margin-top:10px;">PLANO VITALÍCIO VIP</h3>
            <h1 style="color:#00ff66 !important;">R$ 49,90 <span style="font-size:16px;">/único</span></h1>
            <p>Acesso para sempre sem mensalidades</p>
            <hr style="border-color:#30363d;">
            <p>✅ Tudo do Plano Mensal</p>
            <p>✅ Acesso Vitalício Garantido</p>
            <p>✅ Suporte Prioritário no WhatsApp</p>
            <p>✅ Treinamento Exclusivo de Tráfego Orgânico</p>
            <br>
            <button style="width:100%; padding:10px; background:#FF0080; color:white; border:none; border-radius:6px; font-weight:bold;">Garantir Acesso Vitalício</button>
        </div>
        """, unsafe_allow_html=True)
