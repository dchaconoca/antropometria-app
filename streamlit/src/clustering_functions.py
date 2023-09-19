import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt 

import src.chart_common_functions as ccf

from src.app_config import LABEL_SIZE, TITLE_SIZE

def clusters_chart(df):
    x = 'count(*):Q'
    y = 'age_range:O'
    detail = 'cluster:N'

    title='Cantidad de Individuos por rango de edad y el Cluster asignado'

    title_x = 'Total individuos'
    title_y = 'Rangos de Edad'

    char = ccf.bars_chart(df, x, y, detail, title, title_x, title_y)
    return char


def define_label(bmi, cc, rcc, ict):
    return bmi + '-' + cc + '-' + rcc + '-' + ict

def cluster_labels_chart(df):
    
    title = 'Cantidad de individuos por etiqueta'
    
    tooltip=[alt.Tooltip('label:N', title='Etiqueta o grupo'),
             alt.Tooltip('sum(total):Q', title='Cantidad individuos')]
    
    bars = alt.Chart(df).mark_bar().encode(
        x=alt.X('sum(total):Q', title='Total personas'),
        y=alt.Y('label:N', title='Etiqueta o grupo'),
        tooltip=tooltip,
        color=alt.Color(
        'label:N', title='Etiqueta o grupo', legend=alt.Legend(orient="bottom", titleOrient="left")
        )
    ).properties(
        title={
                "text": title,
                #"color": "orange",  # Cambiar color del título
                "fontSize": TITLE_SIZE    # Cambiar tamaño de la fuente del título
            },
        width=700, 
        height=400
    )

    return bars

def obesity_chart(df):

    chart = alt.Chart(df, width=500, height=alt.Step(10)).mark_bar().encode(
    y=alt.Y('label:N', axis=None),
    x=alt.X('sum(total):Q', title='Total personas'),
    color=alt.Color(
        'label:N', title='Etiqueta o grupo', legend=alt.Legend(orient="bottom", titleOrient="left")
    ),
    tooltip=[alt.Tooltip('label:N', title='Etiqueta'),
             alt.Tooltip('sum(total):Q', title='Cantidad individuos'),
             alt.Tooltip('obesity:N', title='Grado de Riesgo')],
    row=alt.Column("obesity:N", title="Grado de Riesgo", 
                header=alt.Header(labelAngle=0, 
                                  labelFontSize=TITLE_SIZE,
                                  titleFontSize=LABEL_SIZE)),
    ).properties(
        title={
            "text": "Cantidad de Personas por Etiqueta y Grado de Riesgo de Obesidad",
            #"color": "orange",  # Cambiar color del título
            "fontSize": TITLE_SIZE    # Cambiar tamaño de la fuente del título
        }
    )

    return chart


def clusters_factors_charts(df, cluster):
    if cluster >= 0:
        query = f'cluster=={cluster}'
        df = df.query(query)[['cluster', 'age_range', 'risk_factors', 'gender']]
    else:
        df = df[['cluster', 'age_range', 'risk_factors', 'gender']]

    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
    

    sns.countplot(x='cluster', hue='risk_factors', data=df, ax=ax1)
    sns.countplot(x='cluster', hue='age_range', data=df, ax=ax2)
    sns.countplot(x='cluster', hue='gender', data=df, ax=ax3)

    fig.tight_layout()
    plt.subplots_adjust(top=0.9)
    fig.suptitle(f"Candidad de individuos según factor", fontsize = TITLE_SIZE, fontweight = "bold")

    return fig

def eda_cluster(df, cluster):      
    query = f'cluster=={cluster}'
    df_table = df.query(query)[['age_range',
                                'obesity_bmi_txt', 'obesity_cc_txt',  
                                'obesity_rcc_txt', 'obesity_ict_txt', 
                                'risk_factors', 'obesity', 'cluster']]
    
    if df_table.obesity.isnull().any():
        index_cols = ['age_range',
                        'obesity_bmi_txt', 'obesity_cc_txt',  
                        'obesity_rcc_txt', 'obesity_ict_txt', 
                        'risk_factors']
    else:
        index_cols = ['age_range',
                        'obesity_bmi_txt', 'obesity_cc_txt',  
                        'obesity_rcc_txt', 'obesity_ict_txt', 
                        'obesity', 'risk_factors']
    
    df_eda_cluster = pd.pivot_table(df_table, 
                                index=index_cols,
                                    aggfunc='count')   
       
    df_eda_cluster.reset_index(inplace=True)
    
    df_eda_cluster.rename(columns={'obesity_bmi_txt': 'bmi',
                                  'obesity_cc_txt': 'cc',
                                  'obesity_rcc_txt': 'rcc',
                                  'obesity_ict_txt': 'ict',
                                  'cluster': 'total'
                                 }, inplace=True)  
       
    df_eda_cluster['label'] = df_eda_cluster.apply(lambda  row: define_label(row['bmi'], row['cc'],
                                                                      row['rcc'], row['ict']), axis=1)

    total = df_table.shape[0]
    st.markdown(f'#### Estudio cluster **{cluster}** - {total} personas')

    fig = clusters_factors_charts(df, cluster)
    st.pyplot(fig)

    labels_chart = cluster_labels_chart(df_eda_cluster)
    st.altair_chart(labels_chart)

    return df_eda_cluster
    