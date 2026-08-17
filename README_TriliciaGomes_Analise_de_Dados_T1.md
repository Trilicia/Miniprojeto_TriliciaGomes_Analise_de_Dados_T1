# 📊 Mini-projeto — Análise Exploratória de Dados de Varejo

## 📌 Sobre o projeto

Este mini-projeto foi desenvolvido como parte do curso de **Análise de Dados**, com o objetivo de aplicar conceitos de manipulação, limpeza, transformação e análise exploratória de dados utilizando **Python**.

A análise foi realizada a partir da base `Base Varejo.csv`, contendo informações relacionadas a clientes, compras e produtos.

O projeto contempla a leitura estruturada do arquivo CSV, validação de regras de negócio, identificação e tratamento de problemas de qualidade, conversão de tipos, remoção de duplicatas, geração de estatísticas descritivas, análises por agrupamento e apresentação dos principais insights encontrados.

---

## 🎯 Objetivos

Os principais objetivos do projeto são:

- Realizar a leitura e exploração da base de dados;
- Utilizar leitura estruturada de arquivos CSV;
- Identificar valores nulos, duplicatas e possíveis inconsistências;
- Realizar limpeza e padronização dos dados;
- Converter e ajustar tipos de dados;
- Validar o identificador das compras;
- Aplicar estruturas condicionais no tratamento dos dados;
- Calcular estatísticas descritivas;
- Explorar padrões utilizando agrupamentos;
- Gerar uma base limpa para análises posteriores;
- Apresentar os principais insights encontrados.

---

## 🛠️ Tecnologias utilizadas

- **Python**
- **Pandas**
- **Módulo CSV (`csv.DictReader`)**
- **Módulo Datetime**
- **VS Code**
- **Git**
- **GitHub**

---

## 🔎 Etapas da análise

### 1. Importação e exploração inicial

Inicialmente, foi realizada a leitura estruturada do arquivo utilizando o módulo nativo `csv` do Python e o método `csv.DictReader`.

O `DictReader` permite interpretar cada registro do arquivo CSV como um dicionário, utilizando os nomes das colunas como chaves.

Em seguida, a base foi carregada em um DataFrame utilizando a biblioteca **Pandas**, possibilitando a realização das etapas de tratamento e análise exploratória.

Na exploração inicial foram analisados:

- Número de registros;
- Número de colunas;
- Nome das colunas;
- Tipos de dados;
- Primeiros registros;
- Informações gerais da base.

A base original possuía **830.000 registros**.

---

### 2. Validação do identificador de compra

A coluna `CO_ID` foi analisada para compreender a regra de identificação das compras.

Foram encontrados **18.471 identificadores de compra distintos** na base original.

Durante a análise foi observado que um mesmo `CO_ID` pode aparecer em várias linhas. Isso ocorre porque uma compra pode estar associada a diferentes registros de produtos.

Dessa forma, a quantidade de linhas da base não deve ser interpretada diretamente como quantidade de compras.

Os registros foram agrupados utilizando `CO_ID`, permitindo separar e visualizar os itens pertencentes a uma mesma compra.

Essa validação foi importante para compreender a estrutura da base antes da realização das análises.

---

### 3. Limpeza, transformação e padronização

Foram realizados tratamentos com o objetivo de melhorar a qualidade e a consistência dos dados.

Entre os principais procedimentos realizados estão:

- Conversão da coluna `DATA`;
- Identificação de possíveis datas inválidas;
- Verificação dos valores das colunas categóricas;
- Padronização dos nomes dos produtos;
- Remoção de espaços excedentes;
- Padronização dos textos da coluna `PR_NOME` para letras maiúsculas;
- Verificação dos valores da variável `CL_FHL`, referente ao número de filhos.

Para a padronização dos nomes dos produtos foram utilizados métodos de manipulação de strings e expressão regular, reduzindo possíveis diferenças causadas por espaços excedentes ou variações na escrita.

---

### 4. Tratamento e conversão de datas

A coluna `DATA`, originalmente armazenada como texto, foi convertida para um formato adequado de data utilizando o módulo nativo `datetime` do Python.

A conversão foi realizada utilizando:

`datetime.strptime()`

O formato esperado para os registros foi definido como:

`%d/%m/%Y`

que representa **dia/mês/ano**.

Foi utilizada uma estrutura `try/except` para permitir o tratamento de valores que não pudessem ser convertidos para uma data válida.

Caso um registro apresente uma data inválida, o valor é convertido para `None`, permitindo posteriormente sua identificação como valor ausente.

Após a conversão, foi realizada uma verificação da quantidade de datas inválidas presentes na base.

Esse tratamento permite que a coluna seja utilizada corretamente em futuras análises temporais.

---

### 5. Tratamento de valores nulos e categorias

Durante a análise foram identificadas quatro colunas completamente vazias:

- `Unnamed: 10`
- `Unnamed: 11`
- `Unnamed: 12`
- `Unnamed: 13`

Como essas colunas não continham informações que pudessem ser utilizadas na análise, optou-se pela remoção, evitando imputar valores sem fundamento.

Na coluna `PR_CAT`, também foram identificados registros sem uma categoria válida.

Para realizar o tratamento foi criada uma função utilizando uma estrutura condicional `if/else`.

Foram considerados como categoria ausente:

- Valores nulos;
- Valores vazios;
- Registros identificados como `#N/D`.

Esses registros foram classificados como:

`Sem Categoria`

A escolha por manter esses registros como `Sem Categoria`, em vez de excluí-los ou atribuí-los a uma categoria existente, evita a perda de informações e a criação de classificações sem evidência nos dados originais.

---

### 6. Tratamento de duplicatas

Durante a análise da qualidade dos dados foram identificados **96.553 registros duplicados exatos**.

Antes da remoção, a base possuía:

**830.000 registros**

Após a remoção das duplicatas, a base passou a possuir:

**733.447 registros**

Isso representa aproximadamente **11,63% dos registros da base original**.

Antes da exclusão, foram visualizados exemplos dos registros duplicados para verificar a ocorrência do problema.

Posteriormente, as duplicatas exatas foram removidas, preservando uma ocorrência de cada registro.

---

### 7. Estatística descritiva

Foi realizada uma análise estatística da coluna `CL_FHL`, referente ao **número de filhos do cliente**.

Foram calculados:

- Média;
- Mediana;
- Moda;
- Desvio padrão;
- Valor mínimo;
- Valor máximo;
- Contagem;
- Primeiro quartil (25%);
- Segundo quartil (50%);
- Terceiro quartil (75%).

Os principais resultados encontrados foram:

- **Média:** aproximadamente 1,15;
- **Mediana:** 0;
- **Moda:** 0;
- **Mínimo:** 0;
- **Máximo:** 4;
- **Terceiro quartil (75%):** 2.

A diferença entre média e mediana indica uma concentração dos registros nos valores mais baixos.

A moda igual a `0` demonstra que esse é o número de filhos que aparece com maior frequência nos registros analisados.

O terceiro quartil igual a `2` indica que **75% dos registros apresentam número de filhos igual ou inferior a 2**.

---

### 8. Análises por agrupamento

Para explorar padrões presentes na base foram realizados agrupamentos utilizando o método `groupby()` do Pandas.

Foram analisadas diferentes combinações.

#### Registros por gênero

Após a limpeza da base:

- **Feminino:** 382.427 registros;
- **Masculino:** 351.020 registros.

Os resultados mostram uma quantidade ligeiramente maior de registros associados ao gênero feminino.

#### Registros por categoria de produto

As categorias com maior quantidade de registros foram:

1. **ALIMENTOS**
2. **HIGIENE**
3. **LIMPEZA**

A categoria `ALIMENTOS` apresentou uma quantidade de registros significativamente superior às demais.

#### Gênero e categoria de produto

Também foi realizado um agrupamento combinando as variáveis `CL_GENERO` e `PR_CAT`.

Essa análise permitiu observar como os registros das diferentes categorias de produtos estão distribuídos entre os gêneros presentes na base.

---

## 💡 Principais insights

1. A base original apresentava problemas de qualidade, incluindo **quatro colunas completamente vazias** e **96.553 registros duplicados exatos**.

2. As duplicatas representavam aproximadamente **11,63% da base original**, reduzindo a base de **830.000 para 733.447 registros** após o tratamento.

3. Na variável número de filhos, a **média é aproximadamente 1,15**, enquanto a **mediana e a moda são iguais a 0**, indicando concentração dos registros nos valores mais baixos.

4. Os registros associados ao gênero feminino aparecem em maior quantidade na base tratada, com **382.427 registros**, em comparação com **351.020 registros** associados ao gênero masculino.

5. **ALIMENTOS** é a categoria com maior quantidade de registros, seguida por **HIGIENE** e **LIMPEZA**.

6. Foram encontrados registros sem uma categoria válida. Esses valores foram preservados como `Sem Categoria`, evitando excluir registros ou atribuir categorias sem evidência nos dados originais.

---

## ⚠️ Limitações da análise

A base não apresenta informações de **preço ou valor financeiro das transações**. Dessa forma, os agrupamentos realizados representam quantidades de registros e não permitem determinar diretamente quais categorias ou grupos geraram maior receita.

Também existem registros classificados como `Sem Categoria`, pois as informações disponíveis na base original não permitem determinar com segurança a categoria correta desses produtos.

Além disso, como um mesmo cliente pode aparecer em diferentes registros da base, as estatísticas da coluna `CL_FHL` representam a distribuição dessa variável entre os **registros analisados**, e não necessariamente entre clientes únicos.

Da mesma forma, uma compra pode possuir vários registros. Por esse motivo, a quantidade de linhas da base não representa diretamente a quantidade de compras realizadas.

---

## 🔄 Reflexão sobre ETL e qualidade dos dados

O processo de **ETL (Extract, Transform, Load)** representa três etapas importantes no trabalho com dados: extração, transformação e carregamento.

Neste projeto, a etapa de **extração (Extract)** ocorreu por meio da leitura dos dados presentes no arquivo `Base Varejo.csv`, utilizando `csv.DictReader` e Pandas.

A etapa de **transformação (Transform)** envolveu a identificação e o tratamento de problemas encontrados na base, incluindo valores nulos, categorias não identificadas, registros duplicados, padronização de textos, validação do identificador das compras e conversão das datas.

A etapa de **carregamento (Load)** foi representada pela exportação dos dados tratados para um novo arquivo denominado `df_limpo.csv`.

A realização dessas etapas demonstrou a importância da **qualidade dos dados** para uma análise confiável. Dados duplicados, ausentes ou inconsistentes podem interferir nos resultados e levar a interpretações incorretas.

Um dos principais aprendizados do projeto foi compreender que a limpeza dos dados não deve ser realizada de maneira automática. Antes de excluir, substituir ou transformar uma informação, é necessário entender o que ela representa e avaliar o impacto da decisão sobre a análise.

Por esse motivo, as quatro colunas completamente vazias foram removidas, enquanto os registros sem categoria válida foram preservados como `Sem Categoria`. Dessa forma, buscou-se manter o máximo de informação possível sem criar dados que não estavam presentes na base original.

---

## 📁 Estrutura do projeto

```text
Mini-projeto/
│
├── Base Varejo.csv
├── Mini_projeto.py
├── df_limpo.csv
└── README.md
```

### Descrição dos arquivos

- `Base Varejo.csv` — base original utilizada no projeto;
- `Mini_projeto.py` — script responsável pela leitura, limpeza, transformação e análise exploratória;
- `df_limpo.csv` — base resultante após o tratamento dos dados;
- `README.md` — documentação do projeto.

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
python Mini_projeto.py
```

Ao final da execução, o script apresenta no terminal o relatório da análise e gera o arquivo:

```text
df_limpo.csv
```

---

## 📝 Considerações finais

O desenvolvimento deste mini-projeto permitiu aplicar conceitos fundamentais de **manipulação e análise exploratória de dados com Python**, passando pelas etapas de leitura, investigação, limpeza, transformação, análise e exportação dos dados.

Além da aplicação dos recursos técnicos do Python e do Pandas, o projeto demonstrou a importância de compreender a estrutura e o contexto dos dados antes de tomar decisões de tratamento.

A validação do identificador das compras mostrou, por exemplo, que uma mesma compra pode estar distribuída em diversos registros. Já o tratamento de categorias, duplicatas e datas demonstrou como problemas de qualidade podem interferir na interpretação das informações.

A análise exploratória permitiu transformar os dados originais em uma estrutura mais organizada, consistente e adequada para análises posteriores.