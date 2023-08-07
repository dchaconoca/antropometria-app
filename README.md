# # dIAna: Uso de medidas antropométricas y algoritmos de ML para determinar el riesgo de obesidad 

>Autora: Diana Chacón Ocariz


##  Estudio del sobrepeso y la obesidad y su incidencia en las ENT:

La obesidad y el sobrepeso son condiciones de salud que han alcanzado proporciones epidémicas a nivel mundial, siendo un factor determinante en el desarrollo de diversas enfermedades no transmisibles (ENT). Estas condiciones se caracterizan por un exceso de grasa corporal, lo que puede tener consecuencias significativas para la salud a largo plazo.

El sobrepeso y la obesidad aumentan sustancialmente el riesgo de padecer enfermedades crónicas, como la diabetes tipo 2, la hipertensión y las enfermedades cardiovasculares. Estas afecciones pueden tener un impacto negativo en la calidad de vida, aumentando la morbilidad y la mortalidad en las poblaciones afectadas.

Para evaluar y cuantificar el grado de sobrepeso y obesidad, se utilizan medidas antropométricas clave:

1. **Índice de Masa Corporal (IMC):** Relaciona el peso y la altura de una persona. Sin embargo, es importante señalar que el IMC no distingue entre masa muscular y grasa, por lo que puede haber limitaciones en su interpretación, especialmente en atletas o personas con una distribución de grasa atípica.

2. **Relación cintura-cadera (RCC) y la relación cintura-talla (RCT):** Estos indicadores ofrecen una perspectiva más completa sobre la distribución de la grasa corporal. Una acumulación excesiva de grasa en la región abdominal, medida mediante el **contorno de cintura**, está particularmente asociada con un mayor riesgo de enfermedades metabólicas y cardiovasculares. Un contorno de cintura elevado puede indicar la presencia de grasa visceral, que se asocia con inflamación y otros procesos patológicos.

3. **La edad y el sexo:** A medida que las personas envejecen, es común experimentar cambios en el metabolismo y en la composición corporal, lo que puede influir en la tendencia a ganar peso. Además, existe evidencia de que las tasas de obesidad varían según el género, con diferencias en la distribución de grasa y en las respuestas hormonales.

**Sin embargo, no existe una fórmula que combine todos estos datos y nos permita saber de manera objetiva el riesgo que tiene una persona de padecer obesidad y ENT.**

## Descripción de la aplicación:

Esta aplicación, además de calcular estos índices, utiliza algoritmos de Machine Learning para poder determinar el riesgo que tiene una persona de sufrir sobrepeso u obesidad, y por ende, de padecer Enfermedades No Transmisibles (ENT).

**Nota:** Esta aplicación es un ejercicio de ciencia de datos. Si bien toma en cuenta las consideraciones médicas y científicas aquí expuestas, el estudio no ha sido verificado y avalado por ningún profesional de la salud. Cualquier duda que tengas, lo mejor es consultar a tu médico.

## Implementación del prototipo de la aplicación:

A partir de los datos que el usuario introduce, la aplicación (hecha utilizando Streamlit) consulta una API (desarrollada con FastAPI) que carga el modelo de ML entrenado, y devuelve:

1. Indicadores y sus índices de riesgo: Índice de masa corporal, contorno de cintura, racio entre cintura y cadera, racio entre cintura y estatura.
2. Ińdice de riesgo predicho por el modelo: Riesgo bajo o nulo, riesgo medio, riesgo alto.

#### [dIAna antropometría y obesidad](https://diana-antropometria.streamlit.app/)

[Repostitorio GitHub](https://github.com/dchaconoca/antropometria-app)

**Nota:** Los resultados NO deben tomarse como la opinión de un especialista. Esto es un simple ejercicio de ciencia de datos.


![Prototipo-dIAna.png](attachment:Prototipo-dIAna.png)


## Instrucciones para la ejecución del proyecto:

1. **Ejecutar la API:** Ir al directorio `api` y ejecutar el comando uvicorn `api:app`. Esto ejecutará la API en local en el puerto 8000

2. **Ejecutar la aplicación Streamlit:** Ejecutar el comando `streamlit run streamlit/Inicio.py`. Esto ejecutará la App en local en el puerto 8501

3. Verificar en el archivo `streamlit/Inicio.py` que se está apuntando a la API en local.

    