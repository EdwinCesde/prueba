#importar las bibliotecas
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#Leer el archivo csv
#df = pd.read_csv('education.csv')

#Título
st.title("Análisis de datos de educación en Colombia")

#Widget para cargar el archivo
uploaded_file = st.file_uploader("Cargar archivos 'education.csv'", type=["csv"])
#Condicional para leer el archivo
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

#Tabla que muestra los datos del archivo
st.dataframe(df)

#Crear filtros 
st.sidebar.header("Filtros")
nivel_educativo = st.sidebar.multiselect(
    "Nivel educativo", df["Nivel educativo"].unique()
)

carrera = st.sidebar.multiselect("Carrera", df["Carrera"].unique())
institucion = st.sidebar.multiselect("Institución", df["Institución"].unique())

#Mostrar datos filtrados
df_filtrado = df.copy()
if nivel_educativo:
    df_filtrado = df_filtrado[df_filtrado["Nivel educativo"].isin(nivel_educativo)]
if carrera:
    df_filtrado = df_filtrado[df_filtrado["Carrera"].isin(carrera)]
if institucion:
    df_filtrado = df_filtrado[df_filtrado["Institución"].isin(institucion)]

st.dataframe(df_filtrado)

#calcular los datos descriptivos de los filtros
st.subheader("Estadísticas Descriptivas")
st.write(df_filtrado.describe())

#conteo de estudiantes por nivel educativo
st.subheader("Conteo de Estudiantes por nivel educativo")
st.bar_chart(df_filtrado["Nivel educativo"].value_counts())

#Visualizar la distribución de la edad con historigrama
st.subheader("Distribución de la Edad")
#st.histogram(df_filtrado["Edad"], bins = 10)

fig, ax = plt.subplots()
ax.hist(df_filtrado["Edad"], bins=10)

st.pyplot(fig)