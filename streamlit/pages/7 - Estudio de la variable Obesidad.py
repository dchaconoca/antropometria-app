# Carga de librerías

import io

import streamlit as st

import pandas as pd

from src.call_api import obesity_data_etl, obesity_return_data
import src.eda_functions as ef
import src.chart_common_functions as ccf

from src.app_config import page_config, sidebar_config

page_config()

#sidebar_config()

st.subheader('En Construcción')

