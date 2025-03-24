import pandas as pd
import plotly.express as px
import streamlit as st

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')
car_data.columns = car_data.columns.str.strip()  # Eliminar espacios invisibles

# Encabezado de la app
st.title("Análisis interactivo de anuncios de autos en venta 🚗")

# Filtro por modelo con opción "Todos"
model_options = ['Todos'] + sorted(car_data['model'].dropna().unique().tolist())
selected_model = st.selectbox('Selecciona un modelo:', model_options)

# Aplicar filtro solo si se seleccionó un modelo específico
if selected_model == 'Todos':
    filtered_data = car_data
else:
    filtered_data = car_data[car_data['model'] == selected_model]

# Mostrar cantidad de autos filtrados
st.write(f"Se encontraron **{len(filtered_data)}** autos del modelo `{selected_model}`.")

# Checkbox para histograma
if st.checkbox('Mostrar histograma de odómetro'):
    st.write('Histograma de odómetro')
    fig = px.histogram(filtered_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para diagrama de dispersión
if st.checkbox('Mostrar diagrama de dispersión precio vs año'):
    st.write('Diagrama de dispersión entre precio y año')
    fig = px.scatter(filtered_data, x='model_year', y='price', color='transmission')
    st.plotly_chart(fig, use_container_width=True)
