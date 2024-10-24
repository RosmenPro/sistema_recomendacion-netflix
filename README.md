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

