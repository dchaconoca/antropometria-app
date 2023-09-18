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


LABEL_SIZE=12
TITLE_SIZE=18

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
    \t0 - Riesgo bajo o nulo: La persona no padece ninguna ENT y a priori 
          tiene un riesgo nulo o bajo de padecerlas.\n
    \t1 - Riesgo medio: La persona no padece ninguna ENT pero hay indicadores 
          que señalan que podría comenzar a padecerlas: Puede estar desarrollando 
          resistencia a la insulina o tener episodios de hipertensión, por ejemplo.\n
    \t2 - Riesgo alto: La persona padece alguna ENT, diagnosticada o no.

'''

COLS_CLUSTER_LABEL = {
  "age_range": 'Rango de Edad',
  "bmi": 'IMC',
  "cc": 'Cintura',
  "rcc": 'RCC',
  "ict": 'ICT',
  "risk_factors": 'N° factores de riesgo',
#   "obesity": st.column_config.NumberColumn(
#             "Grado de Obesidad",
#             help=OBESITY_HELP,
#             min_value=0,
#             max_value=2,
#             step=1
#         ),
  "obesity": st.column_config.SelectboxColumn(
            "Grado de Obesidad",
            help=OBESITY_HELP,
            options=[None, 0, 1, 2],
            default=None,
        ),
  "total": 'Cantidad de personas',
  "label": None,
}


# column_config={
#         "category": st.column_config.SelectboxColumn(
#             "App Category",
#             help="The category of the app",
#             width="medium",
#             options=[
#                 "📊 Data Exploration",
#                 "📈 Data Visualization",
#                 "🤖 LLM",
#             ],
#             required=True,
#         )
#     },

COEF_SIL_HELP = '''
      Coeficiente de Silhouette: Varía entre -1 y 1.\n
      \t-1 - Mal agrupamiento\n
      \t0 - Indiferente\n
      \t1 - Buen agrupamiento
'''

DB_HELP = '''
    Valores pequeños para el índice David-Bouldin 
    indican grupos compactos y cuyos centros 
    están bien separados los unos de los otros.

    El número de grupos o clusters que minimiza el índice DB
    se toma como el óptimo.
'''

CH_HELP = '''
    El índice de Calinski-Harabasz,
    es una métrica con la que se puede evaluar 
    el grado de agrupación de un conjunto de datos. 

    Cuando mayor sea el valor del índice, 
    mejor será la agrupación.
'''