import streamlit as st

def home():
    st.title("Junt.ai")

    # Idea Section
    st.header("O Junt.ai")
    st.write("Encontrar o colega de quarto perfeito pode ser uma tarefa difícil para estudantes universitários. UniMe simplifica o processo conectando você com colegas de quarto compatíveis com base em suas preferências e estilo de vida.")

    # Services Section
    st.header("O que oferecemos?")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Matching de colega de quartos")
        st.write("Junt.ai usa um algoritmo sofisticado para combinar você com colegas de quarto que compartilham seus interesses, hábitos e estilo de vida.")
    with col2:
        st.subheader("Opções de habitação")
        st.write("Explore uma ampla variedade de opções de hospedagem perto da sua universidade, desde dormitórios e apartamentos até casas compartilhadas.")
    with col3:
        st.subheader("Benefícios de vida em grupo")
        st.write("Descubra os benefícios da vida em grupo, como despesas compartilhadas, maior interação social e senso de comunidade.")

    # Why Choose UniMe Section
    st.header("Por que escolher a Junt.ai?")
    st.subheader("Aqui está o que nos diferencia:")
    metrics = {"Taxa de sucesso do Match": 85, "Disponibilidade de suporte": 24/7, "Usuários felizes": 10000}
    col1, col2 = st.columns(2)
    for metric, value in metrics.items():
        with col1:
            st.write(metric)
        with col2:
            st.write(value)

