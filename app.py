import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Visor CEPLAN", page_icon="📊", layout="wide")

# Estilos personalizados para el menú lateral CEPLAN
st.markdown(
    """
    <style>
    /* Fondo general del sidebar */
    [data-testid="stSidebar"] {
        background-color: #C8102E;
    }

    /* Texto general en el menú */
    [data-testid="stSidebar"] .css-1v3fvcr,
    [data-testid="stSidebar"] .css-eww8gc,
    [data-testid="stSidebar"] .css-10trblm {
        color: white;
        font-weight: bold;
    }

    /* Elemento activo (seleccionado) */
    [data-testid="stSidebar"] .css-1v3fvcr:hover,
    [data-testid="stSidebar"] .css-1v3fvcr:focus,
    [data-testid="stSidebar"] .css-1v3fvcr:active,
    [data-testid="stSidebar"] .css-1v3fvcr[aria-selected="true"] {
        background-color: #A50E24 !important;
        color: white !important;
    }

    /* Título encima del menú */
    [data-testid="stSidebarNav"]::before {
        content: "VISOR CEPLAN";
        font-size: 20px;
        font-weight: bold;
        color: white;
        padding-left: 20px;
        display: block;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Mostrar logo CEPLAN centrado
st.markdown("""
<div style='text-align: center;'>
    <img src='https://raw.githubusercontent.com/jazminhurtado/VisorCeplan/main/ceplan.jpg' width='160'>
</div>
""", unsafe_allow_html=True)

# Título principal centrado
st.markdown("""
<h1 style='text-align: center;'>📊 Bienvenido al visor <strong>CEPLAN</strong></h1>
<h2 style='text-align: center;'>Consulta Políticas Nacionales, PDC, PEI y POI fácilmente</h2>
""", unsafe_allow_html=True)

# Subtítulo y contenido
st.markdown("""
### Bienvenido al sistema unificado de visores

Desde aquí puedes consultar:

- 📁 PDC, PEI y POI por Unidad Ejecutora  
- 📌 Políticas Nacionales aprobadas  

Utiliza el menú lateral para navegar entre los visores.

---

App elaborada por la **Dirección Nacional de Coordinación y Planeamiento (DNCP)** – CEPLAN
""")


