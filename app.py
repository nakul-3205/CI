import streamlit as st


st.title('calc')
st.write('enter a num')
n=st.number_input('enter an int',value=1,step=1)

sq=n**2
st.write(sq)