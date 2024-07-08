import streamlit as st
import pandas as pd
import plotly_express as px

st.header("Graficas para autos")

car_data = pd.read_csv(
    "vehicles_us.csv")


car_data

st.header("Comparación de los precios promedio de acuerdo al combustible")

type_group = car_data.groupby(["fuel", "cylinders"])[
    "price"].mean().reset_index()

fig4 = px.bar(type_group, x="fuel", y="price", color="fuel")
st.plotly_chart(fig4, use_container_width=True)


min_odometer, max_odometer = car_data["odometer"].min(
), car_data["odometer"].max()
kilometers = st.slider(
    "Selecciona el rango de kilometros", min_odometer, max_odometer, value=(min_odometer, max_odometer))

tab1, tab2, tab3 = st.tabs(["Histogram", "Scatter", "Scatter_model"])


filter_car = car_data[(car_data["odometer"] >= kilometers[0]) & (
    car_data["odometer"] <= kilometers[1])]

with tab1:
    st.header("Histograma para los diferentes kilometrajes")
    fig = px.histogram(filter_car, x="odometer", range_x=[
                       kilometers[0], kilometers[1]])
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.header(
        "Creación de una grafica de dispersion para el conjunto de datos de anuncios de venta de coches")
    fig2 = px.scatter(filter_car, x="odometer", y="price",
                      color="fuel", range_x=[kilometers[0], kilometers[1]])
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.header("Diferentes precios por modelo de auto")
    fig9 = px.scatter(filter_car, x="model_year", y="price",
                      color="type")
    st.plotly_chart(fig9)


st.header("Grafica de Pie para saber los porcentajes de las condiciones de los autos")

fig5 = px.pie(car_data, "condition")
st.plotly_chart(fig5)

st.header("Diagrama de cajas para ver los días que están en lista")

fig6 = px.box(car_data, x="type", y="days_listed")
st.plotly_chart(fig6, use_container_width=True)


st.header(
    "Grafica para ver los diferentes precios de acuerdo a los cilindros del auto")
fig7 = px.funnel(type_group, x="cylinders", y="price")
st.plotly_chart(fig7, use_container_width=True)


st.header("Vamos a ver los kilometrajes y su transmisión")

fig8 = px.box(car_data, x="transmission", y="odometer", color="transmission")
st.plotly_chart(fig8, use_container_width=True)


correlacion = car_data.corr(numeric_only=True)

st.header("Correlación para los datos númericos")
correlacion
