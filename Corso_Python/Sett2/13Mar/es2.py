#classe animale con numero_animali (att di classe) init a 0.
#nome e specie att di oggetto passati al costruttore
#per ogni animale creato, incrementa numero_animali
#metodo di classe che stampi numero animali
#crea 3 animali e utilizza metodi di classe

class Animale:
    numeroanimali = 0

    def __init__(self, nome="Serpente", specie="Serpis Animalus"):
        self.nome = nome
        self.specie = specie
        Animale.numeroanimali+=1 #necessario nominare la classe

    @classmethod
    def quanti(self): #necessario riconoscere l'oggetto perché è la chiamata
        return Animale.numeroanimali

Serpente = Animale("Serpente", "Serpis Animalus")
Gatto = Animale("Gatus", "Sphynxus")
Criceto = Animale("Criceto", "Topentus")

print("Il numero degli animali è ", Animale.quanti())