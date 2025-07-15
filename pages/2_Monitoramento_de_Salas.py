import streamlit as st
import pandas as pd

st.title("🛏️ Monitoramento das Salas")

df = pd.read_csv("data/dados_ficticios.csv")

uso = df[df["Ocupada"] == "Sim"].groupby(["Data", "Sala"]).size().unstack(fill_value=0)
st.line_chart(uso)