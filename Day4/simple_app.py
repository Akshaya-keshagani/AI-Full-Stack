import streamlit as st
st.title("Welcome to my app")
st.header("this is My 1st app")
name = st.text_input("",placeholder="Enter your name:")
if st.button("Click me"):
    st.write("Hello, ", name)
name = st.chat_input("Type here:")