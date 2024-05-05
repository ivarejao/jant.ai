import streamlit as st
import os
import pandas as pd

DATA_PATH = "/home/imsvarejao/UniMe/data/"

def marketplace():
    st.title("Explore Housing Options")
    st.subheader("Find your perfect place to live with compatible roommates")

    users = pd.read_csv(DATA_PATH + "user.csv")

    # Display housing options with image, description, and interest meter
    for i, user in users.iterrows():
        col1, col2 = st.columns(2)
        with col1:
            st.image(user["image_path"])
        with col2:
            st.subheader(user["age"])
            progress_bar = st.progress(user["age"])
            # st.write(f"{user['age']}% Interested")

