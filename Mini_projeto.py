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

#nulos e duplicados
print("\nValores nulos por coluna:")
print(df.isna().sum())

df = df.drop(columns=["Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13"])

df["PR_CAT"] = df["PR_CAT"].replace("#N/D", "NAO INFORMADO")
print("\nCategorias após tratamento:")
print(df["PR_CAT"].value_counts())

print("\nQuantidade de registros duplicados:")
print(df.duplicated().sum())

print("\nExemplos de registros duplicados:")
print(df[df.duplicated(keep=False)].head(10))

print("\nRegistros antes da remoção:", len(df))

df = df.drop_duplicates()

print("Registros após a remoção:", len(df))


#Estatísticas descritivas
print("\nEstatísticas do número de filhos:")
print("Média:", df["CL_FHL"].mean())
print("Mediana:", df["CL_FHL"].median())
print("Desvio padrão:", df["CL_FHL"].std())
print("Moda:", df["CL_FHL"].mode()[0])
print("Máximo:", df["CL_FHL"].max())
print("Mínimo:", df["CL_FHL"].min())
print("Contagem:", df["CL_FHL"].count())
print("\nResumo estatístico:")
print(df["CL_FHL"].describe())

print("\nQuantidade de registros por gênero:")
print(df.groupby("CL_GENERO").size())

print("\nQuantidade de registros por categoria:")
print(df.groupby("PR_CAT").size().sort_values(ascending=False))

print("\nQuantidade de registros por gênero e categoria:")
print(df.groupby(["CL_GENERO", "PR_CAT"]).size())