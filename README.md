# 🫀 Classificação de Eventos de Insuficiência Cardíaca com KNN

Projeto acadêmico de Inteligência Artificial que utiliza o algoritmo **K-Nearest Neighbors (KNN)** para classificar registros clínicos relacionados à insuficiência cardíaca. O projeto inclui uma aplicação web desenvolvida com Streamlit para permitir que o usuário informe dados e visualize a classificação gerada pelo modelo.

## 🎯 Objetivo

Desenvolver e disponibilizar um protótipo de classificação utilizando aprendizado de máquina, explorando o uso de dados clínicos e a aplicação de algoritmos de classificação.

**Importante:** este projeto possui finalidade exclusivamente acadêmica e educacional. Os resultados não constituem diagnóstico médico nem devem ser utilizados para decisões clínicas.

## 📊 Dataset

Foi utilizado o conjunto de dados **Heart Failure Clinical Records**, disponibilizado no repositório UCI Machine Learning Repository.

- **Fonte:** [UCI Machine Learning Repository — Heart Failure Clinical Records](https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records)
- **Quantidade de registros:** 299
- **Variável-alvo:** `DEATH_EVENT`

O dataset contém informações clínicas e demográficas de pacientes acompanhados em um estudo sobre insuficiência cardíaca.

Para este experimento, foram utilizadas as seguintes variáveis de entrada:

| Variável | Descrição |
|---|---|
| `anaemia` | Indica a presença de anemia |
| `high_blood_pressure` | Indica a presença de pressão alta |
| `serum_creatinine` | Nível de creatinina sérica |
| `sex` | Sexo registrado no dataset |

A variável `DEATH_EVENT` representa o registro de um evento de morte durante o período de acompanhamento:

- `0`: evento de morte não registrado durante o acompanhamento.
- `1`: evento de morte registrado durante o acompanhamento.

## 🤖 Modelo de Machine Learning

O projeto utiliza o algoritmo **K-Nearest Neighbors (KNN)**, que classifica uma nova entrada com base nas classes dos exemplos mais próximos presentes nos dados de treinamento.

O processamento inclui:

1. Separação dos dados em conjuntos de treinamento e teste.
2. Normalização das variáveis numéricas utilizando `MinMaxScaler`.
3. Treinamento do classificador KNN.
4. Avaliação do modelo com dados separados para teste.
5. Salvamento do modelo treinado e do normalizador para utilização na aplicação.

O modelo e o normalizador são armazenados em arquivos `.pkl` e carregados pela aplicação.

## 🛠️ Tecnologias utilizadas

- Python 3.12
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Git e GitHub

## 📁 Estrutura do projeto

```text
predicao-insuficiencia-cardiaca/
├── app.py
├── modelo_knn.pkl
├── normalizador.pkl
├── requirements.txt
└── README.md
```

| Arquivo | Função |
|---|---|
| `app.py` | Código da aplicação web |
| `modelo_knn.pkl` | Modelo KNN treinado |
| `normalizador.pkl` | Normalizador utilizado no treinamento |
| `requirements.txt` | Dependências do projeto |
| `README.md` | Documentação do projeto |

## ⚙️ Como executar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/leoxLF/predicao-insuficiencia-cardiaca.git
```

### 2. Entre na pasta do projeto

```bash
cd predicao-insuficiencia-cardiaca
```

### 3. Crie e ative um ambiente virtual

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Execute a aplicação

```bash
streamlit run app.py
```

Após a inicialização, o Streamlit disponibilizará um endereço local para acessar a aplicação pelo navegador.

## 🌐 Aplicação online

O projeto está sendo preparado para publicação no Streamlit Community Cloud.

**Acesso:** [Predição de Insuficiência Cardíaca](https://predicao-cardiaca.streamlit.app/)

## 📚 Referências

- UCI Machine Learning Repository. *Heart Failure Clinical Records*. https://archive.ics.uci.edu/dataset/519/heart+failure+clinical+records
- Souza, V. S. e Lima, D. A. *Cardiac Disease Diagnosis Using K-Nearest Neighbor Algorithm: A Study on Heart Failure Clinical Records Dataset*. [Artigo científico](https://ojs.bonviewpress.com/index.php/AIA/article/view/2045).

## 👨‍💻 Autores

- **[Leanderson Ferreira](https://github.com/leoxLF)**
- **[Maria Clara](https://github.com/MariCPs)**

**Instituição:** Instituto Federal de Pernambuco (IFPE) — Campus Jaboatão dos Guararapes  
**Curso:** Análise e Desenvolvimento de Sistemas (ADS)

Projeto acadêmico desenvolvido em dupla para fins de estudo de Inteligência Artificial, classificação de dados e desenvolvimento de aplicações web com Python.
