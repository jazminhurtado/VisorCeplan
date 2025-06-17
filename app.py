import streamlit as st

# Configurar la página
st.set_page_config(page_title="Visor CEPLAN", page_icon="📊", layout="wide")

# CSS personalizado para sidebar estilo CEPLAN
st.markdown("""
    <style>
    /* Fondo general del sidebar */
    [data-testid="stSidebar"] {
        background-color: #C8102E;
    }

    /* Texto normal del sidebar */
    [data-testid="stSidebar"] a {
        color: white;
        font-weight: bold;
        text-decoration: none;
    }

    /* Estilo del ítem activo del menú */
    [data-testid="stSidebar"] a[aria-current="page"] {
        background-color: #A50E24;  /* Rojo oscuro */
        color: white !important;
        border-radius: 10px;
        padding: 8px 15px;
        font-weight: bold;
        text-decoration: none;
    }

    /* Título personalizado encima del menú */
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
""", unsafe_allow_html=True)

# Mostrar logo CEPLAN centrado
st.markdown("""
<div style='text-align: center;'>
    <img src='https://raw.githubusercontent.com/jazminhurtado/VisorCeplan/main/ceplan.jpg' width='160'>
</div>
""", unsafe_allow_html=True)

# Título principal
st.markdown("""
<h1 style='text-align: center;'>📊 Bienvenido al visor <strong>CEPLAN</strong></h1>
<h2 style='text-align: center;'>Consulta Políticas Nacionales, PDC, PEI y POI fácilmente</h2>
""", unsafe_allow_html=True)

# Contenido principal
st.markdown("""
### Bienvenido al sistema unificado de visores

Desde aquí puedes consultar:

- 📁 PDC, PEI y POI por Unidad Ejecutora  
- 📌 Políticas Nacionales aprobadas  

Utiliza el menú lateral para navegar entre los visores.

---

App elaborada por la **Dirección Nacional de Coordinación y Planeamiento (DNCP)** – CEPLAN
""")



