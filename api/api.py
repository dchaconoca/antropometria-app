from fastapi import FastAPI
from src.obesity import make_obesity_prediction, PersonObesity

app = FastAPI() 

@app.get("/")
def read_root():
    print('hola')
    return {'message': 'API Medidas Antropométricas'}

@app.post('/obesity')
async def obesity_prediction(person: PersonObesity):
    result = make_obesity_prediction(person)
    return result

