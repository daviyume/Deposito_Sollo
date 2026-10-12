#classe chiamata garage con capienza nel costruttore, lista di targhe di auto presenti,
#metodi parcheggia e rimuovi, posti liberi. parcheggia utilizza formato_targa_valido()

class Garage:
    def __init__(self, inpcapienza):
        self.capienza = inpcapienza

    macchine = []

    def parcheggia(self, inptarga):
        if self.postiliberi() > 0:
            if self.targavalida(inptarga):
                self.macchine.append(inptarga)
            else:
                print("Errore: la targa non è valida.")
        else:
            print("Errore: non ci sono abbastanza posti.")

    def rimuovi(self, inptarga):
        exists = False
        for tar in self.macchine:
            if inptarga == tar:
                exists = True
                break
        if exists:
            self.macchine.remove(inptarga)
        else:
            print("Errore: la targa non esiste.")

    def postiliberi(self):
        return self.capienza - len(self)

    def targavalida(self, inptarga):
        if len(inptarga) == 7:
            return True
        else:
            return False

    def __call__ (self):
        return self.macchine

    def __len__ (self):
        return len(self.macchine)

garageX = Garage(5)

while True:
    sel = input("Seleziona: Parcheggia [p]  /  Rimuovi [r]  /  Vedi posti liberi [v]  /  Esci [x]: ")

    match sel.lower():
        case 'p':
            targa = input("Inserisci la targa della macchina da inserire: ")
            garageX.parcheggia(targa)
        case 'r':
            targa = input("Inserisci la targa della macchina da rimuovere: ")
            garageX.rimuovi(targa)
        case 'v':
            print(garageX())
            print("I posti liberi sono ", garageX.postiliberi())
        case 'x':
            break
        case _:
            pass