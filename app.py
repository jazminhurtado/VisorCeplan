import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Visor CEPLAN",
    page_icon="📊",
    layout="wide"
)

# Diseño de columnas
col1, col2 = st.columns([1, 6])  # 1 parte para logo, 6 para texto

with col1:
    st.image("cplan.jpg", width=90)  # Reemplaza con el nombre real de tu logo

with col2:
    st.markdown("""
    <h1 style='margin-bottom: 0;'>📊 Bienvenido al visor CEPLAN:</h1>
    <h2 style='margin-top: 0; color: #2c2c2c;'>Consulta Políticas Nacionales, PDC, PEI y POI fácilmente</h2>
    """, unsafe_allow_html=True)

# Texto de bienvenida
st.markdown("""
### Bienvenido al sistema unificado de visores

Desde aquí puedes consultar:

- 📄 PDC, PEI y POI por Unidad Ejecutora  
- 🏛️ Políticas Nacionales aprobadas

Utiliza el menú lateral para navegar entre los visores.

---

App elaborada por la **Dirección Nacional de Coordinación y Planeamiento (DNCP)** - CEPLAN
""")


