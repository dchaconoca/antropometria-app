import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import altair as alt 

import src.char_common_functions as ccf

def clusters_char(df):
    x = 'count(*):Q'
    y = 'age_range:O'
    detail = 'cluster:N'

    title='Cantidad de Individuos según su rango de edad y el cluster al que pertenecen'

    title_x = 'Total individuos'
    title_y = 'Rangos de Edad'

    char = ccf.char_bars(df, x, y, detail, title, title_x, title_y)
    return char