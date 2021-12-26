import streamlit as st

st.write("Hello World")

@st.cache
def foo():
    return 3

@st.cache
def foo2():
    return 3

st.write(foo())
foo2()

print("🎈")