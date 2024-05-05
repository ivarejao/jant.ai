import streamlit as st
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import os

# Sample data (replace with your actual dataframe)

def show_n_persons(users : pd.DataFrame, selected_name : str, n : int):
    if not any(users["nome"] == selected_name):
        st.subheader(f"Details of {selected_name}")
        st.dataframe(users[users["nome"] == selected_name])
        selected_index = users[users["nome"] == selected_name].index[0]
    else:
        st.error(f"Pessoa '{selected_name}' não encontrada")
        return 0

    knn = KNeighborsClassifier(n_neighbors=n)
    test_indices = users.index.isin(selected_index)
    train_dataset = users[~test_indices]
    test_dataset = users[test_indices]
    X_train, y_train, X_test, y_test = train_dataset.embedding.tolist(), train_dataset.index, test_dataset.embedding.tolist(), test_dataset.index
    knn.fit(X_train, y_train)

    # Predict the nearest neighbors
    indices = knn.kneighbors(X_test, return_distance=False)
    matches = users.iloc[indices]
    # Print the matched people
    st.subheader("Pessoas linkadas:")
    for _, person in matches.iterrows():
        st.markdown("---")
        st.markdown(f"<div style='border: 1px solid black; border-radius: 10px; padding: 10px;'>")
        st.markdown(f"<p><strong>Name:</strong> {person['nome']}</p>")
        st.markdown(f"<p><strong>Age:</strong> {person['idade']}</p>")
        st.markdown(f"<p><strong>Gender:</strong> {person['genero']}</p>")
        st.markdown(f"<p><strong>Occupation:</strong> {person['ocupacao']}</p>")
        st.markdown(f"</div>")
        st.markdown("---")


def match(data_path : str):

    try:
        users = pd.read_csv(os.path.join(data_path,"users.csv"))
    
        # Function to show N persons
        st.title("Quem é você?")

        # Select person by name
        selected_name = st.selectbox("Quem é você:", users["name"].unique())

        # Input for number of additional people
        num_people = st.number_input("Escolha quantas pessoas você quer dar matching (padrão:1):", min_value=1)

        # Call function to display data
        show_n_persons(users, selected_name, num_people)
    except Exception:
        st.info("Não nenhum usuário registrado ainda. Por favor, registre-se primeiro.")

