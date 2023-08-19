# Carga de librerías

import io

import streamlit as st

import pandas as pd

from src.call_api import obesity_return_data, obesity_return_nb_clusters, obesity_update_var
import src.eda_functions as ef
import src.char_common_functions as ccf

from src.app_config import page_config, sidebar_config, COLS_CLUSTER_LABEL

page_config()

sidebar_config()

def update_obesity(df, cluster):
    for index, row in df.iterrows():
        params = {
                    'obesity': row['obesity'],
                    'cluster': cluster,
                    'age_range': row['age_range'],
                    'bmi': int(row['bmi'][:1]),
                    'cc': int(row['cc'][:1]),
                    'rcc': int(row['rcc'][:1]),
                    'ict': int(row['ict'][:1])
                }
        result = obesity_update_var(params)

st.subheader('Análisis de los grupos generados por KModes')

st.markdown(''' 
    1. Escoge el grupo que deseas analizar.
            
    2. Etiqueta los datos.
            
    3. Actualiza el etiquetado.
''')
            
nb_clusters = obesity_return_nb_clusters()

if nb_clusters:

    result = obesity_return_data()
    df_obesity = pd.read_json(result, orient='records')

    clusters = range(int(nb_clusters))

    cluster = st.selectbox('**Selecciona el cluster o grupo que quieres analizar:**', (clusters))

    df_cluster = ccf.eda_cluster(df_obesity, cluster)

    with st.form('form_analisis'):
        cols_disabled = ["age_range", "bmi", "cc", "rcc", "ict",
                        "risk_factors", "total", "label"]

        df_labeled = st.data_editor(df_cluster, 
                                    width=800,
                                    hide_index=True,
                                    disabled=cols_disabled, 
                                    column_config=COLS_CLUSTER_LABEL)

        submit_data = st.form_submit_button('Guardar Datos')

    if submit_data:
        update_obesity(df_labeled, cluster)
        st.success('¡El etiquetado fue guardado exitosamente!')
else:

    st.warning('Los datos no han sido etiquetados. Debes realizar primero la clasificación y el etiquetado.')
        

    
        