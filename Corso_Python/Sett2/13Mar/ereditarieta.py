class Animale:
    def __init__(self, inpnome="Animale"):
        self.nome = inpnome

    def parla(self):
        print(self.nome+" ti chiama.")

class Topo(Animale):

    def parla(self):
        print(self.nome + " squittisce!")

animaleg = Animale()
topo = Topo("Rattolanio")

animaleg.parla()
topo.parla()

class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca: {self.marca}, modello: {self.modello}")

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")

#si riscrive il costruttore per 

class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello) #overwrite degli attributi
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli

    def mostra_informazioni(self):
        super().mostra_informazioni() #Chiamata con super (primo genitore, Veicolo)
        print("Potenza: ", self.cavalli)
        self.mostra_dotazioni() #Chiamata specifica (DotazioniSpeciali)


auto = AutomobileSportiva("Ferrari", "9000", ["Bei finestrini", "Molto veloce"], 800)

auto.mostra_informazioni()