1. Fonctionnalités
✔ Serveur

Gère une liste de tâches en mémoire

Reçoit des commandes depuis les clients

Peut servir plusieurs clients en parallèle (threads)

✔ Client

Interface console simple (menu)

Envoie des commandes au serveur

Affiche les réponses du serveur

✔ Tâches

Chaque tâche contient :

id (unique, entier)

titre

description

statut (TODO / DOING / DONE)

auteur

🧱 2. Architecture du projet
mini_projet_poo/
│
├─ server/
│  ├─ __init__.py
│  ├─ task.py              # Classe Tache
│  ├─ manager.py           # Classe GestionnaireTaches
│  ├─ server.py            # Serveur TCP
│  └─ Dockerfile           # Docker du serveur
│
├─ client/
│  ├─ __init__.py
│  ├─ client.py            # Client TCP + menu
│  └─ Dockerfile           # (optionnel)
│
├─ docker-compose.yml      # Lancement serveur + clients
├─ .gitignore
└─ README.txt

🔌 3. Protocole de communication (texte)
👉 Commandes client → serveur :
ADD;titre;description;auteur
LIST
DEL;id
STATUS;id;TODO/DOING/DONE

👉 Réponses serveur → client :
OK;id
LIST;id;titre;description;statut;auteur|id;...
ERROR;message

▶️ 4. Exécution SANS Docker
✔ Lancer le serveur
cd server
python server.py


Par défaut : port 5000

✔ Lancer un client

Dans un autre terminal :

cd client
python client.py


Le client demande :

Adresse du serveur (ex : 127.0.0.1) :
Port (ex : 5000) :


Puis un menu apparaît :

1. Ajouter une tâche
2. Lister les tâches
3. Supprimer une tâche
4. Changer le statut
5. Quitter

🐳 5. Exécution AVEC Docker
✔ 5.1 Dockeriser le serveur

Exécuter dans /server :

docker build -t task-server .
docker run -p 5000:5000 task-server

✔ 5.2 Dockeriser le client (optionnel)
docker build -t task-client .
docker run -it task-client

🧩 6. docker-compose (facultatif mais conseillé)

Fichier fourni :

docker-compose up --build


Lance automatiquement :

1 serveur exposé sur 5000

clients optionnels (si activés)

🌿 7. Git — organisation du dépôt

Branches recommandées :

main          → version stable
dev           → intégration
feature/server
feature/client
feature/docker
feature/readme


Bonnes pratiques suivies :

commits fréquents

messages clairs

README complet

.gitignore fourni

⭐ 8. Fonctionnalités implémentées

 - Ajout de tâches

 - Liste des tâches

 - Suppression par id

 - Changement de statut

 - Multi-clients (threads)

 - Dockerisation du serveur

 - (Optionnel) Dockerisation du client