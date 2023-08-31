#################################
## Char Common Functions
#################################

import streamlit as st

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import altair as alt 


# Gráfico de distribución para cada variable numérica
def num_var_distribution(df):
    fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(12, 10))
    axes = axes.flat
    col_num = df.select_dtypes(include=['float64', 'int64']).columns

    colormap = sns.color_palette('Oranges')

    for i, colum in enumerate(col_num):
        sns.histplot(
            data     = df,
            x        = colum,
            stat     = "count",
            kde      = True,
            color    = colormap, #(list(plt.rcParams['axes.prop_cycle'])*2)[i]["color"],
            line_kws = {'linewidth': 2},
            alpha    = 0.3,
            ax       = axes[i]
        )
        axes[i].set_title(colum, fontsize = 12, fontweight = "bold")
        axes[i].tick_params(labelsize = 8)
        axes[i].set_xlabel("")


    fig.tight_layout()
    plt.subplots_adjust(top = 0.9)
    fig.suptitle('Distribución variables numéricas', fontsize = 20, fontweight = "bold")

    return fig


# Gráfico de la correlación de una variable dada con respecto a cada variable numérica 
def num_var_correl(df, col):

    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(12, 10))
    axes = axes.flat
    col_num = df.select_dtypes(include=['float64']).columns
    if col in col_num: #df[col].dtype == np.float64 or df[col].dtype == np.int: 
        col_num = col_num.drop(col)

    for i, colum in enumerate(col_num):
        sns.regplot(
            x           = df[col],
            y           = df[colum],
            color       = "orange",
            marker      = '.',
            scatter_kws = {"alpha":0.4},
            line_kws    = {"color":"r","alpha":0.7},
            ax          = axes[i]
        )
        axes[i].set_title(f"{col} vs {colum}", fontsize = 12, fontweight = "bold")
        axes[i].ticklabel_format(style='sci', scilimits=(-4,4), axis='both')
        axes[i].yaxis.set_major_formatter(ticker.EngFormatter())
        axes[i].xaxis.set_major_formatter(ticker.EngFormatter())
        axes[i].tick_params(labelsize = 8)
        axes[i].set_xlabel("")
        axes[i].set_ylabel("")

    fig.tight_layout()
    plt.subplots_adjust(top=0.9)
    fig.suptitle(f"Correlación con {col}", fontsize = 20, fontweight = "bold")

    return fig
    
    
    
# Gráfico relación entre una variable dada y cada variable categórica
def distribution_var_categ(df, col, invert=False):
    fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(18, 15))
    axes = axes.flat
    if invert:
        object_cols = df.select_dtypes(include=['float64']).columns
    else:
        object_cols = df.select_dtypes(include=['object']).columns
    
    for i, colum in enumerate(object_cols):
        if invert:
            axe_x = col
            axe_y = colum
        else:
            axe_x = colum
            axe_y = col
            
        sns.violinplot(
            x     = axe_x,
            y     = axe_y,
            data  = df,
            color = "orange",
            ax    = axes[i]
        )
        axes[i].set_title(f"{col} vs {colum}", fontsize = 15, fontweight = "bold")
        axes[i].yaxis.set_major_formatter(ticker.EngFormatter())
        axes[i].tick_params(labelsize = 15)
        axes[i].set_xlabel("")
        axes[i].set_ylabel("")

    # Se eliminan los axes vacíos
    for i in [6, 7, 8]:
        fig.delaxes(axes[i])

    fig.tight_layout()
    plt.subplots_adjust(top=0.9)
    fig.suptitle(f'Distribución de {col} por variable categórica', fontsize = 20, fontweight = "bold")
    
    return fig

# Create a horizontal bar char with Altair
# Each bar is a categorie
def bars_chart(df, x_in, y_in, detail, title, title_x, title_y):
    
    x = alt.X(x_in, title = title_x, stack='zero', 
          axis = alt.Axis(format = ",.2s", grid=True, titleAnchor='middle', labelFontSize=12))
    y = alt.Y(y_in, title=title_y, axis = alt.Axis(labelAngle=0, labelFontSize=10))
    
    tooltip=[alt.Tooltip(detail, title='Grado de obesidad'),
             alt.Tooltip(y_in, title='Rango de edad'),
             alt.Tooltip(x_in, title='Cantidad individuos')]

    bars = alt.Chart(df).mark_bar().encode(
        x=x,
        y=y,
        tooltip=tooltip,
        color=alt.Color(detail) 
    ).properties(
        title=title,
        width=550, 
        height=300
    )

    text = alt.Chart(df).mark_text(dx=-12, dy=3, color='white').encode(
        x=alt.X(x_in, stack='zero'),
        y=y_in,
        detail=detail,
        text=alt.Text(x_in)
    )
    
    final_graph = bars + text
    
    return final_graph

# pie_chart
# Crea un gráfico de sectores de las líneas de productos
#
# Parámetros: 
#     df: DataFrame a utilizar
#     theta: Datos que se van a graficar
#     texto: Texto que se mostrará en el cada sector del gráfico
#     titulo: Título del gráfico
def pie_chart(df, theta_in, category, title):

    theta = alt.Theta(theta_in, stack=True)
    text = alt.Text(theta_in) 

    base = alt.Chart(df).encode(
        theta=theta, 
        color=alt.Color(category, scale=alt.Scale(scheme='Oranges'))
    ).properties(title=title)

    pie = base.mark_arc(outerRadius=130, innerRadius=20)

    text = base.mark_text(radius=110, size=20, fill='black').encode(
           text=text
           )
    
    chart = pie + text

    return chart

