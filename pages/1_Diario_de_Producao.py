import streamlit as st
import pandas as pd

st.title("📋 Diário de Produção")

df = pd.read_csv("data/dados_ficticios.csv")

salas = st.multiselect("Selecione a(s) Sala(s):", options=df["Sala"].unique(), default=df["Sala"].unique())

df_filtrado = df[df["Sala"].isin(salas)]

ocupadas = df_filtrado[df_filtrado["Ocupada"] == "Sim"]
total = len(df_filtrado)
taxa_ocup = (len(ocupadas) / total) * 100 if total > 0 else 0

st.metric("Taxa de Ocupação", f"{taxa_ocup:.1f}%")

st.subheader("Produtividade por Profissional")
prod = ocupadas.groupby("Profissional").size().sort_values(ascending=False)
st.bar_chart(prod)

st.subheader("Turno com mais movimento")
turno = ocupadas.groupby("Turno").size()
st.bar_chart(turno)

st.subheader("Cancelamentos e Remarcações")
cancel = df[df["Status"].isin(["Cancelada", "Remarcada"])].groupby(["Profissional", "Status"]).size().unstack(fill_value=0)
st.dataframe(cancel)

st.subheader("Motivos dos Cancelamentos")
motivos = df[df["Status"] == "Cancelada"].groupby("Motivo").size().sort_values(ascending=False)
st.bar_chart(motivos)