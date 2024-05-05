import streamlit as st
import pandas as pd
import os
from PIL import Image
import io

DATA_PATH = "/home/imsvarejao/UniMe/data/"

def register():
    st.title("Register for UniMe")
    st.subheader("Create your profile to find your perfect roommate match")

    # Registration Form
    name = st.text_input("Name")
    age = st.number_input("Age", step=1, format="%d", min_value=18, max_value=100)
    location = st.text_input("Location (City)")
    university = st.text_input("University")
    essay = st.text_area("Tell us a bit about yourself (hobbies, interests, lifestyle preferences)")
    profile_image = st.file_uploader("Upload Profile Image", type=["jpg", "png", "jpeg"], accept_multiple_files=False)

    submit = st.button("Register")

    user_data_path = os.path.join(DATA_PATH, 'user.csv')
    if submit:
        # Save image
        image_path = os.path.join(DATA_PATH, "images", f"{name}_profile.jpg")
        image = Image.open(io.BytesIO(profile_image.getvalue()))
        image.save(image_path)
        
        # Create a DataFrame from user data
        user_data = pd.DataFrame({
            "name": [name],
            "age": [age],
            "location": [location],
            "university": [university],
            "essay": [essay],
            "image_path": image_path
        })

        # Check if CSV file exists, create it if not
        if not os.path.exists(user_data_path):
            user_data.to_csv(user_data_path, index=False)  # Save without index column
        else:
            # Append new data to existing CSV using Pandas
            existing_data = pd.read_csv(user_data_path)
            combined_data = pd.concat([existing_data, user_data], ignore_index=True)
            combined_data.to_csv(user_data_path, index=False)  # Save without index column

        st.success("Registration Successful! You'll be notified when we find a good match for you.")
