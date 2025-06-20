import streamlit as st
import pandas as pd
import unicodedata
import io
from natsort import natsorted
from fpdf import FPDF

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
        st.markdown(f"**Estado:** {mostrar_si_existe('estado')}")
        st.markdown(f"**Periodo:** {mostrar_si_existe('periodo')}")
        st.markdown(f"**Tipo:** {mostrar_si_existe('tipo')}")
        st.markdown(f"**Conductor:** {mostrar_si_existe('conductor')}")
        st.markdown(f"**Problema:** {mostrar_si_existe('problema_publico')}")

        st.markdown("### Formato de descarga")
        formato = st.radio("Selecciona el formato:", ["Excel", "PDF"])

        if st.button("Descargar"):
            if formato == "Excel":
                output = io.BytesIO()
                with pd.ExcelWriter(output, engine='openpyxl') as writer:
                    resultados.to_excel(writer, index=False, sheet_name='Datos')
                output.seek(0)
                st.download_button("Descargar Excel", data=output.getvalue(), file_name='politica_nacional.xlsx', mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            else:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)

                pdf.multi_cell(0, 10, nombre_politica, align="L")
                pdf.cell(0, 10, f"Estado: {mostrar_si_existe('estado')}", ln=True)
                pdf.cell(0, 10, f"Periodo: {mostrar_si_existe('periodo')}", ln=True)
                pdf.cell(0, 10, f"Tipo: {mostrar_si_existe('tipo')}", ln=True)
                pdf.cell(0, 10, f"Conductor: {mostrar_si_existe('conductor')}", ln=True)
                pdf.multi_cell(0, 10, f"Problema: {mostrar_si_existe('problema_publico')}")

                pdf.ln(5)
                pdf.set_font("Arial", 'B', 12)
                pdf.cell(0, 10, "Objetivos Prioritarios y sus Lineamientos", ln=True)
                pdf.set_font("Arial", '', 11)

                op_lineamientos = resultados[
                    resultados['objetivo_prioritario'].notna() & resultados['lineamiento'].notna()
                ][['objetivo_prioritario', 'lineamiento']].drop_duplicates()

                for op in sorted(op_lineamientos['objetivo_prioritario'].unique()):
                    pdf.set_font("Arial", 'B', 11)
                    pdf.multi_cell(0, 10, f"\n{op}")
                    pdf.set_font("Arial", '', 11)
                    lineas = op_lineamientos.loc[
                        op_lineamientos['objetivo_prioritario'] == op, 'lineamiento']
                    for lin in sorted(lineas.unique()):
                        pdf.multi_cell(0, 8, f"- {lin}")

                pdf_output = io.BytesIO()
                pdf_output.write(pdf.output(dest='S').encode('latin1'))
                pdf_output.seek(0)

                st.download_button("Descargar PDF", data=pdf_output, file_name='politica_nacional.pdf', mime='application/pdf')
