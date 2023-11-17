import streamlit as st

def set_padding(padding):
    return st.markdown(f"""
    <div style="height: {str(padding)}px; width: 2px;">
  </div>
""", unsafe_allow_html=True)