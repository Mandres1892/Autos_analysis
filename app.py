import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('data/vehicles_us.csv')

st.title('Autos Analysis')
st.caption('Esta app tiene como fin mostrar un analisis realizado para un datframe que contiene un conjunto de datos de anuncios de venta de coches.')
st.divider()

hist_button = st.button('Construir histograma')



if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

st.divider()
scatter_button = st.button('Construir Grafico de dispersión')
if scatter_button:
    st.write('Creación de un grafico de dispersión analizando la venta de coches')
    fig_1 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_1, use_container_width=True)


st.divider()
build_check = st.checkbox('Distribucion de precios')
    
if build_check:
    st.write('Creacion de un histograma para analizar distribución de precios de los autos reportados')
    fig_2 = px.histogram(car_data['price'])
    st.plotly_chart(fig_2, use_container_width=True)