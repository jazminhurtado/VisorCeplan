import streamlit as st
import pandas as pd
import unicodedata
import io
from natsort import natsorted
from fpdf import FPDF

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
df['nro_pn'] = df['nro_pn'].astype(str).str.strip()
df['nro_normalizado'] = df['nro_pn'].apply(normalizar)
df['opcion_combo'] = df['nro_pn'] + " - " + df['politica_nacional_pn']
df_sorted = df.loc[natsorted(df.index, key=lambda i: df.loc[i, 'nro_pn'])]
opciones = ["-- Selecciona una política --"] + df_sorted['opcion_combo'].drop_duplicates().tolist()

# =======================
# UI
# =======================
st.title("Visor - Consulta de Políticas Nacionales del Perú")
seleccion = st.selectbox("Selecciona una política:", opciones)

def mostrar_si_existe(campo):
    valor = primera.get(campo, '')
    return valor if pd.notna(valor) and str(valor).strip() != '' else "No registrado"

if seleccion != "-- Selecciona una política --":
    nro = seleccion.split(" - ")[0].strip()
    resultados = df_sorted[df_sorted['nro_pn'].astype(str) == nro]

    if not resultados.empty:
        nombre_politica = resultados.iloc[0]['politica_nacional_pn']
        primera = resultados.iloc[0]

        st.subheader(f"\U0001F4D6 {nombre_politica}")

        estado_icono = "🟢" if primera.get('estado', '').lower() == "aprobada" else "🟠"
        tipo = primera.get('tipo', '—')
        color = "#007ACC" if tipo.lower() == "sectorial" else "#4CAF50" if tipo.lower() == "multisectorial" else "#999999"
        etiqueta_tipo = f"<span style='background:{color}; color:white; padding:4px 10px; border-radius:6px; font-size:13px;'>{tipo}</span>"

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

        # =======================
        # Descarga
        # =======================
        st.markdown("### 📥 Formato de descarga:")
        formato = st.radio("Selecciona el formato:", ["Excel", "PDF"], index=0)

        if st.button("Descargar"):
            if formato == "Excel":
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    resultados.to_excel(writer, index=False, sheet_name='Datos')
                output.seek(0)
                st.download_button("Descargar Excel", data=output.getvalue(), file_name='politica_nacional.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

            elif formato == "PDF":
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                pdf.multi_cell(0, 10, f"Política Nacional: {nombre_politica}")
                campos = [
                    ("Estado", 'estado'),
                    ("Periodo", 'periodo'),
                    ("Tipo", 'tipo'),
                    ("Conductor", 'conductor'),
                    ("Interviniente", 'intervinientes'),
                    ("Informe Técnico", 'informe_tecnico'),
                    ("Decreto Supremo", 'decreto_supremo_aprobacion'),
                    ("Problema Público", 'problema_publico'),
                    ("Marco legal", 'marco_legal')
                ]
                for label, key in campos:
                    pdf.multi_cell(0, 10, f"{label}: {mostrar_si_existe(key)}")

                pdf.ln(5)
                pdf.set_font("Arial", style="B", size=12)
                pdf.cell(0, 10, "Objetivos Prioritarios y Lineamientos", ln=True)
                pdf.set_font("Arial", size=11)
                for op in sorted(op_lineamientos['objetivo_prioritario'].unique()):
                    pdf.multi_cell(0, 10, f"\n🔶 {op}")
                    lineas = op_lineamientos.loc[op_lineamientos['objetivo_prioritario'] == op, 'lineamiento'].unique()
                    for lin in sorted(lineas):
                        pdf.multi_cell(0, 10, f" - {lin}")

                pdf_output = pdf.output(dest='S').encode('latin-1')
                st.download_button("Descargar PDF", data=pdf_output, file_name='politica_nacional.pdf', mime='application/pdf')

# Pie institucional
st.markdown("<center><small>App elaborada por la Dirección Nacional de Coordinación y Planeamiento (DNCP) - CEPLAN</small></center>", unsafe_allow_html=True)
