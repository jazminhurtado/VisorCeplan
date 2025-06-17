import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Visor CEPLAN", page_icon="📊", layout="wide")

# Estilos generales (opcional)
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Logo CEPLAN
st.markdown("""
<div style='text-align: center; margin-bottom: 10px;'>
    <img src='https://raw.githubusercontent.com/jazminhurtado/VisorCeplan/main/ceplan.jpg' width='160'>
</div>
""", unsafe_allow_html=True)

# Encabezado
st.markdown("""
<div style='text-align: center;'>
    <h1 style='font-size: 42px;'>📊 Visor CEPLAN</h1>
    <p style='font-size: 22px; font-weight: bold;'>Consulta Políticas Nacionales, PDC, PEI y POI fácilmente</p>
    <hr style='border: 1px solid #C8102E; width: 50%; margin: auto;'>
</div>
""", unsafe_allow_html=True)

# Tabs de contenido
tab1, tab2 = st.tabs(["📁 PEI POI PDC", "🏛️ Políticas Nacionales"])

with tab1:
    st.subheader("PEI, POI y PDC por Unidad Ejecutora")
    st.write("Aquí puedes integrar la visualización de los datos de los planes. Por ejemplo:")
    # Aquí puedes cargar tu archivo o DataFrame
    # st.dataframe(df_pei_poi)

with tab2:
    st.subheader("Políticas Nacionales Aprobadas")
    st.write("Aquí se muestran las políticas nacionales aprobadas:")
    # Aquí puedes cargar tu archivo o visualización
    # st.dataframe(df_politicas)

# Pie de página
st.markdown("""
---
App elaborada por la **Dirección Nacional de Coordinación y Planeamiento (DNCP)** – CEPLAN
""")





