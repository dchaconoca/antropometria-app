import streamlit as st
import requests
import json
from PIL import Image

st.set_page_config(page_title='dIAna', page_icon=None, 
                   layout="centered", initial_sidebar_state="auto", menu_items=None)

URL_BASE = 'https://antropo-api-registry-ft3evlkfyq-rj.a.run.app'

#URL_BASE = 'http://127.0.0.1:8000'

BMI_HELP = '''
      Índice de Masa Corporal.\n
      \t0 - Peso Bajo\n
      \t1 - Peso Normal\n
      \t2 - Sobrepeso\n
      \t3 - Obesidad
'''

CC_HELP = '''
      Contorno de Cintura (CC) y acumulación de grasa abdominal.\n
      \t0 - Sin riesgo\n
      \t1 - Riesgo o exceso de grasa abdominal
'''

RCC_HELP = '''
      Relación entre el Contorno de Cintura y la Cadera.\n
      \t0 - Sin riesgo\n
      \t1 - Riesgo medio\n
      \t2 - Riesgo alto
'''

ICT_HELP = '''
      Relación entre el Contorno de Cintura y la Estatura.\n
      \t0 - Delgado\n
      \t1 - Peso Normal\n
      \t2 - Sobrepeso\n
      \t3 - Obesidad
'''

def calcul_risk():
                  
      person = {
             'age': age,
             'gender': ('male' if gender==0 else 'female'),
             'weight': weight,
             'height': height,
             'waist_circum_preferred': waist_circum_preferred,
             'hip_circum': hip_circum
      }

      person = json.dumps(person) 

      try:
            response = requests.post(URL_BASE + '/obesity',
                              headers={'Content-Type': 'application/json'},
                              data=person,
                              timeout=8000)
            
            return json.loads(response.content)
      
      except requests.exceptions.RequestException as e:
            # Manejar errores de solicitud (por ejemplo, problemas de red)
            st.error("Error de solicitud a la API: " + str(e))
            st.stop()

      except requests.exceptions.HTTPError as e:
            # Manejar errores de respuesta HTTP (por ejemplo, códigos de estado no exitosos)
            st.error("Error HTTP de la API: " + str(e))
            st.stop()

      except Exception as e:
            # Manejar cualquier otro error inesperado
            st.error("Error inesperado: " + str(e))
            st.stop()



st.subheader('¿Tienes algún riesgo de padecer sobrepeso y/o enfermedades no transmisibles?')

st.markdown(
      '¡Hola! Soy **d:blue[IA]na** y te voy a ayudar a predecir si corres algún riesgo de padecer sobrepeso o y/o enfermedades no transmisibles (ENT).'
)

st.markdown(
      'Sólo necesitas introducir la información siguiente (**¡No olvides ningún dato!**):'
)

col1, col2 = st.columns((1, 1))

with col1:

      with st.form('form_obesity_risk'):

            age = st.number_input('¿Cuál es tu edad? Debes tener más de 18 años', min_value=18)
            gender = st.radio('¿Cuál es tu género?', ('Femenino', 'Masculino'), horizontal=True)
            weight = st.number_input('¿Cuál es tu peso, en Kg?', min_value=0.1)
            height = st.number_input('¿Cuál es tu estatura, en cm?', min_value=0.1)
            waist_circum_preferred = st.number_input('¿Cuál es el contorno de tu cintura, en cm?', min_value=0.1)
            hip_circum = st.number_input('¿Y el contorno de tu cadera, en cm? Puedes guiarte por la imagen de la derecha', 
                                         min_value=0.1)
            
            # st.button('¡Empecemos de nuevo!', key=None, help=None, on_click=st.experimental_rerun(), 
            #           type="secondary", disabled=False, use_container_width=False)

            submit = st.form_submit_button('¡Vamos!')

with col2:
      image= Image.open('streamlit/medidas.jpg')

      st.image(image, caption='¿Cómo tomar las medidas?', 
            width=50, use_column_width="auto", output_format="auto")
      
      if submit:
            result = calcul_risk()

            result = result[0]

            if result['obesity'] == 0:
                  st.subheader(':green[¡Excelente!] :smiley:')
                  st.markdown('No tienes sobrepeso ni corres el riesgo de padecer ENT.')
                  st.markdown('Sigue ejercitándote y manteniendo una dieta saludable.')

            if result['obesity'] == 1:
                  st.subheader(':orange[¡Hay cosas que mejorar!] :confused:')
                  st.markdown('Tienes algo de sobrepeso y puede que desarrolles alguna ENT.')
                  st.markdown('Ejercítate un poco más y mejora tu alimentación. Consulta a tu médico si es necesario.')

            if result['obesity'] == 2:
                  st.subheader(':red[¡Ay!...] :worried:')
                  st.markdown('Tienes sobrepeso/obesidad. Corres el riesgo de padecer alguna ENT.')
                  st.markdown('Lo mejor será consultar a tu médico.')
      
if submit:
      col1, col2, col3, col4 = st.columns((1,1,1,1))
      col1.metric(label='Índice de Masa Corporal:', value=result['bmi'], help=BMI_HELP)
      col2.metric('Cintura y grasa abdominal:', result['cc'], help=CC_HELP)
      col3.metric('Relación Cintura y Cadera:', result['rcc'], help=RCC_HELP)
      col4.metric('Relación Cintura y Estatura:', result['ict'], help=ICT_HELP)

st.markdown(':orange[**Nota:** Esto es un ejercicio de ciencia de datos. Los resultados NO deben tomarse como la opinión de un especialista. Consulte a su médico si tiene dudas.]')