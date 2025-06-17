import streamlit as st
import pandas as pd
import unicodedata

# =======================
# Cargar y preparar datos
# =======================
@st.cache_data
def load_data():
    return pd.read_excel('matriz_consistencia_pn.xlsx', sheet_name='43aprobadas')

def normalizar(texto):
    if pd.isna(texto):
        return ""
    texto = str(texto)
    texto = unicodedata.normalize('NFKD', texto)
    texto = "".join([c for c in texto if not unicodedata.combining(c)])
    return texto.lower()

df = load_data()
df['nombre_normalizado'] = df['politica_nacional_pn'].apply(normalizar)
df['nro_normalizado'] = df['nro_pn'].astype(str).apply(normalizar)
df['opcion_combo'] = df['nro_pn'].astype(int).astype(str) + " - " + df['politica_nacional_pn']
df_sorted = df.sort_values(by='nro_pn')
opciones = ["-- Selecciona una política --"] + df_sorted['opcion_combo'].drop_duplicates().tolist()

# =======================
# CSS personalizado
# =======================
st.markdown("""
<style>
/* Botón personalizado */
button[kind="secondary"] {
    background-color: #003366 !important;
    color: white !important;
    border: 1px solid #001f33 !important;
    border-radius: 8px !important;
    padding: 6px 14px !important;
    font-size: 12px !important;
    margin-top: 32px !important;
    white-space: nowrap !important;
    transition: all 0.2s ease-in-out;
}
button[kind="secondary"]:hover {
    background-color: #004080 !important;
}

/* Cabecera de Streamlit - SIN línea inferior */
header[data-testid="stHeader"] {
    background-color: white;
    border-bottom: none;
    box-shadow: none;
}

/* Eliminar espacio superior */
.main .block-container {
    padding-top: 1rem;
}

/* Bloque del combo + botón */
.sticky-filter {
    position: sticky;
    top: 70px;
    background-color: white;
    padding-top: 15px;
    padding-bottom: 10px;
    padding-left: 5px;
    z-index: 999;
    border-bottom: 1px solid #ddd;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.04);
}
</style>
""", unsafe_allow_html=True)

# =======================
# Encabezado
# =======================
st.image("pn.jpg", width=80)  
st.title("Visor - Consulta de Políticas Nacionales del Perú")

# =======================
# Selector + Botón Limpiar (Sticky visual)
# =======================
with st.container():
    st.markdown('<div class="sticky-filter">', unsafe_allow_html=True)

    col1, col2 = st.columns([9, 1])
    with col1:
        seleccion = st.selectbox("📑 Consulta una Política Nacional del Perú :", opciones, key="combo")

    with col2:
        if st.button("Limpiar", key="limpiar_btn"):
            if "combo" in st.session_state:
                del st.session_state["combo"]
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# =======================
# Mostrar resultados
# =======================
def mostrar_si_existe(campo):
    valor = primera.get(campo, '')
    return valor if pd.notna(valor) and str(valor).strip() != '' else "No registrado"

if seleccion != "-- Selecciona una política --":
    nro = seleccion.split(" - ")[0].strip()
    resultados = df_sorted[df_sorted['nro_pn'].astype(str) == nro]

    if not resultados.empty:
        nombre_politica = resultados.iloc[0]['politica_nacional_pn']
        primera = resultados.iloc[0]

        st.subheader(f"🟦 {nombre_politica}")

        # Icono visual por estado
        estado_icono = "🟢" if primera.get('estado', '').lower() == "aprobada" else "🟠"

        # Etiqueta visual por tipo de política
        tipo = primera.get('tipo', '—')
        color = "#007ACC" if tipo.lower() == "sectorial" else "#4CAF50" if tipo.lower() == "multisectorial" else "#999999"
        etiqueta_tipo = f"""<span style='background-color:{color}; color:white; padding:4px 10px; border-radius:6px; font-size:13px;'>{tipo}</span>"""

        # Visual en columnas
        colA, colB = st.columns(2)

        with colA:
            st.markdown(f"**Número:** {mostrar_si_existe('nro_pn')}")
            st.markdown(f"**Estado:** {estado_icono} {mostrar_si_existe('estado')}")
            st.markdown(f"**Periodo:** {mostrar_si_existe('periodo')}")
            st.markdown(f"**Marco legal:** {mostrar_si_existe('marco_legal')}")
            st.markdown(f"**Problema Público:** {mostrar_si_existe('problema_publico')}")

        with colB:
            st.markdown(f"**Tipo:** {etiqueta_tipo}", unsafe_allow_html=True)
            st.markdown(f"**Conductor:** {mostrar_si_existe('conductor')}")
            st.markdown(f"**Interviniente:** {mostrar_si_existe('intervinientes')}")
            st.markdown(f"**Informe Técnico CEPLAN:** {mostrar_si_existe('informe_tecnico')}")
            st.markdown(f"**Aprobación Decreto Supremo:** {mostrar_si_existe('decreto_supremo_aprobacion')}")

        # Objetivos Prioritarios
        st.markdown("### 🎯 Objetivos Prioritarios y sus Lineamientos")

        op_lineamientos = resultados[
            resultados['objetivo_prioritario'].notna() & resultados['lineamiento'].notna()
        ][['objetivo_prioritario', 'lineamiento']].drop_duplicates()

        for op in sorted(op_lineamientos['objetivo_prioritario'].unique()):
            st.markdown(f"**🔶 {op}**")
            lineas = op_lineamientos.loc[
                op_lineamientos['objetivo_prioritario'] == op, 'lineamiento'
            ].unique()
            for lin in sorted(lineas):
                st.markdown(f"- {lin}")

        st.markdown("---")

# =======================
# Pie institucional
# =======================
st.markdown("<center><small>App elaborada por la Dirección Nacional de Coordinación y Planeamiento (DNCP) - CEPLAN</small></center>", unsafe_allow_html=True)



