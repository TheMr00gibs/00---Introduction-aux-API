# Utiliser l'image officielle de Python
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt (si vous avez besoin d'installer des packages)
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers du projet dans le répertoire de travail
COPY . .

# Exécuter le fichier app.py
CMD ["python", "api.py"]