import streamlit as st

def header_home():
    
    logo_url = 'https://upload.wikimedia.org/wikipedia/commons/f/f5/Jstu_logo.png?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original'
    st.markdown(f"""
        <div>
        <img src ='{logo_url}' style='height:100px';/>
        
    </div>
                
                """, unsafe_allow_html=True)