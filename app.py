import streamlit as st
import pandas as pd
import plotly_express as px

st.header("Histogramas para autos")

car_data = pd.read_csv(
    r"C:\Users\migue\Documents\proyect_cars\vehicles_us.csv")
hist_button = st.button("Construir un histograma")
scatter_button = st.button("Construir un grafico de dispersión")

# histogram_check=st.checkbox("Realizar Histograma")
# scatter_check=st.checkbox("Realizar Grafico dispersion")

# if histogram_check:
# st.write("Creación de histograma para conjunto de datos")
# fig1=px.histogram(car_data,x="odometer")
# st.plotly_chart(fig1,use_container_width=True)
# if scatter_check:
# st.write("creación de grafico dispersion")
# fig3=px.scatter(car_data,x="odometer")
# st.plotly_chart(fig3,use_container_width=True)


if hist_button:
    st.write(
        "Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:
    st.write("Creación de una grafica de dispersion para el conjunto de datos de anuncios de venta de coches")
    fig2 = px.scatter(car_data, x="odometer")
    st.plotly_chart(fig2, use_container_width=True)
