#############################################
# Archivo Dockerfile
#############################################
# 1. Es el que se selecciona en Google Cloud Run para construir el contenedor
# 2. Instala Sqlite3 y los requirements
# 3. Copia los archivos en el directorio fuente del contenedor
# 4. Contiene las instrucciones para ejecutar la API

FROM python:3.9

RUN apt-get update && apt-get install -y sqlite3

WORKDIR /code

COPY ./api/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api /code

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]