from fastapi import FastAPI
import src.obesity as ob

app = FastAPI() 

@app.get("/")
def read_root():
    print('hola')
    return {'message': 'API Medidas Antropométricas'}

# Return obesity prediction for a person
@app.post('/obesity_prediction')
async def obesity_prediction(person: ob.PersonObesity):
    result = ob.make_obesity_prediction(person)
    return result

# Save obesity prediction and real information
@app.patch('/obesity_prediction')
async def save_obesity_information(info: ob.PredictedObesityTable):
    result = ob.save_obesity_predicted(info)
    return result

# Return all data for obesity
@app.get('/obesity_data')
async def return_obesity_data():
    result = ob.return_data_obesity()
    items = result.to_dict(orient = 'records')
    validated_items = [ob.ObesityTable(**item) for item in items]
    return validated_items


# Update obesity variable in obesity table
@app.patch('/obesity_data')
async def update_obesity(params: ob.ParamsObesity):
    result = ob.update_obesity(params)

# Make obesity etl and return all data
@app.post('/obesity_data_etl/{replace}')
async def obesity_data_etl(replace: bool):
    result = ob.make_obesity_data_etl(replace)
    #result = result.to_dict(orient = 'records')
    return result

# Create KModes clusters
@app.post('/clusters_kmodes')
async def clusters_kmodes(params: ob.ParamsKModes):
    result = ob.make_clusters_kmodes(params)
    return result

# Return number of clusters
@app.get('/nb_clusters')
async def return_nb_clusters():
    result = ob.return_number_clusters()
    return result