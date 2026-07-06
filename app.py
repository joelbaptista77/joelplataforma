import streamlit as st
from conteudo import LICOES
from quiz import PERGUNTAS

# Configuração de interface avançada do navegador
st.set_page_config(
    page_title="Mentor de Retórica, Escrita e Oratória", 
    page_icon="🎓", 
    layout="wide"
)

# Cabeçalho Principal Customizado
st.title("🎓 Sistema de Alta Performance: Retórica e Oratória")
st.markdown("---")

# Menu Avançado na Barra Lateral
with st.sidebar:
    # Imagem decorativa superior da barra lateral
    st.image("https://images.unsplash.com/photo-1455390582262-044cdead277a?w=500&auto=format&fit=crop&q=60", use_container_width=True)
    st.header("🎯 Central de Controlo")
    menu = st.radio(
        "Selecione o Ambiente da Plataforma:",
        ["Apresentação do Projeto", "Laboratório de Conteúdo", "Simulador Técnico (Quiz)"]
    )
    st.write("---")
    st.caption("Desenvolvido em Python para Fins Académicos Avançados. © 2026")

# 1. TELA DE APRESENTAÇÃO
if menu == "Apresentação do Projeto":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Transformação Prática através da Ciência Linguística")
        st.markdown("""
        Esta plataforma foi desenhada especificamente para afastar a teoria vaga e focar-se na **mudança mecânica e comportamental** do estudante. Aqui não vais estudar apenas história; vais aprender a posicionar os teus pés, estruturar o teu sistema respiratório e desenhar frases como um profissional.
        
        ### 🧪 O que este software executa em tempo real:
        *   **Módulos Anatómicos Dinâmicos:** Guias passo a passo sobre a engenharia por trás do corpo e do texto.
        *   **Recursos Expansíveis de Mentoria:** Caixas de dicas práticas ocultas para estudo focado.
        *   **Simulador de Respostas Imediatas:** Sistema de quiz adaptativo com correção instantânea e fundamentada.
        """)
        
        # Galeria Visual de Conceitos Solicitada para o App.py
        st.markdown("#### 🎨 Pilares Visuais da Comunicação")
        col_img1, col_img2, col_img3 = st.columns(3)
        with col_img1:
            st.image("https://images.unsplash.com/photo-1517486808906-6ca8b3f04846?w=400&auto=format&fit=crop&q=60", caption="Retórica e Persuasão", use_container_width=True)
        with col_img2:
            st.image("https://images.unsplash.com/photo-1475721027785-f74eccf877e2?w=400&auto=format&fit=crop&q=60", caption="Oratória e Leitura Pública", use_container_width=True)
        with col_img3:
            st.image("https://images.unsplash.com/photo-1455390582262-044cdead277a?w=400&auto=format&fit=crop&q=60", caption="Arte da Boa Escrita", use_container_width=True)

    with col2:
        st.info("💡 **Conceito Académico:** A oratória de excelência baseia-se na repetição consciente das posições físicas corretas até que se tornem automáticas.")

# 2. TELA DOS MÓDULOS DE ESTUDO (Aprofundado com Injeção de Imagens Estritas)
elif menu == "Laboratório de Conteúdo":
    st.header("📖 Laboratório de Conteúdo Prático")
    st.write("Selecione o módulo pretendido abaixo para carregar o manual completo de treino.")
    
    modulo_selecionado = st.selectbox(
        "Selecione o Manual Técnico que deseja estudar agora:", 
        list(LICOES.keys())
    )
    
    st.markdown("---")
    
    # Lógica de renderização que insere as imagens exemplares no meio do texto
    texto_completo = LICOES[modulo_selecionado]
    
    if "IMAGEM_ORADOR_POSTURA" in texto_completo:
        partes = texto_completo.split("IMAGEM_ORADOR_POSTURA")
        st.markdown(partes[0])
        st.image("https://images.unsplash.com/photo-1544531516-a5e3579f4de9?w=700&auto=format&fit=crop&q=80", caption="Demonstração Exemplar: Base firme alinhada aos ombros e gestos abertos na zona de segurança.", width=650)
        st.markdown(partes[1])
        
    elif "IMAGEM_LEITURA_ORATORIA" in texto_completo:
        partes = texto_completo.split("IMAGEM_LEITURA_ORATORIA")
        st.markdown(partes[0])
        st.image("https://images.unsplash.com/photo-1524178232363-1fb2b075b655?w=700&auto=format&fit=crop&q=80", caption="Demonstração Exemplar: Altura correta do texto para desobstrução laríngea e contacto visual.", width=650)
        st.markdown(partes[1])
        
    elif "IMAGEM_ESCRITA_POSICAO" in texto_completo:
        partes = texto_completo.split("IMAGEM_ESCRITA_POSICAO")
        st.markdown(partes[0])
        st.image("https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=700&auto=format&fit=crop&q=80", caption="Ergonomia Condicional: Ângulos de apoio corretos para escrita prolongada de alta performance.", width=650)
        st.markdown(partes[1])
    else:
        st.markdown(texto_completo)
    
    st.markdown("---")
    st.subheader("⚙️ Atividades e Recursos do Módulo Selecionado")
    
    tab1, tab2 = st.tabs(["🏋️‍♂️ Treino de Aplicação Prática", "⚠️ Erros Críticos a Evitar"])
    
    with tab1:
        st.write("Executa este checklist físico ou textual hoje mesmo:")
        if modulo_selecionado == "A Postura Física do Orador":
            st.checkbox("Treino do Espelho: Ficar 2 minutos na base axial sem balançar.")
            st.checkbox("Mapeamento Retórico: Colocar 3 objetos no quarto e treinar a fixação do olhar em cada um por 5 segundos.")
        elif modulo_selecionado == "A Dinâmica da Voz e Leitura":
            st.checkbox("Técnica do Queixo: Ler um texto mantendo o queixo paralelo ao chão e gravando no telemóvel.")
            st.checkbox("Checklist da Pausa: Fazer pausas conscientes de 3 segundos em cada ponto final de uma notícia.")
        elif modulo_selecionado == "Mecanismos Práticos da Escrita":
            st.checkbox("Ajuste Ergonómico: Configurar a cadeira e a mesa de escrita seguindo os 3 ângulos de 90°.")
            st.checkbox("Caça ao 'Que': Pegar num parágrafo antigo e eliminar pelo menos três palavras desnecessárias.")

    with tab2:
        if modulo_selecionado == "A Postura Física do Orador":
            st.warning("**Nunca** coloques as duas mãos nos bolsos traseiros ou cruzes os braços à frente do peito durante uma apresentação. Isto destrói a tua credibilidade biológica instantaneamente.")
        elif modulo_selecionado == "A Dinâmica da Voz e Leitura":
            st.error("**Erro Fatal:** Tentar falar até esgotar completamente o ar dos pulmões. Isto gera um som trémulo e força as pregas vocais, causando danos severos a longo prazo.")
        elif modulo_selecionado == "Mecanismos Práticos da Escrita":
            st.warning("**Cuidado:** Escrever blocos maciços de texto com mais de 8 linhas sem quebras de parágrafo faz com que o leitor desista da leitura por cansaço visual.")

# 3. TELA DO QUIZ INTERATIVO
elif menu == "Simulador Técnico (Quiz)":
    st.header("🧠 Simulador Técnico de Validação Académica")
    st.write("Testa o teu nível de retenção das mecânicas estudadas. O sistema avalia a tua resposta no mesmo segundo.")
    st.write("---")
    
    for i, item in enumerate(PERGUNTAS):
        st.markdown(f"##### **Questão {i+1}:** {item['pergunta']}")
        
        resposta = st.radio(
            "Escolha a sua resposta:", 
            item["opcoes"], 
            key=f"quiz_avancado_{i}", 
            index=None
        )
        
        if resposta is not None:
            if resposta == item["correta"]:
                st.success(f"✅ **Excelente!** {item['explicacao']}")
            else:
                st.error(f"❌ **Incorreto.** Reanalise o conceito: {item['explicacao']}")
        st.write("---")