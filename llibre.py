# Llibre
class Llibre:
    def__init__(self, titol, autor):
        self.titol = titol
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible == False:
            raise Exception()
        else:
            self.disponible = False
    def retornar(self):
        self.disponible = True