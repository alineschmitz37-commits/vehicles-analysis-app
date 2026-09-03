import pandas as pd
import plotly.express as px
import streamlit as st

# Título do aplicativo web
st.header('Análise de Anúncios de Vendas de Veículos')

# Carregar os dados
car_data = pd.read_csv('vehicles_us.csv')

# Preencher valores ausentes do odômetro com a mediana (igual ao EDA)
car_data['odometer'] = car_data['odometer'].fillna(car_data['odometer'].median())

# Criar caixas de seleção (checkboxes) para os gráficos
build_histogram = st.checkbox('Criar um histograma')
build_scatter = st.checkbox('Criar um gráfico de dispersão')

# Lógica para exibir o histograma
if build_histogram:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Lógica para exibir o gráfico de dispersão
if build_scatter:
    st.write('Criando um gráfico de dispersão (preço vs odômetro)')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)