# Carga de librerías

import io

import streamlit as st

import pandas as pd

from src.call_api import obesity_return_new_data
import src.eda_functions as ef
import src.chart_common_functions as ccf

from src.app_config import page_config, sidebar_config

page_config()

#sidebar_config()

st.subheader('Ver y descargar nuevos datos')

result = obesity_return_new_data()

if result:

    df_new_data = pd.read_json(result, orient='records')

    st.write(df_new_data)

    csv = df_new_data.to_csv(index=False)
    download_button = st.download_button(label="Descargar datos como CSV", data=csv, file_name='new_data.csv', mime='text/csv')

