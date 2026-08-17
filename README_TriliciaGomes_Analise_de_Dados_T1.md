# 📊 Mini-projeto — Análise de Dados de Varejo

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte do curso de **Análise de Dados**, com o objetivo de aplicar conceitos de **manipulação, limpeza e análise exploratória de dados utilizando Python e Pandas**.

A análise foi realizada a partir da base **Base Varejo.csv**, contendo informações relacionadas a clientes, compras e produtos.

O projeto contempla desde a importação e identificação de problemas de qualidade dos dados até a geração de estatísticas descritivas, agrupamentos e principais insights obtidos a partir da base tratada.

---

## 🎯 Objetivos

* Importar e explorar a base de dados;
* Identificar valores nulos, duplicatas e inconsistências;
* Realizar limpeza e padronização dos dados;
* Converter e ajustar tipos de dados;
* Calcular estatísticas descritivas;
* Explorar padrões utilizando agrupamentos;
* Gerar uma base limpa para análises posteriores;
* Apresentar os principais insights encontrados.

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **Pandas**
* **VS Code**
* **Git**
* **GitHub**

---

## 🔎 Etapas da análise

### 1. Importação e exploração inicial

A base foi carregada utilizando a biblioteca **Pandas**.

Inicialmente foram analisados:

* Número de registros;
* Número e nome das colunas;
* Tipos de dados;
* Primeiros registros;
* Informações gerais da base.

A base original possuía **830.000 registros**.

---

### 2. Limpeza e transformação dos dados

Foram realizados tratamentos para melhorar a qualidade e a consistência dos dados.

Os principais procedimentos realizados foram:

* Conversão da coluna `DATA` para o tipo `datetime`;
* Verificação de possíveis datas inválidas;
* Padronização dos nomes dos produtos;
* Remoção de espaços excedentes utilizando métodos de string e expressão regular;
* Verificação dos valores da variável de número de filhos;
* Padronização dos registros `#N/D` da categoria de produtos para `NAO INFORMADO`.

---

### 3. Tratamento de valores nulos e duplicatas

Durante a análise foram identificadas quatro colunas completamente vazias:

* `Unnamed: 10`
* `Unnamed: 11`
* `Unnamed: 12`
* `Unnamed: 13`

Como essas colunas apresentavam **100% de valores nulos** e não possuíam informações relevantes para a análise, elas foram removidas.

Também foram identificados **96.553 registros duplicados exatos**.

Após a remoção das duplicatas, a base passou de:

**830.000 registros → 733.447 registros**

---

### 4. Estatística descritiva

Foi realizada uma análise estatística da coluna `CL_FHL`, referente ao **número de filhos do cliente**.

Foram calculados:

* Média;
* Mediana;
* Moda;
* Desvio padrão;
* Valor mínimo;
* Valor máximo;
* Contagem;
* Quartis.

Os resultados mostraram uma média de aproximadamente **1,15 filho**, enquanto a mediana encontrada foi **0**.

Também foi observado que **75% dos registros apresentam até 2 filhos**.

---

### 5. Análises por agrupamento

Foram utilizados agrupamentos com o método `groupby()` do Pandas para identificar padrões presentes na base.

As análises realizadas foram:

#### Quantidade de registros por gênero

Após a limpeza da base:

* **Feminino:** 382.427 registros
* **Masculino:** 351.020 registros

#### Quantidade de registros por categoria de produto

A categoria **ALIMENTOS** apresentou a maior quantidade de registros, seguida por **HIGIENE** e **LIMPEZA**.

Também foi realizado um agrupamento combinando **gênero e categoria de produto**, permitindo observar a distribuição das categorias entre os dois grupos.

---

## 💡 Principais insights

1. A base original apresentava problemas relevantes de qualidade, incluindo **quatro colunas completamente vazias** e **96.553 registros duplicados**.

2. Após a limpeza, a base passou de **830.000 para 733.447 registros**, eliminando duplicatas exatas e informações sem utilidade analítica.

3. A distribuição do número de filhos apresenta concentração nos valores mais baixos. A **mediana é 0**, enquanto **75% dos registros possuem até 2 filhos**.

4. O gênero feminino apresenta maior quantidade de registros na base tratada, com **382.427 registros**, comparados a **351.020 registros** do gênero masculino.

5. **ALIMENTOS** é a categoria com maior quantidade de registros, seguida por **HIGIENE** e **LIMPEZA**.

6. Registros originalmente classificados como `#N/D` foram preservados como `NAO INFORMADO`, evitando excluir informações ou atribuir categorias sem evidências.

---

## ⚠️ Limitações da análise

A base não possui informações de **preço ou valor financeiro das transações**. Dessa forma, os agrupamentos realizados representam principalmente quantidades de registros, não sendo possível determinar diretamente quais grupos ou categorias geraram maior receita.

Além disso, alguns produtos permanecem classificados como `NAO INFORMADO`, pois a base original não fornece informações suficientes para determinar corretamente suas categorias.

---

## 📁 Estrutura do projeto

```text
Mini-projeto/
│
├── Base Varejo.csv
├── main.py
├── df_limpo.csv
└── README.md
```

### Descrição dos arquivos

* `Base Varejo.csv` — base original utilizada no projeto;
* `main.py` — script Python responsável pela limpeza e análise exploratória;
* `df_limpo.csv` — base resultante após o tratamento dos dados;
* `README.md` — documentação do projeto.

---

## ▶️ Como executar o projeto

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 2. Acesse a pasta do projeto

```bash
cd NOME_DO_REPOSITORIO
```

### 3. Instale o Pandas, caso necessário

```bash
pip install pandas
```

### 4. Execute o script

```bash
python main.py
```

Ao final da execução, o script apresenta os resultados da análise no terminal e gera o arquivo:

```text
df_limpo.csv
```

---

## 📝 Reflexão

O desenvolvimento deste mini-projeto permitiu aplicar na prática diferentes etapas de uma **Análise Exploratória de Dados (EDA)**, desde a importação da base até a identificação de padrões e geração de insights.

Um dos principais aprendizados foi compreender que a limpeza dos dados não deve ser realizada de forma automática. Antes de excluir, substituir ou transformar uma informação, é necessário entender o que ela representa e avaliar o impacto dessa decisão sobre a análise.

A identificação de duplicatas, valores ausentes e categorias não informadas também demonstrou a importância da **qualidade dos dados** para a obtenção de resultados confiáveis.

Além disso, a utilização de estatísticas descritivas e agrupamentos permitiu transformar os dados tratados em informações mais fáceis de interpretar, demonstrando como ferramentas como **Python e Pandas** podem apoiar o processo de análise de dados.
