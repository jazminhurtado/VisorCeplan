import streamlit as st

st.set_page_config(page_title="Visor CEPLAN", page_icon="📊", layout="wide")
#st.markdown("# 🏠 Inicio")

st.title("📊 Bienvenido al visor CEPLAN: Consulta Políticas Nacionales, PDC, PEI y POI fácilmente")

st.markdown("""
### Bienvenido al sistema unificado de visores

Desde aquí puedes consultar:
- 📋 PDC, PEI y POI por Unidad Ejecutora
- 🏛️ Políticas Nacionales aprobadas

Utiliza el menú lateral para navegar entre los visores.

---

App elaborada por la **Dirección Nacional de Coordinación y Planeamiento (DNCP)** - CEPLAN
""", unsafe_allow_html=True)

