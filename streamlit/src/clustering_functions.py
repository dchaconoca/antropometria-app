import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt 

import src.chart_common_functions as ccf

def clusters_chart(df):
    x = 'count(*):Q'
    y = 'age_range:O'
    detail = 'cluster:N'

    title='Cantidad de Individuos según su rango de edad y el cluster al que pertenecen'

    title_x = 'Total individuos'
    title_y = 'Rangos de Edad'

    char = ccf.bars_chart(df, x, y, detail, title, title_x, title_y)
    return char


def define_label(bmi, cc, rcc, ict):
    return bmi + '-' + cc + '-' + rcc + '-' + ict

def cluster_labels_chart(df):
    
    title = 'Cantidad de individuos por etiqueta'
    
    tooltip=[alt.Tooltip('label:N'),
             alt.Tooltip('sum(total):Q', title='Cantidad individuos')]
    
    bars = alt.Chart(df).mark_bar().encode(
        x='sum(total):Q',
        y='label:N',
        tooltip=tooltip,
        color=alt.Color('label:N') 
    ).properties(
        title=title,
        width=700, 
        height=400
    )

    return bars

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
    fig.suptitle(f"Candidad de individuos según factor", fontsize = 20, fontweight = "bold")

    return fig

def eda_cluster(df, cluster):   
    
    st.markdown(f'#### EDA cluster {cluster}')
    
    query = f'cluster=={cluster}'
    df_table = df.query(query)[['age_range',
                                'obesity_bmi_txt', 'obesity_cc_txt',  
                                'obesity_rcc_txt', 'obesity_ict_txt', 
                                'risk_factors', 'obesity', 'cluster']]

    df_eda_cluster = pd.pivot_table(df_table, 
                                index=['age_range',
                                       'obesity_bmi_txt', 'obesity_cc_txt',  
                                       'obesity_rcc_txt', 'obesity_ict_txt', 
                                       'risk_factors', 'obesity'],
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
    
    fig = clusters_factors_charts(df, cluster)

    st.pyplot(fig)

    char = cluster_labels_chart(df_eda_cluster)

    st.altair_chart(char)

    return df_eda_cluster
    