import streamlit as st

def exibir_quiz():
    st.title("Simulador de Debates e Tomada de Decisão")
    st.subheader("Treina a tua mente para responder sob pressão e identificar falácias.")
    
    # Imagem da Tela de Quiz
    st.image("https://images.unsplash.com/photo-1541872703-74c5e44368f9?q=80&w=1200&auto=format&fit=crop", 
             caption="O conhecimento testa-se na prática.", use_container_width=True)
    
    st.markdown("---")
    
    perguntas = [
        {
            "id": 1,
            "pergunta": "Durante um debate, o teu oponente ataca a tua vida pessoal ao invés de responder ao teu argumento técnico. Que falácia cometeu ele?",
            "opcoes": ["Falácia do Espantalho", "Falácia Ad Hominem", "Apelo à Ignorância", "Falso Dilema"],
            "correta": "Falácia Ad Hominem",
            "explicacao": "Ad Hominem ocorre quando alguém ataca diretamente a pessoa ou o caráter do oponente em vez de refutar o argumento apresentado."
        },
        {
            "id": 2,
            "pergunta": "Se queres convencer a audiência usando estatísticas oficiais, estudos científicos e dados concretos, qual pilar estás a priorizar?",
            "opcoes": ["Ethos", "Pathos", "Logos", "Nenhum dos anteriores"],
            "correta": "Logos",
            "explicacao": "Logos representa o uso do raciocínio lógico, factos e dados empíricos para sustentar um argumento."
        },
        {
            "id": 3,
            "pergunta": "Qual é a melhor forma de iniciar um discurso para captar a atenção imediata do público?",
            "opcoes": [
                "Pedir desculpa por estar nervoso ou despreparado",
                "Começar com uma pergunta retórica provocadora ou uma história impactante",
                "Ler detalhadamente todo o teu currículo académico",
                "Ficar em silêncio até que reparem em ti espontaneamente"
            ],
            "correta": "Começar com uma pergunta retórica provocadora ou uma história impactante",
            "explicacao": "Os primeiros segundos são cruciais. Histórias e perguntas retóricas ativam a curiosidade e criam conexão imediata com a mente da audiência."
        },
        {
            "id": 4,
            "pergunta": "Se a tua voz está muito monótona e a audiência parece estar a dispersar, qual deve ser a tua reação imediata?",
            "opcoes": [
                "Falar mais rápido para acabar o discurso o quanto antes",
                "Alterar drasticamente a modulação, aplicando uma pausa prolongada ou variando o volume e tom da voz",
                "Ignorar o público e continuar a ler os apontamentos",
                "Pedir para acenderem as luzes da sala"
            ],
            "correta": "Alterar drasticamente a modulação, aplicando uma pausa prolongada ou variando o volume e tom da voz",
            "explicacao": "A quebra de padrão vocal (mudar a velocidade, altura ou introduzir silêncios) força o cérebro dos ouvintes a focar-se novamente em ti."
        }
    ]
    
    for p in perguntas:
        st.markdown(f"❓ **Cenário Prático {p['id']}:** {p['pergunta']}")
        resposta = st.radio("Escolhe a estratégia correta:", p['opcoes'], key=f"q_{p['id']}")
        
        if st.button("Submeter Resposta", key=f"btn_{p['id']}"):
            if resposta == p['correta']:
                st.success("🎯 Excelente análise! Resposta Certa.")
            else:
                st.error(f"❌ Resposta incorreta. A melhor abordagem seria: {p['correta']}.")
            st.info(f"💡 **Análise Estratégica:** {p['explicacao']}")
        st.markdown("---")