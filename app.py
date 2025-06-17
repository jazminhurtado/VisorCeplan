# Esto hace que app.py no muestre nada como página
import os
import streamlit as st

# Oculta todos los elementos visuales por si acaso
st.set_page_config(page_title="Redirigiendo...", layout="wide")
st.markdown("<style>main, header, footer {display: none !important;}</style>", unsafe_allow_html=True)

# Redirige silenciosamente
st.switch_page("pages/0_Inicio.py")



