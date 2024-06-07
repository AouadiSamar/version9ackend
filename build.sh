#!/bin/bash

# Utiliser Python et Pip directement
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt

# Appliquer les migrations de base de données
python3 manage.py migrate

# Collecter les fichiers statiques
python3 manage.py collectstatic --noinput
