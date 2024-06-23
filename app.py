import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button("Creación de Histograma")
scatter_button = st.button("Creación de Grafica de Dispersion")

if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de ventas de coches")
    fig = st.hist(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write("creación de grafica de dispersion para el conjunto de datos de anuncios de ventas de coches")
    fig2 = st.scatter(car_data, x="odometer")
    st.plotly_chart(fig2, use_container_widht=True)
