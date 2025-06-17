import streamlit as st

# Logo CEPLAN arriba, centrado
st.image("cplan.JPG", width=190)

# Título debajo del logo
st.markdown("<h1 style='text-align: center;'>📊 Bienvenido al visor <strong>CEPLAN</strong>:</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>Consulta Políticas Nacionales, PDC, PEI y POI fácilmente</h2>", unsafe_allow_html=True)

# Subtítulo
st.markdown("""
### Bienvenido al sistema unificado de visores

Desde aquí puedes consultar:
- 🗂️ PDC, PEI y POI por Unidad Ejecutora
- 🏛️ Políticas Nacionales aprobadas

Utiliza el menú lateral para navegar entre los visores.

---

App elaborada por la **Dirección Nacional de Coordinación y Planeamiento (DNCP)** – CEPLAN
""")



