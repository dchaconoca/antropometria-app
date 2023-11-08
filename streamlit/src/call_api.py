import requests
import json
import io

import streamlit as st

URL_BASE = 'https://antropo-api-ft3evlkfyq-rj.a.run.app'

#URL_BASE = 'http://127.0.0.1:8000'

#URL_BASE = 'http://localhost'

def obesity_prediction(person):
      
      url = URL_BASE + '/obesity_prediction'                  
      person = json.dumps(person) 

      try:
            response = requests.post(url,
                              headers={'Content-Type': 'application/json'},
                              data=person,
                              timeout=8000)
            
            return json.loads(response.content)
      
      except requests.exceptions.RequestException as e:
            # Manejar errores de solicitud (por ejemplo, problemas de red)
            st.error("Error de solicitud a la API: " + str(e))
            st.stop()

      except requests.exceptions.HTTPError as e:
            # Manejar errores de respuesta HTTP (por ejemplo, códigos de estado no exitosos)
            st.error("Error HTTP de la API: " + str(e))
            st.stop()

      except Exception as e:
            # Manejar cualquier otro error inesperado
            st.error("Error inesperado: " + str(e))
            st.stop()

def save_obesity_info(info):
      
      url = URL_BASE + '/obesity_prediction'                  
      info = json.dumps(info) 

      try:
            response = requests.patch(url,
                              headers={'Content-Type': 'application/json'},
                              data=info,
                              timeout=8000)
            return json.loads(response.content)
      
      except requests.exceptions.RequestException as e:
            # Manejar errores de solicitud (por ejemplo, problemas de red)
            st.error("Error de solicitud a la API: " + str(e))
            st.stop()

      except requests.exceptions.HTTPError as e:
            # Manejar errores de respuesta HTTP (por ejemplo, códigos de estado no exitosos)
            st.error("Error HTTP de la API: " + str(e))
            st.stop()

      except Exception as e:
            # Manejar cualquier otro error inesperado
            st.error("Error inesperado: " + str(e))
            st.stop()


def obesity_data_etl(replace):
      
      url = URL_BASE + f'/obesity_data_etl/{replace}'

      try:
            response = requests.post(url,
                              headers={'Content-Type': 'application/json'},
                              timeout=8000)
            
            result = io.BytesIO(response.content)
            return result
      
      except requests.exceptions.RequestException as e:
            # Manejar errores de solicitud (por ejemplo, problemas de red)
            st.error("Error de solicitud a la API: " + str(e))
            st.stop()

      except requests.exceptions.HTTPError as e:
            # Manejar errores de respuesta HTTP (por ejemplo, códigos de estado no exitosos)
            st.error("Error HTTP de la API: " + str(e))
            st.stop()

      except Exception as e:
            # Manejar cualquier otro error inesperado
            st.error("Error inesperado: " + str(e))
            st.stop()


def obesity_return_data():
      
      url = URL_BASE + f'/obesity_data'

      try:
            response = requests.get(url,
                              headers={'Content-Type': 'application/json'},
                              timeout=8000)
            result = io.BytesIO(response.content)
            return result
      
      except requests.exceptions.RequestException as e:
            # Manejar errores de solicitud (por ejemplo, problemas de red)
            st.error("Error de solicitud a la API: " + str(e))
            st.stop()

      except requests.exceptions.HTTPError as e:
            # Manejar errores de respuesta HTTP (por ejemplo, códigos de estado no exitosos)
            st.error("Error HTTP de la API: " + str(e))
            st.stop()

      except Exception as e:
            # Manejar cualquier otro error inesperado
            st.error("Error inesperado: " + str(e))
            st.stop()


def obesity_clusters_kmodes(params):
      
      url = URL_BASE + '/clusters_kmodes'                  
      params = json.dumps(params) 

      try:
            response = requests.post(url,
                              headers={'Content-Type': 'application/json'},
                              data=params,
                              timeout=8000)
            
            return json.loads(response.content)
      
      except requests.exceptions.RequestException as e:
            # Manejar errores de solicitud (por ejemplo, problemas de red)
            st.error("Error de solicitud a la API: " + str(e))
            st.stop()

      except requests.exceptions.HTTPError as e:
            # Manejar errores de respuesta HTTP (por ejemplo, códigos de estado no exitosos)
            st.error("Error HTTP de la API: " + str(e))
            st.stop()

      except Exception as e:
            # Manejar cualquier otro error inesperado
            st.error("Error inesperado: " + str(e))
            st.stop()


def obesity_update_var(params):
      
      url = URL_BASE + f'/obesity_data'                
      params = json.dumps(params) 

      try:
            response = requests.patch(url,
                              headers={'Content-Type': 'application/json'},
                              data=params,
                              timeout=8000)
            
            return json.loads(response.content)
      
      except requests.exceptions.RequestException as e:
            # Manejar errores de solicitud (por ejemplo, problemas de red)
            st.error("Error de solicitud a la API: " + str(e))
            st.stop()

      except requests.exceptions.HTTPError as e:
            # Manejar errores de respuesta HTTP (por ejemplo, códigos de estado no exitosos)
            st.error("Error HTTP de la API: " + str(e))
            st.stop()

      except Exception as e:
            # Manejar cualquier otro error inesperado
            st.error("Error inesperado: " + str(e))
            st.stop()

def obesity_return_nb_clusters():
      
      url = URL_BASE + f'/nb_clusters'

      try:
            response = requests.get(url,
                              headers={'Content-Type': 'application/json'},
                              timeout=8000)
            
            return json.loads(response.content) #response.content
      
      except requests.exceptions.RequestException as e:
            # Manejar errores de solicitud (por ejemplo, problemas de red)
            st.error("Error de solicitud a la API: " + str(e))
            st.stop()

      except requests.exceptions.HTTPError as e:
            # Manejar errores de respuesta HTTP (por ejemplo, códigos de estado no exitosos)
            st.error("Error HTTP de la API: " + str(e))
            st.stop()

      except Exception as e:
            # Manejar cualquier otro error inesperado
            st.error("Error inesperado: " + str(e))
            st.stop()

