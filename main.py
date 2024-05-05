import streamlit as st

from unime import home, register, marketplace

# Call the appropriate page function based on user selection
page_list = ["Homepage", "Register", "Marketplace"]
selected_page = st.sidebar.radio("Select a Page", page_list)

if selected_page == "Homepage":
    home()
elif selected_page == "Register":
    register()
elif selected_page == "Marketplace":
    marketplace()

# Optional styling for a list-like appearance
st.sidebar.markdown("---")  # Add a separator line
for page in page_list:
    if page == selected_page:
        st.sidebar.markdown(f"- **{page}**")  # Bold the selected page
    else:
        st.sidebar.markdown(f"- {page}") 

