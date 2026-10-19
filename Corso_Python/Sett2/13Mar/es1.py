#Convertitore con:
#metodo statico euro in dollari (1.08)
#km in miglia 0.621371
#non creare alcun oggetto

class Convertitore:

    @staticmethod
    def euroindollari(eur):
        return eur*1.08

    @staticmethod
    def kminmiglia(km):
        return km*0.621371

euro = float(input("Inserisci gli euro da convertire in dollari: "))
chilometri = float(input("Inserisci i chilometri da convertire in miglia: "))

print("Dollari: ", Convertitore.euroindollari(euro))
print("Miglia: ", Convertitore.kminmiglia(chilometri))