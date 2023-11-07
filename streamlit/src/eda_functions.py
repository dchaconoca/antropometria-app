import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import altair as alt 

import src.chart_common_functions as ccf

def divide_by_gender(df, val):

    query = f"gender == '{val}'"

    df = df.query(query)
        
    return df

def correlation(df):

    colormap = sns.color_palette('Oranges')

    corr_df = df.corr(method='pearson', numeric_only=True)

    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(corr_df, annot=True, cmap=colormap)
    ax.set_title('Matriz de Correlación', fontsize=14, weight='bold')   

    return fig

def bmi_char(df, df_eda_f, df_eda_m):
    x = 'count(*):Q'
    y = 'age_range:O'
    detail = 'obesity_bmi_txt:N'

    title='Cantidad de Individuos según su rango de edad y grado de Obesidad según su IMC'
    title_f='Sólo Mujeres'
    title_m='Sólo Hombres'

    title_x = 'Total individuos'
    title_y = 'Rangos de Edad'

    char_todo = ccf.bars_chart(df, x, y, detail, title, title_x, title_y)
    char_f = ccf.bars_chart(df_eda_f, x, y, detail, title_f, title_x, title_y)
    char_m = ccf.bars_chart(df_eda_m, x, y, detail, title_m, title_x, title_y)

    char_total = alt.vconcat(char_todo, char_f, char_m)

    return char_total

def ict_char(df, df_eda_f, df_eda_m):
    x = 'count(*):Q'
    y = 'age_range:O'
    detail = 'obesity_ict_txt:N'

    title='Cantidad de Individuos según su rango de edad y grado de Obesidad según su ICT'
    title_f='Sólo Mujeres'
    title_m='Sólo Hombres'

    title_x = 'Total individuos'
    title_y = 'Rangos de Edad'

    char_todo = ccf.bars_chart(df, x, y, detail, title, title_x, title_y)
    char_f = ccf.bars_chart(df_eda_f, x, y, detail, title_f, title_x, title_y)
    char_m = ccf.bars_chart(df_eda_m, x, y, detail, title_m, title_x, title_y)

    char_total = alt.vconcat(char_todo, char_f, char_m)

    return char_total

def rcc_char(df, df_eda_f, df_eda_m):
    x = 'count(*):Q'
    y = 'age_range:O'
    detail = 'obesity_rcc_txt:N'

    title='Cantidad de Individuos según su rango de edad y riesgo de Obesidad según su RCC'
    title_f='Sólo Mujeres'
    title_m='Sólo Hombres'

    title_x = 'Total individuos'
    title_y = 'Rangos de Edad'

    char_todo = ccf.bars_chart(df, x, y, detail, title, title_x, title_y)
    char_f = ccf.bars_chart(df_eda_f, x, y, detail, title_f, title_x, title_y)
    char_m = ccf.bars_chart(df_eda_m, x, y, detail, title_m, title_x, title_y)

    char_total = alt.vconcat(char_todo, char_f, char_m)

    return char_total

def cc_char(df, df_eda_f, df_eda_m):
    x = 'count(*):Q'
    y = 'age_range:O'
    detail = 'obesity_cc_txt:N'

    title='Cantidad de Individuos según su rango de edad y riesgo de Obesidad según su CC'
    title_f='Sólo Mujeres'
    title_m='Sólo Hombres'

    title_x = 'Total individuos'
    title_y = 'Rangos de Edad'

    char_todo = ccf.bars_chart(df, x, y, detail, title, title_x, title_y)
    char_f = ccf.bars_chart(df_eda_f, x, y, detail, title_f, title_x, title_y)
    char_m = ccf.bars_chart(df_eda_m, x, y, detail, title_m, title_x, title_y)

    char_total = alt.vconcat(char_todo, char_f, char_m)

    return char_total

def risks_char(df, df_eda_f, df_eda_m):
    x = 'count(*):Q'
    y = 'age_range:O'
    detail = 'risk_factors:N'

    title='Cantidad de Individuos según su rango de edad y cantidad de factores de riesgo'
    title_f='Sólo Mujeres'
    title_m='Sólo Hombres'

    title_x = 'Total individuos'
    title_y = 'Rangos de Edad'

    char_todo = ccf.bars_chart(df, x, y, detail, title, title_x, title_y)
    char_f = ccf.bars_chart(df_eda_f, x, y, detail, title_f, title_x, title_y)
    char_m = ccf.bars_chart(df_eda_m, x, y, detail, title_m, title_x, title_y)

    char_total = alt.vconcat(char_todo, char_f, char_m)

    return char_total