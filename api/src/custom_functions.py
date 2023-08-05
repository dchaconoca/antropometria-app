# Librerías

from pathlib import Path

import pandas as pd

# Seleccionar solo las columnas necesarias 

def select_data(df, col_drop=[], col_leave=[]):
     
    if col_leave:
        df = df.loc[:,col_leave]
    
    if col_drop:
        df.drop(col_drop, axis=1, inplace=True)
    
    return df


def bmi_calc(weight, height):
    height = height/100
    bmi = weight / (height*height)    
    return bmi

def calc_obesity_bmi(bmi):
    if bmi < 18.5: return 0
    if bmi >= 18.5 and bmi < 25 : return 1
    if bmi >= 25 and bmi < 30 : return 2
    if bmi >= 30 : return 3
    
def calc_obesity_bmi_txt(bmi):
    if bmi == 0: return '0-Bajo Peso'
    if bmi == 1 : return '1-Normal'
    if bmi == 2 : return '2-Sobrepeso'
    if bmi == 3 : return '3-Obesidad'
    

# Clasificación según CC: Circunferencia de cadera

def calc_obesity_cc(gender, waist_circum):
    if gender=='male':
        if waist_circum>94.0: return 1            
    if gender=='female':
        if waist_circum>80.0: return 1 
    return 0

def calc_obesity_cc_txt(cc):
    if cc == 0: return '0-Bajo'
    if cc == 1 : return '1-Alto'


# Clasificación según RCC: Racio entre la circunferencia de la cintura y el de la cadera

def calc_obesity_rcc(gender, rcc):

    if gender == 'female':
        if rcc <= 0.8: return 0
        if rcc > 0.8 and rcc <= 0.85 : return 1
        if rcc > 0.85 : return 2
        
    if gender == 'male':
        if rcc <= 0.95: return 0
        if rcc > 0.95 and rcc <= 1 : return 1
        if rcc > 1 : return 2
        
def calc_obesity_rcc_txt(rcc):
    if rcc == 0: return '0-Bajo'
    if rcc == 1: return '1-Medio'
    if rcc == 2: return '2-Alto'
    

# Clasificación ICT: Índice o racio de circunferencia de cintura y talla (estatura)

def calc_obesity_ict(gender, ict):
    
    if gender == 'female':
        if ict <= 0.41: return 0
        if ict > 0.41 and ict <= 0.48 : return 1
        if ict > 0.48 and ict <= 0.57 : return 2
        if ict > 0.57 : return 3
        
    if gender == 'male':
        if ict <= 0.42: return 0
        if ict > 0.42 and ict <= 0.52 : return 1
        if ict > 0.52 and ict <= 0.62 : return 2
        if ict > 0.62 : return 3
        
def calc_obesity_ict_txt(ict):
    if ict == 0 : return '0-Delgado'
    if ict == 1 : return '1-Normal'
    if ict == 2 : return '2-Sobrepeso'
    if ict == 3 : return '3-Obesidad'
           

# Cuántos factores de riesgo posee una persona

def calc_risk_factors(bmi, cc, rcc, ict):  
    
    total = 0
    
    if bmi >= 2: total = total + 1
    if cc >= 1: total = total + 1
    if rcc >= 1: total = total + 1
    if ict >= 2: total = total + 1
        
    return total

def custom_calculus(df):
    
    df['gender_bin'] = df.apply(lambda  row: (1 if row['gender']=='male' else 0), axis=1)
    
    # Calculamos el BMI para cada registro
    df['bmi'] = df.apply(lambda  row: bmi_calc(row['weight'], row['height']) , axis=1)

    # Calculamos el racio cintura / cadera para cada registro
    df['rcc'] = df.apply(lambda  row: row['waist_circum_preferred'] / row['hip_circum'], axis=1)
    
    # Calculamos el racio cintura / talla para cada registro
    df['ict'] = df.apply(lambda  row: row['waist_circum_preferred'] / row['height'], axis=1)
    
    df['obesity_bmi'] = df.apply(lambda  row: calc_obesity_bmi(row['bmi']) , axis=1)
    df['obesity_bmi_txt'] = df.apply(lambda  row: calc_obesity_bmi_txt(row['obesity_bmi']) , axis=1)
    
    df['obesity_cc'] = df.apply(lambda  row: calc_obesity_cc(row['gender'], row['waist_circum_preferred']) , 
                                            axis=1)
    df['obesity_cc_txt'] = df.apply(lambda row: calc_obesity_cc_txt(row['obesity_cc']), axis=1)
    
    df['obesity_rcc'] = df.apply(lambda row: calc_obesity_rcc(row['gender'], row['rcc']), axis=1)
    df['obesity_rcc_txt'] = df.apply(lambda row: calc_obesity_rcc_txt(row['obesity_rcc']), axis=1)
    
    
    df['obesity_ict'] = df.apply(lambda row: calc_obesity_ict(row['gender'], row['ict']) , axis=1)
    df['obesity_ict_txt'] = df.apply(lambda row: calc_obesity_ict_txt(row['obesity_ict']) , axis=1)

    
    df['risk_factors'] = df.apply(lambda  row: calc_risk_factors(row['obesity_bmi'], 
                                                                   row['obesity_cc'], 
                                                                   row['obesity_rcc'],
                                                                   row['obesity_ict']) , 
                                            axis=1)
    
    return df

