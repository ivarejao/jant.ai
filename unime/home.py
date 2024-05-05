import streamlit as st

def home():
    st.title("UniMe - Your One-Stop Shop for College Roommate Matching")

    # Idea Section
    st.header("The UniMe Idea")
    st.write("Finding the perfect roommate can be a daunting task for college students. UniMe simplifies the process by connecting you with compatible roommates based on your preferences and lifestyle.")

    # Services Section
    st.header("What We Offer")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Roommate Matching")
        st.write("UniMe uses a sophisticated algorithm to match you with roommates who share your interests, habits, and living style.")
    with col2:
        st.subheader("Housing Options")
        st.write("Explore a wide range of housing options near your university, from dorms and apartments to shared houses.")
    with col3:
        st.subheader("Group Living Benefits")
        st.write("Discover the benefits of group living, such as shared expenses, increased social interaction, and a sense of community.")

    # Why Choose UniMe Section
    st.header("Why Choose UniMe?")
    st.subheader("Here's what sets us apart:")
    metrics = {"Universities Served": 120, "Match Success Rate": 85, "Support Availability": 24/7, "Happy Users": 10000}
    col1, col2 = st.columns(2)
    for metric, value in metrics.items():
        with col1:
            st.write(metric)
        with col2:
            st.write(value)

