# Soci
class Soci:
    def__init__(self, nom):
        self.nom = nom
        self.llibres_prestats = []
    def agafar_llibre(self, llibre):
        self.llibres_prestats.append(llibre)
    def tornar_llibre(self, llibre):
        self.llibres_prestats.remove(llibre)
