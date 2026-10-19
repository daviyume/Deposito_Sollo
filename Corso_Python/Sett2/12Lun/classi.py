#definizione della classe
class Persona:
    #Metodo costruttore. Metodo speciale che serve ad inizializzare attributi 
    # dell'oggetto e può richiedere parametri obbligatori.
    def __init__(self, eta):
        self.eta = eta
    nome = "Marco"
    cognome = "Verdetti"
    def saluta(self): #per ogni metodo in una classe viene definito anche l'oggetto stesso
        print(self.nome + Persona.cognome + ": Ciao!")

#inizializzazione dell'oggetto tramite costruzione
Ogg_1 = Persona(26)

print(Ogg_1.nome)
print(Ogg_1.eta)

Ogg_1.nome = "Mario"
Ogg_1.saluta()

class Automobile:
    n_istanze = 0 
    @classmethod
    def conta_istanze(cls):
        print(cls.n_istanze)

    def __init__(self, marca="", modello=""):
        self.marca = marca
        self.modello = modello
        Automobile.n_istanze += 1
    ruote: 4

    def info(self):
        print("L'automobile è una ", self.marca, " ", self.modello)

Macchina1 = Automobile("Lamborghini", "Plus")
Macchina2 = Automobile("Fiat", "Panda")
Macchina1.info()
Macchina1.conta_istanze()
Automobile.conta_istanze() #entrambe le chiamate possono accedere al metodo di classe

class Esempio: #default
    def __init__(self):
        pass

class Calcolatrice:

    @staticmethod #metodo statico
    def somma (a, b): #non è necessario dichiarare il self o cls
        return a+b

print(Calcolatrice.somma(5, 4))