
import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Visor CEPLAN",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título visual grande en la página
st.markdown("# 🏠 Inicio")

# Subtítulo y contenido
st.title("📊  Bienvenido(a) al visor CEPLAN: consulta PEI, POI, PDC y Políticas Nacionales fácilmente")

st.markdown("""
### Bienvenido al sistema unificado de visores

Desde aquí puedes consultar:
- 📋 PEI, POI y PDC por Unidad Ejecutora
- 🏛️ Políticas Nacionales aprobadas

Utiliza el menú lateral para navegar entre los visores.

---

<center><small>App elaborada por la **Dirección Nacional de Coordinación y Planeamiento (DNCP)** - CEPLAN</small></center>
""", unsafe_allow_html=True)
