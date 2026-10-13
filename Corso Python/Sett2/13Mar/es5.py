#es 157
#Classe base UnitaMilitare con diverse unità con compiti e metodi specifici
#classe ControlloMilitare eredita da tutte le classi per gestire
#e controllare tutte le unità

class UnitaMilitare:

    def __init__(self, nome="soldato", num=0, x=0, y=0):
        self.nome = nome
        self.num = num
        self.x = x
        self.y = y

    def avanza(self):
        self.y+=10
        print("La "+self.nome+" avanza!")

    def attacca(self):
        print("La "+self.nome+" attacca!")

    def ritiro(self):
        self.y-=15
        print("La "+self.nome+" si ritira.")
    def destra(self):
        self.x+=10
        print("La "+self.nome+" si muove verso est.")
    def destra(self):
        self.x-=10
        print("La "+self.nome+" si muove verso ovest.")

    #getattribute scopo debug
    def __getattribute__(self, attributo):
            print("Debug: Ecco il valore dell'attributo ", attributo)
            return super().__getattribute__(attributo)

    #eq
    def __eq__(self, unita2):
        return self.nome == unita2.nome

class Fanteria(UnitaMilitare):

    def __init__(self, nome="Fanteria", num=0, x=0, y=50):
            self.nome = nome
            self.num = num
            self.x = x
            self.y = y

    def trincea(self):
        print("Trincea costruita a ", self.x, self.y)

class Artiglieria(UnitaMilitare):

    def __init__(self, nome="Artiglieria", num=0, x=0, y=0, aim=10):
            self.nome = nome
            self.num = num
            self.x = x
            self.y = y
            self.aim = aim

    def calibra(self, newaim):
        self.aim = newaim

    def ritiro(self):
        self.y-=5
        print("La "+self.nome+" si ritira lentamente.")

class Cavalleria(UnitaMilitare):

    def __init__(self, nome="Cavalleria", num=0, x=0, y=0, aim=10):
        self.nome = nome
        self.num = num
        self.x = x
        self.y = y

    def avanza(self):
        self.y+=10
        print("La "+self.nome+" avanza con velocità!")

    def esploraterreno(self):
        print("Lì sembra esserci... hmmm...")

class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome="Supporto Logistico", num=0, x=0, y=0, aim=10):
            self.nome = nome
            self.num = num
            self.x = x
            self.y = y
    
    def attacca(self):
        print("Il supporto logistico non può attaccare.")
    def rifornisciunita(self):
        print("Rifornimento provveduto!")

class Ricognizione(UnitaMilitare):
    def __init__(self, nome="Ricognizione", num=0, x=0, y=0, aim=10):
        self.nome = nome
        self.num = num
        self.x = x
        self.y = y

    def attacca(self):
        print("Le sentinelle non possono attaccare.")
    def conduciricognizione(self):
        print("Sentinella piazzata in ", self.x, self.y)


class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    dizionario = []

    def mostraunita(self):
        print(self.dizionario)

    def reg(self, unita):

        valid = True

        for uni in self.dizionario:
            if uni == unita:
                valid = False
                break
            
        if valid:
            self.dizionario.append(unita)
        else:
            print("Errore, c'è un'unita già con questo nome.")

    def dettagliunita(self, attributo):
        return attributo

    def __call__(self):
        print("Esercito: ")
        for uni in self.dizionario:
            print(uni.nome)

    #repr
    def __repr__(self):
        print("test")


ConM = ControlloMilitare()
Fant1 = Fanteria("Fanteria principale", 15, 10, 50)
Supp1 = SupportoLogistico("Supporto primario", 8, 10, 40)

ConM.reg(Fant1)
ConM.reg(Fant1)
ConM.reg(Supp1)

ConM()