import streamlit as st
st.title("basic calculator app")
num1= st.number_input("enter num1")
num2= st.number_input("enter num 2")
operations = st.selectbox(
    "Select an operator",
    ["add", "sub", "multi", "div"]
)
if st.button("submit"):
    if operations=="add":
      result= st.write(num1+num2)
    elif operations=="sub":
      result= st.write(num1-num2)
    elif operations=="multi":
      result= st.write(num1*num2)
    else:
      result= st.write(num1/num2)
