import streamlit as st

st.set_page_config(page_title="Visor CEPLAN", page_icon="📊", layout="wide")

# CSS funcional para multipágina real
st.markdown("""
    <style>
    /* Fondo del sidebar */
    [data-testid="stSidebar"] {
        background-color: #C8102E;
    }

    /* Título superior personalizado */
    [data-testid="stSidebarNav"]::before {
        content: "VISOR CEPLAN";
        font-size: 20px;
        font-weight: bold;
        color: white;
        padding-left: 20px;
        display: block;
        margin-bottom: 20px;
    }

    /* Texto y enlaces normales del menú */
    section[data-testid="stSidebarNav"] ul li a {
        color: white;
        text-decoration: none;
        font-weight: bold;
    }

    /* Ítem seleccionado (actúa sobre el span dentro del link) */
    section[data-testid="stSidebarNav"] ul li span {
        background-color: #A50E24 !important;
        color: white !important;
        padding: 8px 14px;
        border-radius: 10px;
        display: block;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Logo CEPLAN
st.markdown("""
<div style='text-align: center;'>
    <img src='https://raw.githubusercontent.com/jazminhurtado/VisorCeplan/main/ceplan.jpg' width='160'>
</div>
""", unsafe_allow_html=True)

# Título
st.markdown("""
<h1 style='text-align: center;'>📊 Bienvenido al visor <strong>CEPLAN</strong></h1>
<h2 style='text-align: center;'>Consulta Políticas Nacionales, PDC, PEI y POI fácilmente</h2>
""", unsafe_allow_html=True)

# Cuerpo
st.markdown("""
### Bienvenido al sistema unificado de visores

Desde aquí puedes consultar:

- 📁 PDC, PEI y POI por Unidad Ejecutora  
- 📌 Políticas Nacionales aprobadas  

Utiliza el menú lateral para navegar entre los visores.

---

App elaborada por la **Dirección Nacional de Coordinación y Planeamiento (DNCP)** – CEPLAN
""")




