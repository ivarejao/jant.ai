import streamlit as st
import pandas as pd
import os
from PIL import Image
import io
import cohere
from dotenv import load_dotenv

def get_embedding(composed_string : str):
    load_dotenv()
    # Load the dataset
    co = cohere.Client(os.environ["COHERE_API_KEY"])

    response = co.embed(
        texts=[composed_string],
        model="embed-multilingual-v3.0",
        input_type="classification",
    )
    return response.embeddings

def register(data_path):
    st.title("Registro em Junt.ai")
    st.subheader("Crie seu perfil para encontrar o colega de quarto perfeito!")

    # Registration Form
    name = st.text_input("Nome")
    age = st.number_input("Idade", step=1, format="%d", min_value=18, max_value=100)
    area = st.text_input("Área de atuação")
    university = st.text_input("Universidade")
    essay = st.text_area("Conte-nos sobre você")
    profile_image = st.file_uploader("Faça um upload de você", type=["jpg", "png", "jpeg"], accept_multiple_files=False)

    submit = st.button("Registrar")
    
    user_data_path = os.path.join(data_path, 'users.csv')
    if submit:
        # Save image
        image_path = os.path.join(data_path, "images", f"{name}_profile.jpg")
        image = Image.open(io.BytesIO(profile_image.getvalue()))
        image.save(image_path)
        
        # Create a DataFrame from user data
        user_data = pd.DataFrame({
            "nome": [name],
            "idade": [age],
            "area": [area],
            "universidade": [university],
            "minibio": [essay],
            "image_path": image_path
        })
        # Ensure that the fields are lowercase
        user_data["area"] = user_data["area"].str.lower()
        user_data["universidade"] = user_data["universidade"].str.lower()
        user_data["composed"] = "Area: " + user_data["area"] + "; Universidade: " + user_data["universidade"] + "; Minibio: " + user_data["minibio"] + ";"
        user_data["embedding"] = get_embedding(user_data["composed"].iloc[0])
        # Check if CSV file exists, create it if not
        if not os.path.exists(user_data_path):
            user_data.to_csv(user_data_path, index=False)  # Save without index column
        else:   
            # Append new data to existing CSV using Pandas
            existing_data = pd.read_csv(user_data_path)

            # Create composed string
            updated_data = pd.concat([existing_data, user_data], ignore_index=True)            
            updated_data.to_csv(user_data_path, index=False)  # Save without index column

        st.success("Registro concluído com sucesso!")
