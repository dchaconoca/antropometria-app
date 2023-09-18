#!/usr/bin/env sh

# abort on errors
set -e
clear

# Activate virtuals envs
#source apivenv/bin/activate
#source strmltvenv/bin/activate

# run API
#gnome-terminal
#gnome-terminal --tab #sh "run-api.sh"
uvicorn api:app

# run StreamlitApp
#gnome-terminal
#gnome-terminal -e cd .. / streamlit run streamlit/Inicio.py
# cd ..
# streamlit run streamlit/Inicio.py

# Execute jupyter notebook
# Pregunta si desea ejecutar Jupyter Notebook
echo "¿Desea ejecutar Jupyter Notebook? (Y/N)"
read resp

# Si la respuesta es "Y", ejecuta Jupyter Notebook
# if [[ $resp =~ "Y" ]]; then
#   cd / && jupyter notebook
# fi
