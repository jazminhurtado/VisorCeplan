import streamlit as st
import pandas as pd
import io
import requests
import re
from fpdf import FPDF

st.set_page_config(page_title="Monitoreo Institucional", layout="wide")
st.image("pe.JPG", width=150)
st.title("Visor Institucional de Monitoreo")
st.markdown("Consulta unificada del estado de los planes PEI–POI y PDC por unidad ejecutora o región.") 

# --- Carga de archivos sin cache ---
def cargar_excel_pei_poi():
    url_excel = "https://github.com/jazminhurtado/monitoreo/raw/first/monitoreoPEI-POI.xlsx"
    response = requests.get(url_excel)
    if response.status_code != 200:
        st.error("No se pudo cargar el archivo PEI–POI desde GitHub.")
        return None
    return pd.read_excel(io.BytesIO(response.content), sheet_name=0)

def cargar_excel_pdc():
    try:
        return pd.read_excel("monitoreoPDC.xlsx", sheet_name="pdc")
    except Exception as e:
        st.error(f"No se pudo cargar el archivo PDC: {e}")
        return None

# --- Funcionalidad del botón recargar datos ---
#if st.button("🔄 Recargar datos desde fuente"):
 #   st.session_state["pei_df"] = cargar_excel_pei_poi()
  #  st.session_state["pdc_df"] = cargar_excel_pdc()

# --- Carga inicial si no existe en session ---
if "pei_df" not in st.session_state:
    st.session_state["pei_df"] = cargar_excel_pei_poi()
if "pdc_df" not in st.session_state:
    st.session_state["pdc_df"] = cargar_excel_pdc()

pei_df = st.session_state["pei_df"]
pdc_df = st.session_state["pdc_df"]

# --- Limpieza de datos ---
def preparar_datos(df, tipo):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
    df['id_ue'] = df['id_ue'].astype(str).str.replace(".0", "", regex=False)
    df['codigo_nombre'] = (
        df['nombre_departamento'].str.upper().fillna("SIN DEPTO") + " - " +
        df['nombre_provincia'].str.upper().fillna("SIN PROV") + " - [" +
        df['id_ue'] + "] " +
        df['nombre_unidad_ejecutora']
    )
    return df

if pei_df is not None:
    pei_df = preparar_datos(pei_df, "PEI–POI")
if pdc_df is not None:
    pdc_df = preparar_datos(pdc_df, "PDC")

# --- Selector de plan ---
plan = st.selectbox("Selecciona el plan a visualizar", ["PEI–POI", "PDC"])

def limpiar_busqueda():
    st.session_state["unidad_seleccionada"] = ""

# --- PEI–POI ---
if plan == "PEI–POI" and pei_df is not None:
  
    opciones = [""] + sorted(pei_df['codigo_nombre'].dropna().unique())
    unidad = st.selectbox("🔍 Buscar o seleccionar unidad ejecutora:", options=opciones, key="unidad_seleccionada")
    st.button("🪑 Limpiar búsqueda", on_click=limpiar_busqueda)

    if unidad:
        codigo_match = re.search(r"\[(\d+)\]", unidad)
        codigo = codigo_match.group(1) if codigo_match else ""
        filtro = pei_df[pei_df['id_ue'] == codigo]
        if not filtro.empty:
            st.subheader("Información PEI disponible:")
            columnas_pei = ['tiene_pei', 'tipo_pei', 'periodo_ultimo_pei', 'pei_vigente', 'estado_pei', 'fase_pei', 'expediente', 'nro_informe_tecnico', 'fecha_informe_tecnico', 'especialista_asignado', 'correo_electronico_especialista']
            for col in columnas_pei:
                if col in filtro.columns and pd.notna(filtro[col].values[0]):
                    st.write(f"**{col.replace('_',' ').capitalize()}:** {filtro[col].values[0]}")

            st.subheader("Información POI disponible:")
            columnas_poi = ['poi_2024_en_seguimiento', 'poi_2025_en_seguimiento', 'poi_2025_en_consistenciado', 'poi_2025_2027_en_elaboración', 'poi_2026_2028_en_elaboración', 'poi_2026_2028_en_aprobado']
            for col in columnas_poi:
                if col in filtro.columns and pd.notna(filtro[col].values[0]):
                    estado = str(filtro[col].values[0]).strip().lower()
                    icono = "✅" if "seguimiento" in estado else "🔆" if "aprobado" in estado else "🟡" if "consistenciado" in estado else "🔴"
                    st.markdown(f"{icono} **{col.replace('_', ' ').capitalize().replace('Poi', 'POI')}:** {filtro[col].values[0]}")

# --- PDC ---
elif plan == "PDC" and pdc_df is not None:
    st.subheader("Visor PDC - Plan de Desarrollo Concertado")

    opciones = [""] + sorted(pdc_df['codigo_nombre'].dropna().unique())
    unidad = st.selectbox("🔍 Buscar o seleccionar unidad ejecutora:", options=opciones, key="unidad_seleccionada")
    st.button("🪑 Limpiar búsqueda", on_click=limpiar_busqueda)

    if unidad:
        codigo_match = re.search(r"\[(\d+)\]", unidad)
        codigo = codigo_match.group(1) if codigo_match else ""
        filtro = pdc_df[pdc_df['id_ue'] == codigo]
        if not filtro.empty:
            st.subheader("Información del PDC")
            columnas_pdc = ['tiene_pdc', 'tipo_pdc', 'periodo_ultimo_pdc', 'pdc_vigente', 'estado_pdc', 'fase_pdc', 'expediente_pdc', 'fecha_informe_tecnico_pdc', 'nro_informe_tecnico_pdc', 'especialista_asignado_pdc', 'correo_electronico_especialista_pdc']
            for col in columnas_pdc:
                if col in filtro.columns and pd.notna(filtro[col].values[0]):
                    st.write(f"**{col.replace('_',' ').capitalize()}:** {filtro[col].values[0]}")

st.markdown("<center><small>App elaborada por la Dirección Nacional de Coordinación y Planeamiento (DNCP) - CEPLAN</small></center>", unsafe_allow_html=True)



