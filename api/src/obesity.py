# Librerías
from pathlib import Path

import pandas as pd
import pickle

from pydantic import BaseModel, Field, confloat

from src.custom_functions import custom_calculus, select_data

class PersonObesity(BaseModel):
    age: int = 18
    gender: str = Field(..., description="Género de la persona", pattern="^(female|male)$")
    weight: confloat(gt=0) 
    height: confloat(gt=0)
    waist_circum_preferred: confloat(gt=0) 
    hip_circum: confloat(gt=0) 
    

def make_obesity_prediction(person: PersonObesity):

    CURRENT_DIR = Path.cwd()

    df = pd.DataFrame([person.dict()])
    df_transformed = custom_calculus(df)

    cols_to_leave = ['age', 'gender_bin', 'obesity_cc', 'obesity_bmi', 'obesity_rcc', 'obesity_ict']  
    df_transformed = select_data(df_transformed, [], cols_to_leave)

    with open(f"{CURRENT_DIR}/ml_models/rf_obesity.pkl", "rb") as f:
        trained_model = pickle.load(f)

    df['obesity'] = trained_model.predict(df_transformed) 
  
    result = df.to_dict(orient = 'records')

    return result

