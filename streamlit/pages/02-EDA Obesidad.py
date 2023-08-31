# Carga de librerías

import io

import streamlit as st

import pandas as pd

from src.call_api import obesity_data_etl, obesity_return_data
import src.eda_functions as ef
import src.chart_common_functions as ccf

from src.app_config import page_config, sidebar_config

page_config()

sidebar_config()

st.subheader('Análisis de los Datos sobre Obesidad')

st.markdown('''
    Aquí podrás explorar y analizar los datos sobre Obesidad.
            
    También podrás inicializar la base de datos cargando y transformando los datos originales del archivo:
    [**Civilian American and European Surface Anthropometry Resource, or CAESAR**](https://data.world/andy/caesar/workspace/file?filename=caesar.csv).
    
    Créditos: [Andy R. Terrel](https://data.world/andy)
''')


result = obesity_return_data()

# st.write(result)
# df_obesity = pd.read_json(result, orient='records')

if result:

    df_obesity = pd.read_json(result, orient='records')

    df_eda_f = ef.divide_by_gender(df_obesity, 'female')
    df_eda_m = ef.divide_by_gender(df_obesity, 'male')

    st.markdown('#### Descripción del DataFrame:')

    st.markdown('**Datos numéricos**')
    st.write(df_obesity.describe())
    st.markdown('**Datos no numéricos**')
    st.write(df_obesity.select_dtypes(include=['object']).describe())

    st.dataframe(df_obesity)

    #report = ProfileReport(df_obesity, explorative=True)

    st.markdown("#### Reporte Obesity")
    # @st.cache_data
    # st_profile_report(report)

    st.pyplot(ef.correlation(df_obesity))

    option = st.selectbox('**¿Qué indicador deseas analizar?**',
    ('IMC', 'ICT', 'RCC', 'CC', 'Riesgos'))

    if option == 'IMC':
        st.markdown('#### Estudio Índice de Masa Corporal:')
        st.altair_chart(ef.bmi_char(df_obesity, df_eda_f, df_eda_m), theme=None)
        st.pyplot(ccf.num_var_correl(df_obesity, 'bmi'))
        st.pyplot(ccf.distribution_var_categ(df_obesity, 'bmi'))

    if option == 'ICT':
        st.markdown('#### Estudio Índice Cintura Talla:')
        st.altair_chart(ef.ict_char(df_obesity, df_eda_f, df_eda_m), theme=None)
        st.pyplot(ccf.num_var_correl(df_obesity, 'ict'))
        st.pyplot(ccf.distribution_var_categ(df_obesity, 'ict'))

    if option == 'RCC':
        st.markdown('#### Estudio Relación Cintura Cadera:')
        st.altair_chart(ef.rcc_char(df_obesity, df_eda_f, df_eda_m), theme=None)
        st.pyplot(ccf.num_var_correl(df_obesity, 'rcc'))
        st.pyplot(ccf.distribution_var_categ(df_obesity, 'rcc'))

    if option == 'CC':
        st.markdown('#### Estudio Contorno de Cintura y Grasa Abdominal:')
        st.altair_chart(ef.cc_char(df_obesity, df_eda_f, df_eda_m), theme=None)
        st.pyplot(ccf.num_var_correl(df_obesity, 'waist_circum_preferred'))
        st.pyplot(ccf.distribution_var_categ(df_obesity, 'waist_circum_preferred'))

    if option == 'Riesgos':
        st.markdown('#### Estudio Cantidad de Factores de Riesgo:')
        st.altair_chart(ef.risks_char(df_obesity, df_eda_f, df_eda_m), theme=None)
        st.pyplot(ccf.distribution_var_categ(df_obesity, 'risk_factors'))

with st.form('form_eda'):
    replace = st.radio('¿Deseas reinicializar la base de datos? (Se borrarán todos los datos y se cargarán de nuevo)', 
                    ('Sí', 'No'), horizontal=True)
    submit = st.form_submit_button('OK')

if submit:
    replace = (replace == 'Sí')
    if replace:
        result = obesity_data_etl(replace)
        buffer = io.BytesIO(result)
        df_obesity = pd.read_json(buffer, orient='records')