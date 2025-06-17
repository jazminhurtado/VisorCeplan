import streamlit as st

st.set_page_config(page_title="Visor CEPLAN", page_icon="📊", layout="wide")

# Mostrar logo CEPLAN centrado
st.markdown("""
<div style='text-align: center;'>
    <img src='https://raw.githubusercontent.com/jazminhurtado/VisorCeplan/main/ceplan.jpg' width='260'>

</div>
""", unsafe_allow_html=True)

# Título principal centrado
st.markdown("""
<h1 style='text-align: center;'> Bienvenido al visor <strong>CEPLAN</strong>:</h1>
<h2 style='text-align: center;'>Consulta Políticas Nacionales, PDC, PEI y POI fácilmente</h2>
""", unsafe_allow_html=True)

# Subtítulo y contenido
st.markdown("""
### Bienvenido al sistema unificado de visores

Desde aquí puedes consultar:

- 🗂️ PDC, PEI y POI por Unidad Ejecutora  
- 🏛️ Políticas Nacionales aprobadas

Utiliza el menú lateral para navegar entre los visores.

---

App elaborada por la **Dirección Nacional de Coordinación y Planeamiento (DNCP)** – CEPLAN
""")





