import streamlit as st

def home_screen():
    st.header('Home Screen')
    col1, col2 = st.columns(2)
    
    with col1:
        st.button('Teacher Portal')
        
    with col2:
        st.button('Student Portal')