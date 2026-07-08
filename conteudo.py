import streamlit as st

def exibir_conteudo():
    st.title("Gabinete de Retórica, Oratória e Escrita")
    st.subheader("O guia definitivo para dominar a palavra falada e escrita com alta performance.")
    
    # Imagem de Destaque na Tela Inicial
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=1200&auto=format&fit=crop", 
             caption="A arte de influenciar e liderar através da palavra.", use_container_width=True)
    
    st.markdown("---")
    
    menu_teoria = st.selectbox(
        "Escolhe o módulo de estudo:",
        ["1. Fundamentos Psicológicos (Aristóteles)", 
         "2. Estruturação de Textos e Redação", 
         "3. Técnicas de Palco e Voz", 
         "4. Gestão de Crise e Combate ao Bloqueio"]
    )
    
    if menu_teoria == "1. Fundamentos Psicológicos (Aristóteles)":
        st.header("Os Pilares da Persuasão Humana")
        st.write("A retórica não é apenas falar bem; é a capacidade de identificar os meios de persuasão disponíveis para qualquer tema.")
        
        # Imagem do Módulo 1
        st.image("https://images.unsplash.com/photo-1455390582262-044cdead277a?q=80&w=600&auto=format&fit=crop", width=500)
        
        st.subheader("Aprofundamento Prático:")
        st.markdown("""
        *   **Ethos (Construção de Autoridade):** Antes de começares a falar, o público avalia a tua competência. Podes construir Ethos demonstrando preparação, citando fontes confiáveis e mantendo uma postura vertical e segura.
        *   **Pathos (Apelo Emocional):** As decisões humanas são baseadas em emoções e justificadas pela lógica. Usa narrativas (storytelling) onde haja um herói, um conflito claro e uma resolução inspiradora.
        *   **Logos (Arquitetura Lógica):** Usa silogismos e dados estatísticos. Evita generalizações como 'toda a gente sabe'. Usa dados concretos: 'Segundo dados oficiais de 2026...'.
        """)
        
    elif menu_teoria == "2. Estruturação de Textos e Redação":
        st.header("Guia Prático de Boa Escrita")
        st.write("Escrever com clareza é o primeiro passo para falar com impacto. Um texto confuso gera um discurso perdido.")
        
        # Imagem do Módulo 2
        st.image("https://images.unsplash.com/photo-1457369804613-52c61a468e7d?q=80&w=600&auto=format&fit=crop", width=500)
        
        st.subheader("As Quatro Fases da Redação Oratória:")
        st.markdown("""
        1.  **O Exórdio Provocador:** Nunca comeces a dizer 'Olá a todos, hoje vou falar sobre...'. Começa com um impacto. Uma pergunta direta, uma frase impactante em silêncio absoluto ou uma metáfora visual forte.
        2.  **A Proposição Claro:** Define em apenas uma frase o objetivo central do teu discurso. Se não conseguires resumir o teu tema numa linha, o teu texto ainda precisa de edição.
        3.  **A Confutação (Antecipação de Críticas):** Um bom escritor destrói os argumentos contrários antes mesmo que a audiência os levante. Diz abertamente: 'Muitos podem pensar que este projeto é caro, mas a verdade é que o retorno será o dobro...'.
        4.  **A Peroração (O Fecho de Ouro):** Termina no pico da energia. Usa uma estrutura de frases paralelas (ritmo) e encerra com uma frase de efeito memorável.
        """)
        
    elif menu_teoria == "3. Técnicas de Palco e Voz":
        st.header("Domínio da Linguagem Corporal e Expressão Vocal")
        st.write("O corpo fala antes da boca emitir o primeiro som. A tua postura dita como serás recebido.")
        
        # Imagem do Módulo 3
        st.image("https://images.unsplash.com/photo-1475721027785-f74eccf877e2?q=80&w=600&auto=format&fit=crop", width=500)
        
        st.subheader("Checklist de Performance Física:")
        st.markdown("""
        *   **A Posição de Base:** Pés alinhados com os ombros, peso distribuído igualmente. Evita balançar o corpo para os lados, pois isso demonstra ansiedade subconsciente.
        *   **Gestos Abertos:** Mostra as palmas das mãos. Historicamente, mostrar as mãos significa 'não tenho armas, podes confiar em mim'. Gestos acima da linha da cintura demonstram entusiasmo.
        *   **Modulação Vocal:** 
            *   *Volume Alto:* Para fazer chamadas de atenção ou declarações fortes.
            *   *Volume Baixo/Sussurro:* Para criar intimidade, segredo e focar a atenção total da sala.
            *   *Ritmo Lento:* Passa solenidade, seriedade e importância extrema.
        """)
        
    elif menu_teoria == "4. Gestão de Crise e Combate ao Bloqueio":
        st.header("Como Controlar a Ansiedade e Brancos Mentais")
        st.write("Sentir o coração acelerar é apenas o teu corpo a dar-te energia extra para o desafio.")
        
        # Imagem do Módulo 4
        st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=600&auto=format&fit=crop", width=500)
        
        st.subheader("Técnicas de Emergência no Palco:")
        st.markdown("""
        *   **O Branco Mental:** Se esqueceres o que ias dizer, nunca digas 'esqueci-me' ou 'onde é que eu ia?'. Faz uma pausa intencional, caminha dois passos para o lado lentamente, olha para o público e repete a última frase que disseste com convicção ou faz uma pergunta retórica à plateia para ganhares 5 segundos de raciocínio.
        *   **Ansiedade Física:** Faz exercícios de respiração diafragmática profunda minutos antes de falar. O oxigénio extra engana o cérebro, reduzindo a produção de cortisol e adrenalina.
        """)