import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Wavex | Multiplique suas Vendas como Afiliado",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ESTADO DE SESSÃO PARA AUTENTICAÇÃO (LOGIN)
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ""

# ESTILIZAÇÃO CUSTOMIZADA (PRETO, ROXO E ROSA NEON)
st.markdown("""
<style>
    /* Fundo Preto Profundo */
    .stApp {
        background-color: #08070b;
        color: #f3f4f6;
        font-family: 'Inter', system-ui, -apple-system, sans-serif;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Badge de Topo Neon */
    .hero-badge {
        display: inline-block;
        background-color: #130d1e;
        border: 1px solid #3b1859;
        color: #ff007f;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 20px;
    }
    .badge-dot {
        height: 8px;
        width: 8px;
        background-color: #ff007f;
        border-radius: 50%;
        display: inline-block;
        margin-right: 6px;
        box-shadow: 0 0 8px #ff007f;
    }

    /* Título Hero de Impacto (Roxo e Rosa) */
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        line-height: 1.15;
        color: #ffffff;
        margin-bottom: 15px;
        letter-spacing: -1px;
    }
    .hero-title-purple {
        background: linear-gradient(90deg, #9d4edd 0%, #ff007f 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Subtítulo */
    .hero-subtitle {
        font-size: 1.15rem;
        color: #a0a0ab;
        margin-bottom: 30px;
        max-width: 650px;
        line-height: 1.6;
    }

    /* Botões em Degradê Roxo/Rosa */
    .stButton>button {
        background: linear-gradient(135deg, #7928ca 0%, #ff007f 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.8rem 1.8rem !important;
        font-size: 15px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 15px rgba(255, 0, 127, 0.2);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(121, 40, 202, 0.5);
    }

    /* Cards de Recursos e Canais */
    .channel-card {
        background-color: #120e18;
        border: 1px solid #28193d;
        border-radius: 10px;
        padding: 12px 20px;
        text-align: center;
        color: #e2e8f0;
        font-weight: 600;
        font-size: 14px;
    }
    
    .feature-card {
        background-color: #100b16;
        border: 1px solid #28193d;
        border-radius: 12px;
        padding: 24px;
        height: 100%;
    }
    .feature-card h4 {
        color: #ffffff !important;
        font-size: 18px;
        margin-bottom: 10px;
    }
    .feature-card p {
        color: #94a3b8;
        font-size: 14px;
        margin: 0;
    }

    /* Topbar Navbar */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 0px 30px 0px;
    }
    .logo {
        font-size: 26px;
        font-weight: 900;
        color: #ffffff;
        letter-spacing: -0.5px;
    }
    .logo span {
        color: #ff007f;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SIDEBAR COM LOGIN E CONTROLES
# -----------------------------------------------------------------------------
st.sidebar.markdown("# 🔮 Wavex Control")

if not st.session_state['logged_in']:
    st.sidebar.subheader("Área de Membros")
    opcao_auth = st.sidebar.radio("Selecione:", ["Entrar na Conta", "Criar Nova Conta"])
    
    user_input = st.sidebar.text_input("Usuário / E-mail:")
    pass_input = st.sidebar.text_input("Senha:", type="password")
    
    if opcao_auth == "Entrar na Conta":
        if st.sidebar.button("ACESSAR PLATAFORMA"):
            if user_input and pass_input:
                st.session_state['logged_in'] = True
                st.session_state['user_name'] = user_input
                st.sidebar.success(f"Bem-vindo, {user_input}!")
                st.rerun()
            else:
                st.sidebar.error("Preencha usuário e senha!")
    else:
        if st.sidebar.button("CADASTRAR E ASSINAR"):
            if user_input and pass_input:
                st.session_state['logged_in'] = True
                st.session_state['user_name'] = user_input
                st.sidebar.success("Conta criada com sucesso!")
                st.rerun()
            else:
                st.sidebar.error("Preencha todos os campos!")
else:
    st.sidebar.success(f"Logado como: **{st.session_state['user_name']}**")
    st.sidebar.info("Plano: **Vip Vitalício Active**")
    st.sidebar.write("---")
    tag_user = st.sidebar.text_input("Sua Tag Afiliado Shopee/ML:", value="wavex_oficial_2026")
    
    if st.sidebar.button("Sair da Conta"):
        st.session_state['logged_in'] = False
        st.session_state['user_name'] = ""
        st.rerun()

# -----------------------------------------------------------------------------
# NAVBAR SUPERIOR (ESTILO MULTIPLACE)
# -----------------------------------------------------------------------------
col_nav1, col_nav2 = st.columns([4, 1])
with col_nav1:
    st.markdown('<div class="logo"><span>W</span> Wavex</div>', unsafe_allow_html=True)
with col_nav2:
    if not st.session_state['logged_in']:
        st.write("🔒 Faça login ao lado para liberar")
    else:
        st.write(f"🟢 **Online:** {st.session_state['user_name']}")

st.write("---")

# -----------------------------------------------------------------------------
# SEÇÃO HERO (ROXO E ROSA)
# -----------------------------------------------------------------------------
st.markdown("""
<div class="hero-badge">
    <span class="badge-dot"></span> Mineração + Automação de Afiliados
</div>
<h1 class="hero-title">
    Venda em todos os marketplaces <br>
    <span class="hero-title-purple">com comissões no piloto automático</span>
</h1>
<p class="hero-subtitle">
    A Wavex conecta você aos produtos virais mais quentes do Mercado Livre, Shopee e Amazon. 
    Pegue seu link de afiliado pronto, copie a copy de alta conversão e publique diretamente nos grupos certos.
</p>
""", unsafe_allow_html=True)

st.caption("🔒 7 dias de garantia • Cancele quando quiser • Sem fidelidade")
st.write(" ")

# CANAIS INTEGRADOS
col_c1, col_c2, col_c3, col_c4, col_c5 = st.columns(5)
with col_c1:
    st.markdown('<div class="channel-card">🟡 Mercado Livre</div>', unsafe_allow_html=True)
with col_c2:
    st.markdown('<div class="channel-card">🔴 Shopee</div>', unsafe_allow_html=True)
with col_c3:
    st.markdown('<div class="channel-card">🟠 Amazon</div>', unsafe_allow_html=True)
with col_c4:
    st.markdown('<div class="channel-card">🟣 Facebook Groups</div>', unsafe_allow_html=True)
with col_c5:
    st.markdown('<div class="channel-card">🟢 WhatsApp Groups</div>', unsafe_allow_html=True)

st.write(" ")
st.write(" ")

# -----------------------------------------------------------------------------
# PAINEL DA PLATAFORMA (BLOQUEADO CASO NÃO ESTEJA LOGADO)
# -----------------------------------------------------------------------------
if not st.session_state['logged_in']:
    st.warning("⚠️ **Acesso Restrito:** Faça Login ou Cadastre-se na barra lateral esquerda para acessar o painel de mineração e grupos.")

tab_minerador, tab_copys, tab_grupos, tab_planos = st.tabs([
    "🔥 Minerador de Produtos Quentes",
    "✍️ Gerador de Textos Persuasivos",
    "🎯 Diretório de Grupos (Links Reais)",
    "💳 Planos de Acesso (SaaS)"
])

# BASE DE DADOS DOS PRODUTOS
PRODUTOS_BASE = [
    {"id": 1, "plataforma": "Shopee", "categoria": "Beleza", "nome": "Kit Mini Liquidificador Portátil Recarregável", "preco": "R$ 39,90", "comissao": "14% (R$ 5,58)", "temp": "99° C (Alta Conversão)"},
    {"id": 2, "plataforma": "Shopee", "categoria": "Beleza", "nome": "Escova Rotativa Modeladora 5 em 1", "preco": "R$ 89,90", "comissao": "12% (R$ 10,78)", "temp": "98° C (Tendência)"},
    {"id": 3, "plataforma": "Mercado Livre", "categoria": "Eletrônicos", "nome": "Fone de Ouvido Sem Fio Bluetooth TWS", "preco": "R$ 49,90", "comissao": "10% (R$ 4,99)", "temp": "95° C (Top Vendas)"},
    {"id": 4, "plataforma": "Amazon", "categoria": "Casa", "nome": "Lâmpada LED Inteligente Wi-Fi Alexa", "preco": "R$ 54,90", "comissao": "9% (R$ 4,94)", "temp": "92° C (Procura Alta)"}
]

# -----------------------------------------------------------------------------
# TAB 1: MINERADOR DE PRODUTOS
# -----------------------------------------------------------------------------
with tab_minerador:
    if st.session_state['logged_in']:
        plat_sel = st.selectbox("Filtrar Marketplace:", ["Todos", "Shopee", "Mercado Livre", "Amazon"])
        tag_atual = st.session_state.get('user_name', 'wavex_afiliado')

        st.write("---")
        for p in PRODUTOS_BASE:
            if plat_sel == "Todos" or p["plataforma"] == plat_sel:
                link_final = f"https://{p['plataforma'].lower().replace(' ', '')}.com.br/item/{p['id']}?tag={tag_atual}"
                
                st.markdown(f"""
                <div class="feature-card" style="margin-bottom:15px;">
                    <span style="background:#7928ca; color:white; padding:2px 8px; border-radius:4px; font-size:12px; font-weight:bold;">{p['temp']}</span>
                    <span style="background:#ff007f; color:white; padding:2px 8px; border-radius:4px; font-size:12px; font-weight:bold; margin-left:5px;">Comissão: {p['comissao']}</span>
                    <h4 style="margin-top:10px;">{p['nome']}</h4>
                    <p>Plataforma: <b>{p['plataforma']}</b> | Preço Média: <b>{p['preco']}</b></p>
                </div>
                """, unsafe_allow_html=True)
                
                col_l1, col_l2 = st.columns([3, 1])
                with col_l1:
                    st.text_input("Seu Link de Afiliado Gerado:", value=link_final, key=f"link_{p['id']}")
                with col_l2:
                    st.write("")
                    st.write("")
                    if st.button("Copiar p/ Gerador", key=f"btn_{p['id']}"):
                        st.session_state['produto_nome'] = p['nome']
                        st.session_state['produto_link'] = link_final
                        st.success("Produto enviado para o gerador!")
    else:
        st.info("Efetue o login para visualizar os produtos e gerar os seus links com comissão.")

# -----------------------------------------------------------------------------
# TAB 2: GERADOR DE COPYS
# -----------------------------------------------------------------------------
with tab_copys:
    if st.session_state['logged_in']:
        nome_prod = st.text_input("Nome do Produto:", value=st.session_state.get('produto_nome', 'Kit Mini Liquidificador Portátil'))
        link_prod = st.text_input("Seu Link de Afiliado:", value=st.session_state.get('produto_link', 'https://shopee.com.br/item/1?tag=wavex_afiliado'))
        
        if st.button("GERAR TEXTO AUTOMÁTICO"):
            copy_gerada = f"""Gente, olha o que acabou de chegar pra mim! 😱😍
Comprei esse {nome_prod} e me surpreendeu demais a qualidade!

Pra quem sempre me pergunta onde eu compro essas coisas baratinhas, peguei no link oficial aqui:
👇
{link_prod}

Aproveitem que tá com frete grátis hoje! 🚀"""
            st.code(copy_gerada, language="text")
    else:
        st.info("Efetue o login para acessar o gerador de copys.")

# -----------------------------------------------------------------------------
# TAB 3: DIRETÓRIO DE GRUPOS (LINKS DIRETO DE ENTRADA E POSTAGEM)
# -----------------------------------------------------------------------------
with tab_grupos:
    if st.session_state['logged_in']:
        st.subheader("Entrar nos Grupos de Divulgação (Direto ao Ponto)")
        st.write("Clique no botão do grupo para abrir diretamente a página de entrada no Facebook ou WhatsApp:")
        
        # LISTA DE GRUPOS COM LINKS REAIS DE BUSCA E ENTRADA DIRETA
        grupos_reais = [
            {
                "nome": "Achadinhos da Shopee & Mercado Livre", 
                "tipo": "Facebook", 
                "membros": "180.000 membros",
                "link_direto": "https://www.facebook.com/groups/search/groups/?q=achadinhos%20shopee"
            },
            {
                "nome": "Ofertas & Promoções Femininas / Beleza", 
                "tipo": "Facebook", 
                "membros": "95.000 membros",
                "link_direto": "https://www.facebook.com/groups/search/groups/?q=promocoes%20femininas"
            },
            {
                "nome": "Gadgets, Tech e Achados Eletrônicos", 
                "tipo": "Facebook", 
                "membros": "210.000 membros",
                "link_direto": "https://www.facebook.com/groups/search/groups/?q=achados%20tecnologia"
            },
            {
                "nome": "Grupos de Promoções no WhatsApp (Diretório)", 
                "tipo": "WhatsApp", 
                "membros": "Vários Grupos Ativos",
                "link_direto": "https://www.google.com/search?q=grupos+whatsapp+achadinhos+shopee+link"
            }
        ]
        
        for idx, g in enumerate(grupos_reais):
            st.markdown(f"""
            <div class="feature-card" style="margin-bottom:15px;">
                <h4 style="margin:0; color:#ff007f !important;">{g['nome']} ({g['tipo']})</h4>
                <p>{g['membros']} • <span style="color:#00ff66;">Pronto para publicar</span></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Botão HTML Real de Redirecionamento Direto
            st.markdown(f'''
            <a href="{g['link_direto']}" target="_blank" style="text-decoration: none;">
                <button style="
                    background: linear-gradient(135deg, #7928ca 0%, #ff007f 100%);
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 6px;
                    font-weight: bold;
                    cursor: pointer;
                    width: 100%;
                    margin-bottom: 20px;">
                    👉 Entrar no Grupo e Publicar Agora
                </button>
            </a>
            ''', unsafe_allow_html=True)
            st.write("---")
    else:
        st.info("Efetue o login para liberar o acesso aos links dos grupos.")

# -----------------------------------------------------------------------------
# TAB 4: PLANOS & ASSINATURA (SAAS)
# -----------------------------------------------------------------------------
with tab_planos:
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.markdown("""
        <div class="feature-card" style="text-align:center;">
            <p style="color:#a0a0ab; font-weight:bold;">PLANO MENSAL</p>
            <h2 style="color:#ffffff !important; font-size:2.5rem; margin:10px 0;">R$ 19,90 <span style="font-size:14px; color:#a0a0ab;">/mês</span></h2>
            <p style="margin-bottom:20px;">Acesso completo a todas as ferramentas de mineração e grupos.</p>
            <hr style="border-color:#28193d;">
            <p style="text-align:left; margin:8px 0;">✅ Minerador de Produtos Quentes</p>
            <p style="text-align:left; margin:8px 0;">✅ Gerador de Copys Anti-Spam</p>
            <p style="text-align:left; margin:8px 0;">✅ Diretório de Grupos de Tráfego</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Assinar Plano Mensal", key="btn_mensal_saas")
        
    with col_p2:
        st.markdown("""
        <div class="feature-card" style="text-align:center; border: 2px solid #ff007f;">
            <span style="background:#ff007f; color:white; padding:3px 12px; border-radius:20px; font-size:12px; font-weight:bold;">MAIS POPULAR</span>
            <p style="color:#a0a0ab; font-weight:bold; margin-top:10px;">PLANO VITALÍCIO VIP</p>
            <h2 style="color:#ff007f !important; font-size:2.5rem; margin:10px 0;">R$ 49,90 <span style="font-size:14px; color:#a0a0ab;">/único</span></h2>
            <p style="margin-bottom:20px;">Pague uma única vez e tenha acesso para sempre.</p>
            <hr style="border-color:#28193d;">
            <p style="text-align:left; margin:8px 0;">✅ Tudo do Plano Mensal</p>
            <p style="text-align:left; margin:8px 0;">✅ Sem mensalidades ou renovações</p>
            <p style="text-align:left; margin:8px 0;">✅ Acesso Prioritário a Novos Grupos</p>
        </div>
        """, unsafe_allow_html=True)
        st.button("Garantir Acesso Vitalício", key="btn_vitalicio_saas")
