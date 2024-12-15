![Image](./logo.jpg)
# Todo REST API

Une API REST simple pour gérer des tâches à faire (à l'aide du module Python `http.server`), supportant les opérations de type CRUD (Create, Read, Update, Delete).

## Fonctionnalités

- **GET** `/todos` : Récupérer toutes les tâches.
- **GET** `/todos/<id>` : Récupérer une tâche par son ID.
- **POST** `/todos` : Créer une nouvelle tâche.
- **PUT** `/todos/<id>` : Mettre à jour une tâche existante.
- **DELETE** `/todos/<id>` : Supprimer une tâche par son ID.

## Prérequis

- **Python 3.7+**

Aucune dépendance externe n'est requise, le code utilise uniquement la bibliothèque standard de Python.

## Installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/todo-rest-api.git
   cd todo-rest-api
   ```

2. Lancez le serveur :
   ```bash
   python todos_api.py
   ```

3. L'API sera accessible à l'adresse : `http://localhost:8080`

## Utilisation

Vous pouvez tester l'API avec des outils comme [Postman](https://www.postman.com/) ou `curl`.

### Exemples de requêtes

#### 1. Récupérer toutes les tâches
```bash
curl http://localhost:8080/todos
```

#### 2. Créer une nouvelle tâche
```bash
curl -X POST http://localhost:8080/todos -H "Content-Type: application/json" -d '{"title": "Faire les courses"}'
```

#### 3. Mettre à jour une tâche
```bash
curl -X PUT http://localhost:8080/todos/0 -H "Content-Type: application/json" -d '{"title": "Faire les courses et le ménage", "completed": true}'
```

#### 4. Supprimer une tâche
```bash
curl -X DELETE http://localhost:8080/todos/0
```

## Structure du projet

```
.
├── todos_api.py   # Code source de l'API REST
├── README.md      # Documentation du projet
```

## Contributions

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou à soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus d'informations.

---

**Amusez-vous bien avec ce projet !**

