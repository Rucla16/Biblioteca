# S_Biblioteca
from llibre import Llibre
from soci import Soci 

class Biblioteca(self):
    def__init__(self):
        self.socis = []
        self.llibres = []

    def afegir_llibre(self):
        titol = input("Escriu el títol del llibre: ")
        autor = input("Escriu el autor del llibre: ")
        llibre = Llibre(titol, autor)
        self.llibres.append(llibre)
     
    def afegir_soci(self):
        nom = input("Escriu el nom del soci: ")
        soci = Soci(nom)
        self.socis.append(soci)

    def prestar_llibre(self, dies_a_prestar):
        registre = input("Quin és el teu nom?: ")
        pregunta = input("Quin llibre t'emportes?: ")
        llibre_a_prestar = None
        dies_a_prestar = 30
        for i in self.llibres:
            if llibre.titol == pregunta:
                llibre_a_prestar = llibre
        for soci in self.socis:
            if soci.nom == registre:
                soci_actual = soci

        try:
            llibre_a_prestar.prestar()
            soci_actual.prestar_llibre(llibre_a_prestar)
        except Exception:
            print("Llibre ja en prestec")

    def devolucio_llibres(self, devolucio):
        devolucio = int(input("Introdueix el nombre de dies que portes amb el llibre prestat: "))
        if devolucio < dies_a_prestar:
            print("Encara no has de retornar el teu llibre.")
        elif devolucio == dies_a_prestar:
            print("Avui és l'últim dia per retornar el teu llibre.")
        elif devolucio > dies_a_prestar:
            penalitzacio_retard(self, retard)


    def limit_per_soci(self, limit):
        limit = 3
        if soci_actual.prestar_llibre(llibre_a_prestar) = limit:
            print("Has arribat al límit de llibres que pots agafar!")
        else:
            return Biblioteca.prestar_llibre(self)
    
    def penalitzacio_retard(self, retard):
        retard = dies_a_prestar + 1
        if soci_actual.devolucio_llibres(devolucio) = retard:
            print("Tens un retard en la devolució del teu llibre!")
        

        
