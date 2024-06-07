# Utiliser l'image officielle de Python
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de l'application
COPY . /app

# Installer les dépendances
RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

# Appliquer les migrations de base de données
RUN python manage.py migrate

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port de l'application
EXPOSE 8000

# Lancer l'application
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
