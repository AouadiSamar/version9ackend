#!/bin/bash

# Utiliser Python et Pip directement
python -m pip install --upgrade pip
python -m pip install setuptools==65.5.0 wheel
python -m pip install -r requirements.txt

# Appliquer les migrations de base de données
python manage.py migrate

# Collecter les fichiers statiques
python manage.py collectstatic --noinput
