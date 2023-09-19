import streamlit as st

from src.app_config import page_config, sidebar_config

page_config()

#sidebar_config()

st.header('Estudio del sobrepeso y la obesidad y su incidencia en las ENT:')

st.markdown(
    '''
    La obesidad y el sobrepeso son condiciones de salud que han alcanzado proporciones epidémicas a nivel mundial, siendo un factor determinante en el desarrollo de diversas enfermedades no transmisibles (ENT). Estas condiciones se caracterizan por un exceso de grasa corporal, lo que puede tener consecuencias significativas para la salud a largo plazo.

    El sobrepeso y la obesidad aumentan sustancialmente el riesgo de padecer enfermedades crónicas, como la diabetes tipo 2, la hipertensión y las enfermedades cardiovasculares. Estas afecciones pueden tener un impacto negativo en la calidad de vida, aumentando la morbilidad y la mortalidad en las poblaciones afectadas.

    Para evaluar y cuantificar el grado de sobrepeso y obesidad, se utilizan medidas antropométricas clave:

    1. **Índice de Masa Corporal (IMC):** Relaciona el peso y la altura de una persona. Sin embargo, es importante señalar que el IMC no distingue entre masa muscular y grasa, por lo que puede haber limitaciones en su interpretación, especialmente en atletas o personas con una distribución de grasa atípica.

    2. **Relación cintura-cadera (RCC) y la relación cintura-talla (RCT):** Estos indicadores ofrecen una perspectiva más completa sobre la distribución de la grasa corporal. Una acumulación excesiva de grasa en la región abdominal, medida mediante el **contorno de cintura**, está particularmente asociada con un mayor riesgo de enfermedades metabólicas y cardiovasculares. Un contorno de cintura elevado puede indicar la presencia de grasa visceral, que se asocia con inflamación y otros procesos patológicos.

    3. **La edad y el sexo:** A medida que las personas envejecen, es común experimentar cambios en el metabolismo y en la composición corporal, lo que puede influir en la tendencia a ganar peso. Además, existe evidencia de que las tasas de obesidad varían según el género, con diferencias en la distribución de grasa y en las respuestas hormonales.

    Medidas como el IMC, RCC y RCT no se encuentran en los datos utilizados para el estudio. Sin embargo, pueden ser calculados a partir del peso, la estatura, el contorno de cintura y el de cadera con las siguientes fórmulas:
    '''
)

st.latex('IMC = Peso (Kg) / Altura (m)^2')
st.latex('RCC = Cintura (cm) / Cadera (cm)')
st.latex('RCT = Cintura (cm) / Altura (cm)')

st.markdown(
    '''
    
    Luego, existen tablas que permiten clasificar el grado de sobrepeso y obesidad y el riesgo de tener exceso de grasa abdominal, en función de los valores obtenidos:

    
    1. Clasificación de obesidad según el IMC:

    |Riesgo|IMC|
    |------|---------|
    |Peso bajo | < 18.5 |
    |Peso normal|18.5 - 25 |
    |Sobrepeso|25 - 30 |
    |Obesidad|> 30 |  

    
    2. Clasificación de riesgo de grasa abdominal según el contorno de cintura (CC)

    |Riesgo|Femenino|Masculino|
    |------|---------|--------|
    |Bajo o nulo| < 80 cm | < 94 cm|
    |ALto |> 80 cm |> 94 cm |  

    
    3. Clasificación de riesgo de de grasa abdominal según el racio circunferencia de cintura y circunferencia de cadera (RCC)

    |Riesgo|Femenino|Masculino|
    |------|---------|--------|
    |Bajo| < 0.8 | < 0.95|
    |Medio|0.81 - 0.85 |0.96 - 1 |
    |Alto| > 0.86| > 1|  

    
    4. Clasificación de riesgo sobrepeso y riesgo de enfermedades no transmisibles según racio circunferencia cintura y talla (ICT):

    |Riesgo|Femenino|Masculino|
    |------|---------|--------|
    |Delgado| < 0.41 | < 0.42|
    |Sano| 0.41 - 0.48| 0.42 - 0.52|
    |Sobrepeso| 0.48 - 0.57 | 0.52 - 0.62|
    |Obesidad| > 0.57| > 0.62|  

    Esta aplicación, además de calcular estos índices, utiliza **Aprendizaje Automático** (parte de la inteligencia artificial) para poder determinar el riesgo que tiene una persona de sufrir sobrepeso u obesidad, y por ende, de padecer **Enfermedades No Transmisibles** (ENT).

    La predicción del riesgo se realiza gracias a la comparación de la información con la de individuos con características similares.

    **Nota:** Esta aplicación es un ejercicio de ciencia de datos. Si bien toma en cuenta las consideraciones médicas y científicas aquí expuestas, el estudio no ha sido verificado y avalado por ningún profesional de la salud. Cualquier duda que tengas, lo mejor es consultar a tu médico. 
   

    '''
)
