# Librerías
from pathlib import Path
import datetime 

import pandas as pd
import pickle

from pydantic import BaseModel, Field, confloat, conint, constr
from typing import Optional

from src.obesity_etl_functions import custom_calculus, load_clean_transform, calc_age_range
from src.obesity_kmodes_functions import generate_kmodes_clusters
from src.data_common_functions import select_data
from src.bd import CURRENT_DIR, URL_DB, open_connection, close_connection, exec_query_result, exec_query


class PersonObesity(BaseModel):
    age: int = 18
    gender: str = Field(..., description="Género de la persona", pattern="^(female|male)$")
    weight: confloat(gt=0) 
    height: confloat(gt=0)
    waist_circum_preferred: confloat(gt=0) 
    hip_circum: confloat(gt=0) 

class PredictedObesityTable(BaseModel):
    age: float
    age_range: constr(regex='^(17-25|26-35|36-45|46-55|56-65|66-100)$')
    gender:  str = Field(..., description="Género de la persona", pattern="^(female|male)$")
    height: float
    weight: float
    waist_circum_preferred: float
    hip_circum: float
    gender_bin: int
    bmi: float
    rcc: float
    ict: float
    obesity_bmi: int
    obesity_bmi_txt: str
    obesity_cc: int
    obesity_cc_txt: str
    obesity_rcc: int
    obesity_rcc_txt: str
    obesity_ict: int
    obesity_ict_txt: str
    risk_factors: int
    obesity: int
    real_obesity: Optional[int] = None
    comment: Optional[str] = None
    creation_date: Optional[datetime.datetime] = None

class ObesityTable(BaseModel):
    age: float
    age_range: constr(regex='^(17-25|26-35|36-45|46-55|56-65|66-100)$')
    gender:  str = Field(..., description="Género de la persona", pattern="^(female|male)$")
    height: float
    weight: float
    waist_circum_preferred: float
    hip_circum: float
    gender_bin: int
    bmi: float
    rcc: float
    ict: float
    obesity_bmi: int
    obesity_bmi_txt: str
    obesity_cc: int
    obesity_cc_txt: str
    obesity_rcc: int
    obesity_rcc_txt: str
    obesity_ict: int
    obesity_ict_txt: str
    risk_factors: int
    creation_date: datetime.datetime
    obesity: Optional[int] = None
    obesity_date: Optional[datetime.datetime] = None
    cluster: Optional[int] = None
    cluster_kmodes_date: Optional[datetime.datetime] = None

class ParamsKModes(BaseModel):
    n_clusters: conint(gt=1)
    n_init: conint(gt=0)
    random_state: conint(gt=0)

class ParamsObesity(BaseModel):
    obesity: Optional[int] = None
    cluster: Optional[int] = None
    age_range: Optional[str] = None
    bmi: Optional[int] = None
    cc: Optional[int] = None
    rcc: Optional[int] = None
    ict: Optional[int] = None

def save_data_obesity(df, table, repĺace=True):
    conn = open_connection()
    action = ('replace' if repĺace else 'append') 
    df.to_sql(table, conn, if_exists=action, index=False)
    close_connection(conn)

def update_data_obesity(query):
    conn = open_connection()
    exec_query(query, conn)
    close_connection(conn)

def return_data_obesity():
    conn = open_connection()
    query = f'SELECT * FROM obesity'
    result = pd.read_sql_query(query, conn)
    #result = exec_query_result(query, conn, True)
    close_connection(conn)
    return result

def return_number_clusters():
    conn = open_connection()
    query = f'SELECT MAX(cluster) + 1 FROM obesity'
    result = exec_query_result(query, conn, False)
    close_connection(conn)
    return result[0]

def make_obesity_prediction(person: PersonObesity):
    person = person.dict()
    df = pd.DataFrame([person])
    df_transformed = custom_calculus(df)

    cols_to_leave = ['age', 'gender_bin', 'obesity_cc', 'obesity_bmi', 'obesity_rcc', 'obesity_ict']  
    df_transformed = select_data(df_transformed, [], cols_to_leave)

    with open(f"{CURRENT_DIR}/ml_models/rf_obesity.pkl", "rb") as f:
        trained_model = pickle.load(f)

    df['obesity'] = trained_model.predict(df_transformed) 
    df['age_range'] = calc_age_range(person['age'])

    # save_data_obesity(df, 'PredictedObesity', False)
 
    items = df.to_dict(orient = 'records')
    validated_items = [PredictedObesityTable(**item) for item in items]
    return validated_items

def make_obesity_data_etl(replace=True):

    if replace:
        columns_to_drop = []
        columns_to_leave = [
            'age',
            'age_range',
            'gender',
            'height',
            'weight',
            'waist_circum_preferred',
            'hip_circum'
        ]

        df_obesity = load_clean_transform(columns_to_drop, columns_to_leave, 
                                        transform=True)
        
        ## Workflow: Salvaguarda
        ########################################
        df_obesity['creation_date'] = datetime.datetime.now() 
        df_obesity['obesity']= None
        df_obesity['obesity_date'] = None
        df_obesity['cluster'] = None
        df_obesity['cluster_kmodes_date'] = None
                
        save_data_obesity(df_obesity, 'Obesity', replace)
        
    result = return_data_obesity()

    items = result.to_dict(orient = 'records')
    validated_items = [ObesityTable(**item) for item in items]
    return validated_items

def make_clusters_kmodes(params: ParamsKModes):
    params = params.dict()

    df_obesity = return_data_obesity()

    (df_obesity, metrics) = generate_kmodes_clusters(df_obesity, 
                                                     params['n_clusters'], 
                                                     params['n_init'], 
                                                     params['random_state'])
    
    df_obesity['cluster_kmodes_date'] = datetime.datetime.now() 
    save_data_obesity(df_obesity, 'Obesity')

    return metrics

def update_obesity(params: ParamsObesity):
    params = params.dict()

    query = f"UPDATE obesity SET obesity = {params['obesity']}, obesity_date = '{datetime.datetime.now()}' "

    # if params['cluster']:
    #     query_where = f"cluster={params['cluster'] }"
    # else:
    query_where = f"WHERE cluster={params['cluster']} AND "
    query_where = query_where + f"age_range='{params['age_range']}' AND "
    query_where = query_where + f"obesity_bmi={params['bmi']} AND "
    query_where = query_where + f"obesity_cc={params['cc']} AND "
    query_where = query_where + f"obesity_rcc={params['rcc']} AND "
    query_where = query_where + f"obesity_ict={params['ict']} "

    query = query + query_where

    return update_data_obesity(query)

def save_obesity_predicted(info: PredictedObesityTable):

    info = info.dict()

    df = pd.DataFrame(info, index=[0])
    df['creation_date'] = datetime.datetime.now()
    
    save_data_obesity(df, 'PredictedObesity', False)

    items = df.to_dict(orient = 'records')
    validated_items = [PredictedObesityTable(**item) for item in items]
    return validated_items
    

