import streamlit as st
from PIL import Image

from src.call_api import obesity_prediction, save_obesity_info
from src.app_config import page_config, sidebar_config, BMI_HELP, CC_HELP, RCC_HELP, ICT_HELP, OBESITY_HELP, COMMENTS_HELP

page_config()

#sidebar_config()

st.subheader('¿Tienes algún riesgo de padecer sobrepeso y/o enfermedades no transmisibles?')

st.markdown(
      '¡Hola! Soy **d:orange[IA]na** y te voy a ayudar a predecir si corres algún riesgo de padecer sobrepeso o y/o enfermedades no transmisibles (ENT).'
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
            
            submit_prediction = st.form_submit_button('¡Vamos!')

with col2:
      image= Image.open('streamlit/images/medidas.jpg')

      st.image(image, caption='¿Cómo tomar las medidas?', 
            width=50, use_column_width="auto", output_format="auto")
      
      if submit_prediction:

            person = {
                  'age': age,
                  'gender': ('male' if gender=='Masculino' else 'female'),
                  'weight': weight,
                  'height': height,
                  'waist_circum_preferred': waist_circum_preferred,
                  'hip_circum': hip_circum
            }

            result = obesity_prediction(person)

if submit_prediction:
            
            result = result[0]
            st.session_state.result_global = result

            if result['obesity'] == 0:
                  st.subheader(':green[¡Excelente!] :smiley:')
                  st.markdown('**No tienes sobrepeso ni corres el riesgo de padecer ENT.**')
                  st.markdown('**Sigue ejercitándote y manteniendo una dieta saludable.**')

            if result['obesity'] == 1:
                  st.subheader(':orange[¡Hay cosas que mejorar!] :confused:')
                  st.markdown('**Tienes algo de sobrepeso y puede que desarrolles alguna ENT.**')
                  st.markdown('**Ejercítate un poco más y mejora tu alimentación. Consulta a tu médico si es necesario.**')

            if result['obesity'] == 2:
                  st.subheader(':red[¡Ay!...] :worried:')
                  st.markdown('**Tienes sobrepeso/obesidad. Corres el riesgo de padecer alguna ENT.**')
                  st.markdown('**Lo mejor será consultar a tu médico.**')
      
if submit_prediction:
      col1, col2, col3, col4 = st.columns((1,1,1,1))
      col1.markdown(':orange[**Índice de Masa Corporal**]', help=BMI_HELP)
      col2.markdown(':orange[**Cintura y grasa abdominal**]', help=CC_HELP)
      col3.markdown(':orange[**Relación Cintura y Cadera**]', help=RCC_HELP)
      col4.markdown(':orange[**Relación Cintura y Estatura**]', help=ICT_HELP)

      col1.metric(label=' ', value=round(result['bmi'], 2), label_visibility='hidden')
      col2.metric(label=' ', value=round(result['waist_circum_preferred'], 2), label_visibility='hidden')
      col3.metric(label=' ', value=round(result['rcc'], 2), label_visibility='hidden')
      col4.metric(label=' ', value=round(result['ict'], 2), label_visibility='hidden')

      col1.metric(label=' ', value=result['obesity_bmi_txt'], help=BMI_HELP, label_visibility='hidden')
      col2.metric(label=' ', value=result['obesity_cc_txt'], help=CC_HELP, label_visibility='hidden')
      col3.metric(label=' ', value=result['obesity_rcc_txt'], help=RCC_HELP, label_visibility='hidden')
      col4.metric(label=' ', value=result['obesity_ict_txt'], help=ICT_HELP, label_visibility='hidden')

      st.markdown(':orange[**Nota:** Esto es un ejercicio de ciencia de datos. Los resultados NO deben tomarse como la opinión de un especialista. Consulta a tu médico si tienes dudas.]')

with st.form('form_save_data'):

      st.markdown('###### Si eres personal médico y deseas llevar un registro de los datos, agrega la información siguiente y guarda los datos:')

      obesity_risk = (
            '0 - Riesgo bajo o nulo',
            '1 - Riesgo medio',
            '2 - Riesgo alto'
      )

      real_obesity = st.selectbox('Escoge el grado de riesgo **real**, según el paciente y sus posibles padecimientos:', 
                        obesity_risk, help=OBESITY_HELP)
      
      comment = st.text_area('Escribe cualquier comentario que pueda ser útil (opcional):', help=COMMENTS_HELP)

      to_save = st.radio('¿Deseas guardar la información?', ('Sí', 'No'), horizontal=True)
      submit_data = st.form_submit_button('Guardar')        

      if submit_data:

            if to_save=='Sí': 
                  st.session_state.result_global.update({'real_obesity': int(real_obesity[:1])}) 
                  st.session_state.result_global.update({'comment': comment}) 
                  result_save = save_obesity_info(st.session_state.result_global)

                  if result_save: st.success('¡La información fue guardada exitosamente!')