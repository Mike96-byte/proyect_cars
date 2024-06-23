import pandas as pd
import streamlit as st
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

hist_button = st.button("Creación de Histograma")
scatter_button = st.button("Creación de Grafica de Dispersion")

if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de ventas de coches")
    fig1 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write("creación de grafica de dispersion para el conjunto de datos de anuncios de ventas de coches")
    fig2 = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig2, use_container_widht=True)

check_hist = st.checkbox("Realizar Histograma")
check_scatter = st.checkbox("Realizar Grafica de dispersión")

if check_hist:
    st.write(
        "Creación de Histograma para el conjunto de datos de anuncios de ventas de coches")
    fig3 = px.hist(car_data, x="odometer")
    st.plotly_chart(fig3, use_container_width=True)

if check_scatter:
    st.write("Cración de grafica de dispersion para el conjunto de datos de anuncios de ventas de coches")
    fig4 = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig4, use_container_widht=True)
