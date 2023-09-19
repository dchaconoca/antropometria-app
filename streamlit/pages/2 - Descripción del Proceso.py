import streamlit as st

from src.app_config import page_config, sidebar_config

page_config()

#sidebar_config()

st.header('Descripción del procesamiento de los datos:')

st.markdown(
    '''
    **Objetivo del estudio:** Determinar el grado de riesgo de un individuo de padecer sobrepeso u obesidad y Enfermedades No Transmisibles (ENT).

    El grado de risgo se determina utilizando algoritmos de aprendizaje automático que permiten comparar y clasificar individuos con características similares y así deducir el grado de riesgo.

    Al no tener explícitamente la información sobre el grado de riesgo en los datos originales, se utiliza primero un algoritmo que determinará grupos de individuos similares y luego, gracias al análisis por un profesional de la salud de cada grupo, es posible etiquetar los datos.

    Con los datos etiquetados, se podrá entrenar el modelo que permitirá derterminar el grado de riesgo de una nueva persona.

    Finalmente, es posible guardar los datos de nuevas personas, con el grado de riesgo real determinado por su médico. 

    El algoritmo de predicción podrá ser entrenado de nuevo utilizando también los nuevos datos.
    '''
)

st.markdown('##### Pasos del procesamiento de los datos:')

st.markdown(
    '''
    1. **Carga, limpieza y transformación de los datos:** Información sobre 4.300 personas, datos contenidos en el archivo:
    [**Civilian American and European Surface Anthropometry Resource, or CAESAR**](https://data.world/andy/caesar/workspace/file?filename=caesar.csv). Luego de limpiar los datos, se transforman al sistema métrico y se calculan los indicadores.
    '''
)

st.markdown(
    '''
    2. **EDA:** Análisis Exploratorio de los Datos, en particular de los indicadores calculados y que serán utilizados para la clasificación y entrenamiento del modelo de aprendizaje automático.
    '''
)

st.markdown(
    '''
    3. **Clasificación:** Se utiliza el algoritmo **KModes** para clasificar los datos. Este algoritmo busca similitudes entre las personas y crea grupos de individuos con características similares. Luego se pueden estudiar y analizar estos grupos para facilitar el etiquetado de los individuos según el grado de riesgo de padecer ENT por sobrepeso u obesidad.
    '''
)

st.markdown(
    '''
    4. **Análisis y Etiquetado:** Cada grupo creado en el paso anterior, se puede analizar y asignarle un grado de riesgo (etiqueta). Este etiquetado permitirá entrenar un modelo que clasificará los individuos.
    '''
)
