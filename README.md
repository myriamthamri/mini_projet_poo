**Structure du projet :**



mini\_projet\_poo/

│

├─ server/

│  ├─ \_\_init\_\_.py

│  ├─ task.py              # Classe Tache

│  ├─ manager.py           # Classe GestionnaireTaches

│  ├─ server.py           # Serveur TCP

│  └─ Dockerfile           # Docker du serveur

│

├─ client/

│  ├─ \_\_init\_\_.py

│  ├─ client.py           # Client TCP + menu

│  └─ Dockerfile         

│

├─ docker-compose.yml      # Lancement serveur + clients

├─ .gitignore

└─ README.txt



**Lancement du projet :**



1️⃣ Construire les images

docker compose build



2️⃣ Lancer uniquement le serveur

docker compose up server





---> Le serveur reste actif et écoute sur le port défini dans docker-compose.yml.



3️⃣ Lancer le client

docker compose run --rm client





---> Le flag --rm supprime automatiquement le conteneur après exécution — c’est normal pour un client qui ne tourne qu’une fois.



**Configuration \& Variables d’environnement :**



ENV PYTHONUNBUFFERED=1 est ajouté afin que les logs s’affichent immédiatement, ce qui est particulièrement utile côté serveur.



**Tests :**



Démarrer le serveur :



docker compose up server





Exécuter le client :



docker compose run --rm client



**Auteur** :

Nom : Meriam Thamri

Mini Projet : Gestionnaire de tâches partagé (client–serveur en Python + Git + Docker) 

