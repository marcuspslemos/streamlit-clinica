import streamlit as st
import pandas as pd

st.title("💰 Faturamento")

df = pd.read_csv("data/dados_ficticios.csv")
realizados = df[df["Status"] == "Realizada"]

st.subheader("Total Faturado")
st.metric("R$", f"{realizados['Valor'].sum():,.2f}")

st.subheader("Por Profissional")
st.bar_chart(realizados.groupby("Profissional")["Valor"].sum())

st.subheader("Por Plano de Saúde")
st.bar_chart(realizados.groupby("Plano")["Valor"].sum())

st.subheader("Por Forma de Pagamento")
st.bar_chart(realizados.groupby("Forma_Pagamento")["Valor"].sum())