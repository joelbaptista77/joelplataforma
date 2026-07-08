import streamlit as st

# Configuração da página (Deve ser a primeira linha)
st.set_page_config(page_title="Academia de Retórica", page_icon="🎙️", layout="wide")

# Script para ativação da PWA (Aplicação Móvel sem anúncios)
st.components.v1.html(
    """
    <script>
        var link = parent.document.createElement('link');
        link.rel = 'manifest';
        link.href = './manifest.json';
        parent.document.head.appendChild(link);

        if ('serviceWorker' in navigator) {
            parent.navigator.serviceWorker.register('./sw.js');
        }
    </script>
    """,
    height=0
)

# Inicialização do estado da navegação
if "pagina" not in st.session_state:
    st.session_state.pagina = "Início"

# Barra Lateral de Navegação Limpa
st.sidebar.title("Menu Principal")
if st.sidebar.button("📚 Teoria e Técnicas"):
    st.session_state.pagina = "Início"
if st.sidebar.button("🧠 Treino de Quiz"):
    st.session_state.pagina = "Quiz"

# Carregamento dinâmico dos módulos
if st.session_state.pagina == "Início":
    import conteudo
    conteudo.exibir_conteudo()
elif st.session_state.pagina == "Quiz":
    import quiz
    quiz.exibir_quiz()