import matplotlib.pyplot as plt
import numpy as np  
import pandas as pd
import seaborn as sns 

# Carregando a base de dados e informações iniciais
df = pd.read_csv("Base Varejo.csv", sep=";")

print("Número de registros:", df.shape[0])
print("Número de colunas:", df.shape[1])

print("\nPrimeiros registros:")
print(df.head())

print("\nColunas da base:")
print(df.columns)

print("\nTipos de dados:")
print(df.dtypes)

print("\nInformações gerais da base:")
df.info()

#Limpeza, conversão e padronização de tipos de dados
df["DATA"] = pd.to_datetime(
    df["DATA"],
    format="%d/%m/%Y",
    errors="coerce"
)
print("\nTipo da coluna DATA após conversão:")
print(df["DATA"].dtype)
print("\nQuantidade de datas inválidas:")
print(df["DATA"].isna().sum())

print("\nValores da coluna gênero:")
print(df["CL_GENERO"].value_counts(dropna=False))

print("\nValores da coluna segmento:")
print(df["CL_SEG"].value_counts(dropna=False))

print("\nValores da coluna categoria:")
print(df["PR_CAT"].value_counts(dropna=False))

print("\nQuantidade de produtos diferentes:")
print(df["PR_NOME"].nunique())

print("\nExemplos de produtos:")
print(df["PR_NOME"].unique()[:20])

df["PR_NOME"] = df["PR_NOME"].str.strip().str.upper()
df["PR_NOME"] = df["PR_NOME"].str.replace(r"\s+", " ", regex=True)

print("\nValores da coluna número de filhos:")
print(df["CL_FHL"].value_counts(dropna=False).sort_index())
print("\nMenor número de filhos:", df["CL_FHL"].min())
print("Maior número de filhos:", df["CL_FHL"].max())