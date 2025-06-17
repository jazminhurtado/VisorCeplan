import streamlit as st

# Configuración mínima oculta para evitar mostrar como página
st.set_page_config(page_title="Redirigiendo...", layout="wide")
st.markdown("<style>header, footer, .stApp {{ visibility: hidden; }}</style>", unsafe_allow_html=True)

# Redirección silenciosa a la página real de inicio
st.switch_page("pages/0_Inicio.py")



