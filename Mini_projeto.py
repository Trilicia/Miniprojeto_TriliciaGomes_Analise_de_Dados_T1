import csv
import pandas as pd
from datetime import datetime

# Carregando a base de dados e informações iniciais
with open("Base Varejo.csv", mode="r", encoding="utf-8") as arquivo:
    leitor_csv = csv.DictReader(arquivo, delimiter=";")
    primeira_linha = next(leitor_csv)

print("\nPrimeiro registro lido com csv.DictReader:")
print(primeira_linha)

df = pd.read_csv("Base Varejo.csv", sep=";")
total_inicial = len(df)

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

#Validação do identificador de compra
print("\nQuantidade de identificadores de compra:")
print(df["CO_ID"].nunique())

print("\nQuantidade de compras únicas:")
print(df["CO_ID"].head(20))

print("\nQuantidade de registros por compra:")
print(df.groupby("CO_ID").size().head(20))

# Separação dos registros por identificador de compra
compras = df.groupby("CO_ID")

print("\nExemplo de registros da compra 1000:")
print(compras.get_group(1000)[["CO_ID", "CL_ID", "PR_ID", "PR_NOME"]].head(10))

#Limpeza, conversão e padronização de tipos de dados
def converter_data(valor):
    try:
        return datetime.strptime(valor, "%d/%m/%Y")
    except:
        return None

df["DATA"] = df["DATA"].apply(converter_data)

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

def tratar_categoria(valor):
    if pd.isna(valor) or valor == "#N/D" or valor.strip() == "":
        return "Sem Categoria"
    else:
        return valor
    
df["PR_CAT"] = df["PR_CAT"].apply(tratar_categoria)
print("\nCategorias após tratamento:")
print(df["PR_CAT"].value_counts())

duplicatas = df.duplicated().sum()

print("\nQuantidade de registros duplicados:")
print(duplicatas)

print("\nExemplos de registros duplicados:")
print(df[df.duplicated(keep=False)].head(10))

print("\nRegistros antes da remoção:", len(df))

df = df.drop_duplicates()
total_final = len(df)
percentual_duplicatas = (duplicatas / total_inicial) * 100
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


#Dados para sprint 5
print("\n" + "=" * 50)
print("RELATÓRIO FINAL - ANÁLISE DA BASE VAREJO")
print("=" * 50)

print("\nResumo da limpeza:")
print("Registros iniciais:", total_inicial)
print("Registros finais:", total_final)
print("Duplicatas removidas:", duplicatas)
print(f"Percentual de duplicatas: {percentual_duplicatas:.2f}%")

print("\nPrincipais insights:")
print("1. Foram identificadas e removidas 4 colunas totalmente vazias.")
print(f"2. Foram removidos {duplicatas} registros duplicados.")
print(f"3. A média do número de filhos é {df['CL_FHL'].mean():.2f}, enquanto a mediana é {df['CL_FHL'].median():.0f}.")
print("4. O gênero feminino apresenta maior quantidade de registros na base.")
print("5. ALIMENTOS é a categoria com maior quantidade de registros.")
print("6. Categorias vazias ou não identificadas foram tratadas como 'Sem Categoria'.")


#Exportar base limpa
df.to_csv("df_limpo.csv", sep=";", index=False)

print("\nBase limpa exportada com sucesso!")

