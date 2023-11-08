# Carga de librerías

import streamlit as st

import pandas as pd

from src.call_api import obesity_clusters_kmodes, obesity_return_data
import src.clustering_functions as cf
import src.chart_common_functions as ccf

from src.app_config import page_config, COEF_SIL_HELP, DB_HELP, CH_HELP, N_INIT_HELP, RDM_STE_HELP

page_config()

#sidebar_config()

st.subheader('Clasificación de los Datos')

st.markdown('''
    La variable objetivo, **grado de riesgo de obesidad**, no existe en el conjunto de datos. 
            
    Se puede utilizar un algoritmo de **Clasificación no Supervisada** para poder identificar grupos de personas con características similares y facilitar el etiquetado de los datos, previo al entrenamiento del algoritmo de clasificación: 
    
    1. Ejecuta el algoritmo **KModes** con los parámetros indicados: 
            
        - El número ideal de clusters o grupos está entre 5 y 6
        - Un buen resultado se obtiene con los parámetros **5 clusters**, **n_init=15**, **ramdon_state=2**
            
    2. Se mostrarán los datos de cada grupo (cluster) con sus características para su análisis.
            
    3. En la parte **Análisis y Etiquetado** podrás analizar los datos grupo por grupo y podrás etiquetarlos.
''')


with st.form('form_clusters'):

    n_clusters = st.number_input('¿Cuántos clusters o grupos deseas?', value=2)
    n_init = st.number_input('Valor para el parámetro **n_init**:', value=10, help=N_INIT_HELP)
    random_state = st.number_input('Valor para el parámetro **random_state**:', value=1, help=RDM_STE_HELP)

    submit = st.form_submit_button('Definir grupos')

if submit:

    params = {
            'n_clusters': n_clusters,
            'n_init': n_init,
            'random_state': random_state
    }

    metrics = obesity_clusters_kmodes(params)

    str_clusters = f'#### Métricas del modelo KModes para {n_clusters} clusters'
    st.markdown(str_clusters)
    col1, col2, col3, col4 = st.columns((1,1,1,1))

    col1.markdown(':orange[**Costo**]')
    col2.markdown(':orange[**Coef. Silhouette**]', help=COEF_SIL_HELP)
    col3.markdown(':orange[**David-Bouldin**]', help=DB_HELP)
    col4.markdown(':orange[**Calinski-Harabasz**]', help=CH_HELP)

    col1.metric(label=' ', value=round(metrics['cost'], 2), label_visibility='hidden')
    col2.metric(label=' ', value=round(metrics['silhouette_score'], 2), label_visibility='hidden')
    col3.metric(label=' ', value=round(metrics['davies_bouldin_score'], 2), label_visibility='hidden')
    col4.metric(label=' ', value=round(metrics['calinski_harabasz_score'], 2), label_visibility='hidden')

    # Análisis de los clusters

    st.markdown('#### Análisis de los grupos o clusters:')

    result = obesity_return_data()

    df_obesity = pd.read_json(result, orient='records')

    theta = 'count(age):Q'
    category = 'cluster:N'
    title = 'Cantidad de personas por cluster o grupo'
    cat_title = 'Cluster'

    st.altair_chart(ccf.pie_chart(df_obesity, theta, category, title, cat_title))

    st.pyplot(cf.clusters_factors_charts(df_obesity, -1))
    st.altair_chart(cf.clusters_chart(df_obesity), theme=None)
    st.pyplot(ccf.num_var_correl(df_obesity, 'cluster'))
    st.pyplot(ccf.distribution_var_categ(df_obesity, 'cluster'))
