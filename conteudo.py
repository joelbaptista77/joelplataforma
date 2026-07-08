import streamlit as st

def exibir_conteudo():
    st.title("Gabinete de Retórica, Oratória e Escrita")
    st.subheader("O guia definitivo para dominar a palavra falada e escrita com alta performance.")
    
    # Imagem de Destaque na Tela Inicial
    st.image("https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?q=80&w=1200&auto=format&fit=crop", 
             caption="A arte de influenciar e liderar através da palavra.", use_container_width=True)
    
    st.markdown("---")
    
    menu_teoria = st.selectbox(
        "Escolhe o módulo de estudo avançado:",
        ["1. Fundamentos Psicológicos e a Retórica Clássica (Aristóteles)", 
         "2. Estruturação de Textos, Redação e Figuras de Estilo", 
         "3. Técnicas de Palco, Voz, Expressão e Microfone", 
         "4. Gestão de Crise, Combate ao Bloqueio e Resiliência Oratória"]
    )
    
    if menu_teoria == "1. Fundamentos Psicológicos e a Retórica Clássica (Aristóteles)":
        st.header("Módulo I: A Engenharia Clássica da Persuasão")
        st.write("A retórica, formalizada por Aristóteles na Grécia Antiga, não é a arte da manipulação vazia, mas sim a ciência de extrair e apresentar a verdade de forma irresistível para a mente humana.")
        
        st.image("https://images.unsplash.com/photo-1455390582262-044cdead277a?q=80&w=600&auto=format&fit=crop", width=500)
        
        st.subheader("📜 Desdobramento Profundo dos Três Pilares")
        
        st.markdown("""
        ### **1. ETHOS (A Construção da Credibilidade)**
        O Ethos opera antes mesmo de abrires a boca. É o julgamento subconsciente que a audiência faz sobre o teu caráter, competência e benevolência.
        *   **Autoridade Intrínseca:** Construída através do teu histórico, títulos e reputação prévia.
        *   **Autoridade Extrínseca (No Palco):** Demonstra-se através da precisão vocabular, vestuário adequado ao contexto e firmeza nas primeiras frases. Se hesitares no exórdio, o teu Ethos cai drasticamente.
        *   **A Tríade de Aristóteles para o Ethos:** *Phronesis* (sabedoria prática), *Arete* (virtude moral) e *Eunoia* (boa vontade para com o público). Deves mostrar que és inteligente, honesto e que queres genuinamente ajudar quem te ouve.

        ### **2. PATHOS (A Psicologia e a Conexão Emocional)**
        As pessoas não compram ideias baseadas apenas em factos frios; elas agem pela emoção e justificam com a lógica. O Pathos dita o estado emocional da plateia.
        *   **A Escala de Sentimentos:** Um orador mestre sabe mover o público da apatia para a indignação, e da indignação para a esperança.
        *   **O Poder do Storytelling:** O cérebro humano está biologicamente programado para processar narrativas. Ao contar uma história com um protagonista claro, um obstáculo intransponível e uma lição moral, os neurónios espelho da audiência disparam, criando empatia instantânea.

        ### **3. LOGOS (A Arquitetura Racional e Argumentativa)**
        A fundação intelectual do teu discurso. Sem Logos, o Pathos transforma-se em demagogia e o Ethos desmorona sob escrutínio.
        *   **O Entimema:** Um silogismo dedutivo onde uma das premissas é omitida porque o público já a assume como verdadeira. Exemplo: *'Somos humanos, por isso falhamos'*. Abrevia o raciocínio e prende a atenção.
        *   **Dados e Evidências:** A sustentação factual de um argumento. Deves estruturar o Logos usando o método comparativo, causas e efeitos claros, e estatísticas irrefutáveis provenientes de fontes científicas e académicas de autoridade.
        """)
        
    elif menu_teoria == "2. Estruturação de Textos, Redação e Figuras de Estilo":
        st.header("Módulo II: O Desenho da Palavra Escrita")
        st.write("A escrita oratória difere da escrita puramente académica. Ela é feita para o ouvido, não apenas para o olho. Cada frase deve ter ritmo, cadência e impacto cirúrgico.")
        
        st.image("https://images.unsplash.com/photo-1457369804613-52c61a468e7d?q=80&w=600&auto=format&fit=crop", width=500)
        
        st.subheader("🏛️ A Estrutura Quinquipartite do Discurso Perfeito")
        st.markdown("""
        Um texto de alto impacto divide-se historicamente em cinco partes essenciais que guiam a mente do ouvinte numa jornada lógica:
        
        1.  **Exórdio (A Captura da Atenção):** Os primeiros 30 a 60 segundos determinam o teu sucesso. Proibido usar clichês. Usa um gancho cognitivo: uma pergunta retórica profunda, uma estatística chocante ou um momento de silêncio absoluto focado na plateia.
        2.  **Narratio (A Contextualização):** A exposição breve e clara dos factos do problema. É aqui que desenhas o cenário e preparas o terreno intelectual para os teus argumentos.
        3.  **Argumentatio / Confirmatio (A Prova Técnica):** A apresentação das tuas teses centrais. Aplica a *Regra dos Três*: agrupa os teus argumentos em três grandes blocos fortes. Mais do que três confunde a memória do público; menos parece fraco.
        4.  **Refutatio (A Destruição de Objeções):** Antecipa-te aos teus críticos. Identifica a maior fraqueza da tua proposta e desconstrói-a antes que alguém a use contra ti. Isto demonstra um domínio absoluto do tema e desarma a oposição.
        5.  **Peroratio / Epílogo (A Conclusão Memorável):** O encerramento emocional e definitivo. Divide-se em recapitulação sintética dos pontos e na 'Chamada para a Ação' (Call to Action). Termina com uma frase de efeito concisa e marcante que ecoe na mente da audiência durante dias.
        
        ### ✍️ Figuras de Estilo para uma Escrita Magnética
        *   **Anáfora:** A repetição de uma palavra ou frase no início de orações consecutivas para criar ritmo musical (Ex: *'Nós lutaremos nas praias, nós lutaremos nos campos...'*).
        *   **Tricolon:** Estruturar frases em grupos de três elementos coordenados (Ex: *'Veni, vidi, vici'* - Vim, vi, venci). O cérebro adora padrões triplos.
        *   **Antítese:** Justapor duas ideias opostas para criar um contraste nítido (Ex: *'O esforço é temporário, o legado é eterno'*).
        """)
        
    elif menu_teoria == "3. Técnicas de Palco, Voz, Expressão e Microfone":
        st.header("Módulo III: A Performance Física e Vocal")
        st.write("O conteúdo do teu discurso é apenas o mapa; a tua entrega física e o uso da voz são o veículo que transporta a audiência.")
        
        st.image("https://images.unsplash.com/photo-1475721027785-f74eccf877e2?q=80&w=600&auto=format&fit=crop", width=500)
        
        st.subheader("🗣️ Fisiologia da Voz e Modulação Avançada")
        st.markdown("""
        A voz é um instrumento de sopro mecânico. Oradores amadores falam com a garganta, cansando-se rapidamente; oradores profissionais utilizam a projeção diafragmática.
        *   **Ressonância e Projeção:** Direciona o som para os teus ressonadores faciais (máscara vocal). Isto confere um tom encorpado, grave e autoritário à tua fala.
        *   **A Matriz da Modulação:**
            *   *Velocidade Variável:* Acelera ligeiramente para transmitir entusiasmo, paixão e urgência. Desacelera drasticamente para impor solenidade, respeito e marcar conceitos complexos.
            *   *O Poder Soberano da Pausa:* O silêncio é a ferramenta mais subutilizada na oratória moderna. Uma pausa de 3 segundos *antes* de uma palavra importante cria suspense; uma pausa *depois* permite que o conceito assente e seja digerido pelo público.
        
        ### 🕴️ Cinesiologia e Linguagem Corporal no Palco
        *   **A Âncora Fisiológica:** Mantém os pés firmes, paralelos à linha dos ombros. Não caminhes sem rumo de um lado para o outro de forma repetitiva (o chamado 'efeito leão na jaula'), pois isso projeta ansiedade e falta de controlo espacial. Cada deslocação no palco deve ser intencional e marcar a transição para um novo ponto do discurso.
        *   **Gesticulação Aberta e Concreta:** Mantém as mãos acima da linha da cintura e nunca dentro dos bolsos ou cruzadas atrás das costas. Gestos abertos revelam honestidade. Usa gestos ilustrativos (ex: simular uma linha do tempo com a mão esquerda para o passado e a direita para o futuro).
        *   **Olhar Segmentado (Técnica do Farol):** Não olhes para o teto ou para o chão. Divide a sala em quadrantes visuais e fixa o olhar diretamente nos olhos de uma pessoa específica em cada quadrante por 3 a 4 segundos antes de mudar. Isto cria uma ligação individualizada e mantém toda a sala atenta.
        """)
        
    elif menu_teoria == "4. Gestão de Crise, Combate ao Bloqueio e Resiliência Oratória":
        st.header("Módulo IV: A Psicologia do Autocontrolo sob Alta Pressão")
        st.write("A glotofobia (medo de falar em público) está listada entre os maiores medos da humanidade. O segredo não reside em anular o medo, mas sim em dominar a resposta biológica ao stress.")
        
        st.image("https://images.unsplash.com/photo-1506126613408-eca07ce68773?q=80&w=600&auto=format&fit=crop", width=500)
        
        st.subheader("🚨 Protocolo de Resgate contra Brancos Mentais e Ansiedade")
        st.markdown("""
        Quando o cortisol e a adrenalina disparam, o córtex pré-frontal do teu cérebro pode falhar temporariamente, gerando o famoso 'branco'. Se isto acontecer, aplica a estratégia dos mestres:
        
        *   **A Técnica da Recapitulação Invertida:** Nunca digas 'esqueci-me' ou 'desculpem, estou nervoso'. Isso destrói instantaneamente o teu Ethos. Em vez disso, faz uma pausa intencional, respira pelo nariz, olha para o público com calma e diz com autoridade: *'Para que este ponto fique perfeitamente claro, vale a pena relembrarmos a fundação central que referimos anteriormente...'* – isto dá-te 5 a 10 segundos para o teu cérebro restabelecer as ligações sinápticas do roteiro.
        *   **A Pergunta Defletora:** Transfere a pressão para o público. Faz uma questão aberta provocadora: *'Quantos de vós já se depararam com uma situação semelhante na vossa rotina diária?'*. Enquanto a audiência reflete e levanta as mãos, tu ganhas o tempo necessário para te reposicionares mentalmente.
        
        ### 🌬️ Reprogramação Neurovegetativa Pré-Palco
        Aplica o método de **Respiração Quadrada (Box Breathing)** 5 minutos antes de entrar em cena:
        1.  Inala profundamente pelo nariz expandindo o diafragma durante **4 segundos**.
        2.  Retém o ar nos teus pulmões cheios durante **4 segundos**.
        3.  Exala de forma linear e controlada pela boca durante **4 segundos**.
        4.  Mantém os teus pulmões completamente vazios durante **4 segundos**.
        
        *Repete este ciclo 4 vezes seguidas.* Este protocolo reduz imediatamente os batimentos cardíacos por via do estímulo do nervo vago, limpando o tremor nas mãos e estabilizando o teu tom de voz.
        """)