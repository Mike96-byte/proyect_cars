import streamlit as st
import pandas as pd
import plotly_express as px

st.header("Graficas para autos")

car_data = pd.read_csv(
    "vehicles_us.csv")


st.text(car_data.describe())

st.write("Mapa de calor para modelo del año y el tipo de auto")
fig4 = px.density_heatmap(car_data, x="type", y="model_year")
st.plotly_chart(fig4, use_container_width=True)


hist_button = st.button("Construir un histograma")
scatter_button = st.button("Construir un grafico de dispersión")

if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write("Creación de una grafica de dispersion para el conjunto de datos de anuncios de venta de coches")
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)


histogram_check = st.checkbox("Realizar Histograma")
scatter_check = st.checkbox("Realizar Grafico dispersion")


if histogram_check:
    st.write("Creación de histograma para conjunto de datos")
    fig1 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig1, use_container_width=True)
if scatter_check:
    st.write("creación de grafico dispersion")
    fig3 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig3, use_container_width=True)
