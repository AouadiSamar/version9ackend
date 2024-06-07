#!/bin/bash

# Utiliser Python et Pip directement
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

# Appliquer les migrations de base de données
python manage.py migrate

# Collecter les fichiers statiques
python manage.py collectstatic --noinput
