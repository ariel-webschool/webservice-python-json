import json

# Chemin du fichier pour stocker les données
JSON_FILE = 'todos.json'

def load_todos():
    """Charge les tâches depuis un fichier JSON."""
    try:
        with open(JSON_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Retourne une liste vide si le fichier n'existe pas ou est invalide

def save_todos(todos):
    """Sauvegarde les tâches dans un fichier JSON."""
    with open(JSON_FILE, 'w') as file:
        json.dump(todos, file, indent=4)
