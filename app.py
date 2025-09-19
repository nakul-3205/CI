# app.py
import streamlit as st

def square(n):
    return n ** 2

st.title('calc')
st.write('Enter a number')
n = st.number_input('Enter an int', value=1, step=1)

sq = square(n)
st.write(sq)
