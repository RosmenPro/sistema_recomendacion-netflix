# Recomendador de Películas de Netflix

Este proyecto es un recomendador de películas y series basado en similitud de títulos, utilizando técnicas de procesamiento de lenguaje natural y aprendizaje automático. Permite al usuario ingresar el título de una película o serie, y el sistema genera una lista de recomendaciones similares.

## Características

- Preprocesamiento de texto para eliminar palabras vacías y lematización.
- Cálculo de la similitud de títulos utilizando el algoritmo **TF-IDF** y **similitud coseno**.
- Interfaz gráfica de usuario (GUI) para una interacción sencilla utilizando **Tkinter**.
- Base de datos de películas y series obtenida de un archivo CSV.

## Tecnologías Utilizadas

- **Python 3.x**
- **Tkinter**: Para la interfaz gráfica de usuario.
- **NLTK**: Para procesamiento de lenguaje natural.
- **scikit-learn**: Para vectorización TF-IDF y cálculo de similitud coseno.
- **Pandas y Numpy**: Para manipulación de datos.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalados los siguientes paquetes:

```bash
pip install pandas numpy nltk scikit-learn
```

Además, es necesario descargar los recursos de NLTK:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener los paquetes necesarios instalados.
3. Coloca el archivo `netflixData.csv` en la ruta correcta en el proyecto.

## Uso

1. Ejecuta el script principal:

   ```bash
   python recomendador_netflix.py
   ```

2. Aparecerá una ventana que te pedirá ingresar el título de una película o serie.

3. Haz clic en "Obtener recomendaciones" para obtener una lista de títulos similares.

## Estructura del Código

- **preprocess_text**: Función que tokeniza, elimina palabras vacías y lematiza los títulos.
- **get_recommendations**: Genera recomendaciones basadas en la similitud coseno de los títulos procesados.
- **get_recommendations_gui**: Crea la interfaz gráfica de usuario para interactuar con el recomendador.

## Archivo CSV

El archivo `netflixData.csv` debe contener las siguientes columnas:

- Código de película/serie
- Título
- Descripción
- Director
- Géneros
- Reparto
- País de origen

## Contribuir

Las contribuciones son bienvenidas. Si tienes sugerencias o mejoras, siéntete libre de crear un pull request.

---

# Netflix Movie Recommender

This project is a movie and series recommender based on title similarity, using natural language processing techniques and machine learning. It allows users to enter a movie or series title, and the system generates a list of similar recommendations.

## Features

- Text preprocessing to remove stop words and apply lemmatization.
- Title similarity calculation using **TF-IDF** and **cosine similarity**.
- Graphical User Interface (GUI) for easy interaction using **Tkinter**.
- Database of movies and series obtained from a CSV file.

## Technologies Used

- **Python 3.x**
- **Tkinter**: For the graphical user interface.
- **NLTK**: For natural language processing.
- **scikit-learn**: For TF-IDF vectorization and cosine similarity calculation.
- **Pandas and Numpy**: For data manipulation.

## Requirements

Before running the project, make sure you have the following packages installed:

```bash
pip install pandas numpy nltk scikit-learn
```

Additionally, download the required NLTK resources:

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

## Installation

1. Clone this repository or download the files.
2. Ensure the necessary packages are installed.
3. Place the `netflixData.csv` file in the correct path in the project.

## Usage

1. Run the main script:

   ```bash
   python recomendador_netflix.py
   ```

2. A window will appear, prompting you to enter a movie or series title.

3. Click "Get Recommendations" to receive a list of similar titles.

## Code Structure

- **preprocess_text**: Function that tokenizes, removes stop words, and lemmatizes titles.
- **get_recommendations**: Generates recommendations based on cosine similarity of processed titles.
- **get_recommendations_gui**: Creates the graphical user interface to interact with the recommender.

## CSV File

The `netflixData.csv` file should contain the following columns:

- Movie/series code
- Title
- Description
- Director
- Genres
- Cast
- Country of origin

## Contributing

Contributions are welcome. If you have suggestions or improvements, feel free to create a pull request.

