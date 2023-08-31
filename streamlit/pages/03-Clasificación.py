# Carga de librerías

import streamlit as st

import pandas as pd

from src.call_api import obesity_clusters_kmodes, obesity_return_data
import src.clustering_functions as cf
import src.chart_common_functions as ccf

from src.app_config import page_config, sidebar_config

page_config()

sidebar_config()

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

st.subheader('Clasificación de los Datos')

st.markdown('''
    La variable objetivo no existe en el conjunto de datos. 
            
    Se puede utilizar un algoritmo de **Clasificación no Supervisada** para poder identificar grupos de personas con características similares y facilitar el etiquetado de los datos, previo al entrenamiento del algoritmo de clasificación: 
    
    1. Se ejecuta el algoritmo **KModes** con los parámetros indicados.
            
    2. Se muestran los datos de cada grupo (cluster) con sus características para su análisis.
            
    3. Se asigna manualmente una etiqueta a cada grupo o subgrupo.
            
    4. Se actualizan los datos etiquetados en la base de datos.
''')


with st.form('form_clusters'):

    n_clusters = st.number_input('¿Cuántos clusters o grupos deseas?', value=2)
    n_init = st.number_input('Valor para el parámetro **n_init**:', value=1)
    random_state = st.number_input('Valor para el parámetro **random_state**:', value=1)

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

    df_num_cluster = pd.DataFrame(df_obesity.groupby('cluster')['age'].count())
    df_num_cluster.rename(columns={'age': 'num_people'}, inplace=True) 
    df_num_cluster.reset_index(inplace=True)

    theta = 'num_people:Q'
    category = 'cluster:N'
    title = 'Cantidad de personas por cluster o grupo'

    st.altair_chart(ccf.pie_chart(df_num_cluster, theta, category, title))

    st.pyplot(cf.clusters_factors_charts(df_obesity, -1))
    st.altair_chart(cf.clusters_chart(df_obesity), theme=None)
    #st.pyplot(ccf.num_var_correl(df_obesity, 'cluster'))
    st.pyplot(ccf.distribution_var_categ(df_obesity, 'cluster'))
