from transformers import pipeline
import streamlit as st


# Функция подгрузки данных модели
@st.cache_resource
def load_model():
    model_pipeline = pipeline(
        task="question-answering", model="deepset/roberta-base-squad2"
    )
    return model_pipeline


# Функция запуска модели
def execute(question1, text1):
    result = model(question=question1, context=text1)
    st.text("Ответ на вопрос: " + result["answer"])


# Функция инициализации части фронтенда
def initializing_frontend():
    # Заголовок
    st.title(body="Приложение отвечающее на пользовательские вопросы по тексту")
    # Текст для анализа
    text = st.text_area(label="Введите текст", value=" ", height=300)
    # Вопрос
    question = st.text_input(label="Введите вопрос", value=" ")


# Инициализация фронтенда
initializing_frontend()
# Активность кнопки
disabled = True if text == " " or question == " " else False
# Подгрузка модели
model = load_model()
# Кнопка для запуска модели
executed = st.button(label="Выполнить", disabled=disabled)
if executed:
    execute(question, text)