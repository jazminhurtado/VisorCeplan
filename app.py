import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Visor CEPLAN", page_icon="📊", layout="wide")

# Personalización del menú lateral con color rojo CEPLAN
st.markdown(
    """
    <style>
    /* Fondo del sidebar */
    [data-testid="stSidebar"] {
        background-color: #C8102E; /* Rojo CEPLAN */
    }

    /* Color y estilo del texto en el sidebar */
    [data-testid="stSidebar"] .css-1v3fvcr, [data-testid="stSidebar"] .css-eww8gc {
        color: white;
        font-weight: bold;
    }

    /* Cambiar "app" por título personalizado */
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

