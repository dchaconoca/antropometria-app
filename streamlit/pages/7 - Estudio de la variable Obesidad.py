# Carga de librerías

import io

import streamlit as st

import pandas as pd

from src.call_api import obesity_return_new_data, obesity_delete_new_data
import src.eda_functions as ef
import src.chart_common_functions as ccf

from src.app_config import page_config, sidebar_config, COLS_CLUSTER_LABEL

page_config()

#sidebar_config()

def delete_obesity(df):
    deleted = False
    for index, row in df.iterrows():

        if row['Eliminar']:
            params = {
                        'age': row['age'],
                        'gender': row['gender'],
                        'height': row['height'],
                        'weight': row['weight'],
                        'waist_circum_preferred': row['waist_circum_preferred'],
                        'hip_circum': row['hip_circum'],
                        'creation_date': row['creation_date']
                    }
            obesity_delete_new_data(params)

            deleted = True
    
    return deleted


st.subheader('Ver y descargar nuevos datos')

result = obesity_return_new_data()

df_new_data = pd.read_json(result, orient='records')

if df_new_data.size:

    cols=["age", "gender", "height", "weight", "waist_circum_preferred",
            "hip_circum", "obesity_bmi_txt", "obesity_cc_txt", "obesity_rcc_txt",
            "obesity_ict_txt", "risk_factors", "obesity", "real_obesity", 
            "comment", "creation_date"]

    df_new_data = df_new_data.loc[:,cols]
    df_new_data['Eliminar'] = False

    st.markdown('**Selecciona las líneas que deseas eliminar:**')
    df_delete = st.data_editor(df_new_data, 
                                width=900,
                                hide_index=True,
                                disabled=cols, 
                                column_config=COLS_CLUSTER_LABEL)

    if st.button('Eliminar Datos'):
        if delete_obesity(df_delete):
            st.success('¡Los datos fueron eliminados correctamente!')
            st.rerun()
        

    csv = df_new_data.to_csv(index=False)
    download_button = st.download_button(label="Descargar datos como CSV", data=csv, file_name='new_data.csv', mime='text/csv')

else:
    st.warning('No hay datos que mostrar')

