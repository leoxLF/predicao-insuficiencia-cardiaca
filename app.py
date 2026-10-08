
import joblib
import pandas as pd
import streamlit as st

# Carregar o modelo e o normalizador
modelo_knn = joblib.load("modelo_knn.pkl")
normalizador = joblib.load("normalizador.pkl")

# Configuração da página
st.set_page_config(
    page_title="Predição de Insuficiência Cardíaca",
    page_icon="❤️",
    layout="centered"
)

# Título e apresentação
st.title("Predição de Insuficiência Cardíaca")

st.write(
    "Preencha os dados abaixo para que o modelo KNN "
    "realize uma classificação experimental."
)

st.warning(
    "Este aplicativo é um protótipo acadêmico. "
    "Não deve ser usado para diagnóstico ou decisões médicas."
)

# Formulário de entrada
st.subheader("Dados do paciente")

anemia = st.selectbox(
    "O paciente apresenta anemia?",
    options=[0, 1],
    format_func=lambda valor: "Não" if valor == 0 else "Sim"
)

pressao_alta = st.selectbox(
    "O paciente apresenta pressão alta?",
    options=[0, 1],
    format_func=lambda valor: "Não" if valor == 0 else "Sim"
)

creatinina = st.number_input(
    "Creatinina sérica",
    min_value=0.1,
    max_value=20.0,
    value=1.2,
    step=0.1
)

sexo = st.selectbox(
    "Sexo registrado no conjunto de dados",
    options=[0, 1],
    format_func=lambda valor: "Feminino" if valor == 0 else "Masculino"
)

# Executar a previsão
if st.button("Fazer previsão", type="primary"):

    paciente = pd.DataFrame({
        "anaemia": [anemia],
        "high_blood_pressure": [pressao_alta],
        "serum_creatinine": [creatinina],
        "sex": [sexo]
    })

    # Aplicar a mesma normalização usada no treinamento
    paciente_normalizado = normalizador.transform(paciente)

    # Obter a classificação do modelo
    previsao = modelo_knn.predict(paciente_normalizado)[0]

    st.subheader("Resultado da classificação")

    if previsao == 0:
        st.success(
            "O modelo classificou a entrada na classe 0: "
            
        )
    else:
        st.error(
            "O modelo classificou a entrada na classe 1: "
            
        )
