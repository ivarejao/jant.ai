from argparse import ArgumentParser, Namespace
import streamlit as st

from jantai import home, register, match

def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument('data-path', help='')

    args = parser.parse_args()
    return args

def app(data_path : str):
    # Call the appropriate page function based on user selection
    page_list = ["Homepage", "Registro", "Match me"]
    selected_page = st.sidebar.radio("Selecione a página", page_list)

    if selected_page == "Homepage":
        home()
    elif selected_page == "Registro":
        register(data_path)
    elif selected_page == "Match me":
        match(data_path)

    # Optional styling for a list-like appearance
    st.sidebar.markdown("---")  # Add a separator line
    for page in page_list:
        if page == selected_page:
            st.sidebar.markdown(f"- **{page}**")  # Bold the selected page
        else:
            st.sidebar.markdown(f"- {page}")


if __name__ == "__main__":
    # args = parse_args()
    app("data/")

