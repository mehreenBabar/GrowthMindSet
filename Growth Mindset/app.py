# Python Website With Streamlitpytho

import streamlit as st

# Title and Header
st.title("My Python Website")
st.header("Get User Information")

# Adding Some Text
st.write("This is a simple Python website with Streamlit to add user data")

# Adding a Button
if st.button("Click the Button"):
   st.write("Thankyou for clicking the button !")

# Adding User Input
name = st.text_input("What is your name?")
if st.button("Result"):
   st.write(f"Hi!, {name} Welcome to my Website !")
