import streamlit as st

# Import your pages

def main():
    st.title("Retail Analytics")

    # Get the current page from query parameter
    signup_page()

# Sign-up Page
def signup_page():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    email = st.text_input("Email")

    if st.button("Login"):
        if username and password and email:
            st.success("Login Successful!")

            # Redirect to search page
            st.experimental_set_query_params(page="search")
            st.experimental_rerun()  # Rerun the script to load the search page
        else:
            st.error("Please fill out all fields")

if __name__ == "__main__":
    main()