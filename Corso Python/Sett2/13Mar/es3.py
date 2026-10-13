#crea Animale classe base con diverse classi derivate in uno zoo
#nome, eta, faisuono().
#3 animali che hanno metodi specifici all'animale.

class Animale:
    def __init__(self, nome="Animale Generico", eta=0):
        self.nome= nome
        self.eta = eta

    def verso(self):
        print("L'animale ti chiama.")

class Cane(Animale):
    def __init__(self, nome, eta, giocopreferito):
        self.nome = nome
        self.eta = eta
        self.giocopreferito = giocopreferito

    def verso(self):
            print("Bau bau!")

    def gioca(self):
        print("Hai giocato con "+ self.nome+ " a "+ self.giocopreferito+ ", è contento!")

class Leone(Animale):

    def verso(self):
        print("Roooooar!")

    def caccia(self):
        print("Il leone conosciuto come ", self.nome, "è in caccia!!")

class Drago(Animale):

    y = 0

    def verso(self):
        print("RAAAAAOOOR!")

    def vola(self):
        self.y+=100
        print("Il drago spiega le sue ali!! Raggiunge un'altezza di ", self.y, "m!")

    def scendi(self):
        self.y = 0
        print("Il drago scende al suolo con potenza.")

cane1 = Cane("Doggie", 5, "palla da tennis")
leone1 = Leone("Leo", 8)
drago1 = Drago("Orasus", 200)

cane1.verso()
cane1.gioca()

leone1.verso()
leone1.caccia()

drago1.verso()
drago1.vola()
drago1.vola()
drago1.scendi()
drago1.vola()
drago1.scendi()
