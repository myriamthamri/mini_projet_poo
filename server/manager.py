from .task import Tache

class GestionnaireTaches:
    def __init__(self):
        self.taches = {}

    def ajouter_tache(self, titre, desc, auteur):
        t = Tache(titre, desc, auteur)
        self.taches[t.id] = t
        return t

    def supprimer_tache(self, id_):
        return self.taches.pop(id_, None)

    def lister_taches(self):
        return list(self.taches.values())

    def changer_statut(self, id_, statut):
        t = self.taches.get(id_)
        if t:
            t.statut = statut
            return t
        return None