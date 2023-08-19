import streamlit as st

def page_config():

    return st.set_page_config(
        page_title='dIAna Antropometría y Obesidad', 
        page_icon=':health_worker:', 
        layout="centered", 
        initial_sidebar_state="auto", 
        menu_items={
            'Get Help': None,
            'Report a bug': None,
            'About': '''## Medidas Antropométricas para el predecir el riesgo de obesidad y ENT 
            
            Aplicación hecha por Diana Chacón Ocariz'''
        }
    )

def sidebar_config():
    st.sidebar.markdown(':orange[El estudio de los datos, la clasificación y el entrenamiento del modelo, no afectan el modelo ya existente y utilizado para las predicciones.]')


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

OBESITY_HELP = '''
    Asigna un valor entre 0 y 2:\n
    \t0 - Riesgo bajo o nulo\n
    \t1 - Riesgo medio\n
    \t2 - Riesgo alto

'''
COLS_CLUSTER_LABEL = {
  "age_range": 'Rango de Edad',
  "bmi": 'IMC',
  "cc": 'Cintura',
  "rcc": 'RCC',
  "ict": 'ICT',
  "risk_factors": 'N° factores de riesgo',
  "obesity": st.column_config.NumberColumn(
            "Grado de Obesidad",
            help=OBESITY_HELP,
            min_value=0,
            max_value=2,
            step=1
        ),
  "total": 'Cantidad de personas',
  "label": None,
}
