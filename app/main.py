import streamlit as st
import os

st.title("Hi from streamlit inside docker")
st.write("looks like this works properly.")
st.write("Env Test", os.getenv('TEST_ENV'))
st.write(print(os.environ))
