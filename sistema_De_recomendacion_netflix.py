"""9. Sistema de Recomendación de Netflix
Este proyecto es particularmente interesante. Se trata de un sistema de recomendación de
Netflix, ideal para aspirantes a científicos de datos o entusiastas del aprendizaje automático.
Para crear este proyecto, deberás importar una variedad de módulos, incluyendo tkinter, re,
nltk, pandas y numpy (consulta las instrucciones de instalación de pip para los nuevos
módulos). También necesitarás descargar un conjunto de datos que contenga películas y
programas de TV de Netflix (puedes encontrar datos aquí: https://www.kaggle.com/
datasets/satpreetmakhija/netflix-movies-and-tv-shows-2021?resource=download).
Puedes utilizar tkinter para crear nuestra interfaz gráfica de usuario (GUI), que utilizará
etiquetas, botones y campos de entrada. El usuario podrá ingresar una serie o película que
haya disfrutado en Netflix para obtener recomendaciones basadas en sus gustos. El motor de
recomendación podría utilizar reparto, director, calificaciones, país y géneros como
‘características' de similitud. """

# Importar las bibliotecas necesarias
import tkinter as tk  # Importa la biblioteca Tkinter para la creación de la interfaz gráfica de usuario (GUI)
from tkinter import messagebox  # Importa el módulo messagebox de Tkinter para mostrar cuadros de mensaje
import pandas as pd  # Importa pandas para la manipulación de datos (aunque no se usa directamente en este código)
import numpy as np  # Importa numpy para operaciones matemáticas
import nltk  # Importa NLTK (Natural Language Toolkit) para procesamiento de lenguaje natural
from nltk.corpus import stopwords  # Importa la lista de palabras vacías de NLTK
from nltk.tokenize import word_tokenize  # Importa el tokenizador de NLTK
from nltk.stem import WordNetLemmatizer  # Importa el lematizador de NLTK
from sklearn.feature_extraction.text import TfidfVectorizer  # Importa el vectorizador TF-IDF de scikit-learn
from sklearn.metrics.pairwise import cosine_similarity  # Importa la función para calcular la similitud coseno

# Descargar recursos necesarios de NLTK
nltk.download('punkt')  # Descarga el tokenizador de NLTK
nltk.download('stopwords')  # Descarga la lista de palabras vacías de NLTK
nltk.download('wordnet')  # Descarga el lematizador de NLTK

# Preprocesamiento de texto
stop_words = set(stopwords.words('english'))  # Lista de palabras vacías en inglés
lemmatizer = WordNetLemmatizer()  # Lematizador de palabras en inglés

def preprocess_text(text):
    words = word_tokenize(text.lower())  # Tokeniza el texto y lo convierte a minúsculas
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]  # Elimina palabras vacías y caracteres no alfanuméricos
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]  # Lematiza las palabras
    return ' '.join(lemmatized_words)  # Une las palabras procesadas en una cadena de texto

# Leer el archivo CSV y construir el diccionario de películas
movies = {}
with open('C:\\Users\\user\\Desktop\\ConqerBlocks\\Phyton\\python_avanzado\\Proyectos\\recomendacionNEtflix\\netflixData.csv', 'r', encoding='utf-8') as file:
    for line in file:
        parts = line.strip().split(',')
        code = parts[0]  # Código de la película
        title = parts[1]  # Título de la película
        description = parts[2]  # Descripción de la película
        director = parts[3]  # Director de la película
        genres = parts[4]  # Géneros de la película
        cast = parts[5]  # Reparto de la película
        country = parts[6]  # País de origen de la película
        
        # Combinar todos los atributos relevantes como características de la película
        features = ','.join([title, description, director, genres, cast, country])
        
        movies[code] = features  # Agregar la película al diccionario de películas

# Preprocesar los títulos de las películas
processed_titles = {code: preprocess_text(features.split(',')[0]) for code, features in movies.items()}

# Crear la matriz TF-IDF
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(processed_titles.values())

# Calcular similitud coseno entre los títulos
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Función para obtener recomendaciones
def get_recommendations(title):
    input_title_processed = preprocess_text(title)  # Preprocesamiento del título de entrada
    input_tfidf_vector = tfidf_vectorizer.transform([input_title_processed])  # Convertir el título preprocesado en un vector TF-IDF
    cosine_similarities = cosine_similarity(input_tfidf_vector, tfidf_matrix).flatten()  # Calcular la similitud coseno
    related_indices = cosine_similarities.argsort()[::-1][1:11]  # Obtener los índices de las películas más similares
    recommendations = [list(processed_titles.keys())[idx] for idx in related_indices]  # Obtener los códigos de las películas recomendadas
    recommendation_titles = [movies[code].split(',')[0] for code in recommendations]  # Obtener los títulos correspondientes a los códigos de las películas recomendadas
    return recommendation_titles  # Devolver los títulos de las películas recomendadas

# Interfaz gráfica de usuario (GUI) utilizando Tkinter
def get_recommendations_gui():
    def show_recommendations():
        input_title = entry.get()  # Obtener el título ingresado por el usuario
        recommendations = get_recommendations(input_title)  # Obtener las recomendaciones para el título ingresado
        if not recommendations:
            messagebox.showinfo("Error", "No se encontraron recomendaciones para esta película o serie.")
        else:
            messagebox.showinfo("Recomendaciones", "\n".join(recommendations))  # Mostrar las recomendaciones en un cuadro de mensaje

    root = tk.Tk()  # Crear la ventana principal de la interfaz gráfica
    root.title("Recomendaciones de Netflix")  # Establecer el título de la ventana

    label = tk.Label(root, text="Ingrese el título de la película o serie:")  # Etiqueta para instrucciones al usuario
    label.pack()  # Empaquetar la etiqueta en la ventana

    entry = tk.Entry(root)  # Campo de entrada para que el usuario ingrese el título
    entry.pack()  # Empaquetar el campo de entrada en la ventana

    button = tk.Button(root, text="Obtener recomendaciones", command=show_recommendations)  # Botón para obtener recomendaciones
    button.pack()  # Empaquetar el botón en la ventana

    root.mainloop()  # Iniciar el bucle de eventos de la interfaz gráfica

# Llamar a la función para mostrar la interfaz gráfica de usuario
get_recommendations_gui()