import uuid

class Tache:
    def __init__(self, titre, description, auteur, statut="TODO"):
        self.id = str(uuid.uuid4())
        self.titre = titre
        self.description = description
        self.statut = statut
        self.auteur = auteur

    def to_line(self):
        return f"{self.id};{self.titre};{self.description};{self.statut};{self.auteur}"