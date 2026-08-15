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