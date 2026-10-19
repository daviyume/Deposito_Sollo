#creiamo classe Prodotto con i suoi figli. Tramite classe fabbrica creiamo i prodotti.
#nome, costo, prezzo, caloclaprofitto(), metodo specifico

class Prodotto:
    def __init__(self, nome, costo, prezzo):
        self.nome = nome
        self.costo = costo
        self.prezzo = prezzo

    def profitto(self):
        return self.prezzo-self.costo

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo, prezzo, dim=50):
            self.nome = nome
            self.costo = costo
            self.prezzo = prezzo
            self.dim = dim

    def taglia(self):
        if self.dim>30:
            if self.dim>40:
                if self.dim>60:
                    return "XL"
                else:
                    return "L"
            else:
                return "M"
        else:
            return "S"

class Cibo(Prodotto):
    def __init__(self, nome, costo, prezzo, scad):
        self.nome = nome
        self.costo = costo
        self.prezzo = prezzo
        self.scad = scad

    def mostrascadenza(self):
        print("La scadenza è: "+self.scad)

class Contenitore(Prodotto):
    def __init__(self, nome, costo, prezzo, grand="media"):
            self.nome = nome
            self.costo = costo
            self.prezzo = prezzo
            self.grand = grand

    def mostragrandezza(self):
        print("la grandezza è "+self.grand+" ")


class Fabbrica:
    inventario = []
    guadagno = 0

    def aggprod(self, prod):
        self.inventario.append(prod)

    def venprod(self, prodnum):
        print("Profitto realizzato: ", self.inventario[prodnum].profitto())
        self.guadagno += self.inventario[prodnum].profitto()
        self.inventario.remove(self.inventario[prodnum])
    
    def resiprodotto(self, prod):
        copia = prod
        self.inventario.append(copia)
        print("Reso effettuato!")

    def __call__(self):
        for prod in self.inventario:
            print(prod.nome)

vestito1 = Abbigliamento("Maglia", 8, 12.50, 48)
print(vestito1.nome)
print("Profitto: ", vestito1.profitto())
print("Taglia: "+vestito1.taglia())

cibo1 = Cibo("Wurstel", 1, 2, "26/12/27")
print(cibo1.nome)
print("Profitto: ", cibo1.profitto())
cibo1.mostrascadenza()

contenitore1 = Contenitore("Contenitore di plastica", 1, 1.80, "medio-grande")
print(contenitore1.nome)
print("Profitto: ", contenitore1.profitto())
contenitore1.mostragrandezza()

print("")

fab1 = Fabbrica()

fab1()
fab1.aggprod(Abbigliamento("Maglia", 9, 12.50, 80))
fab1()
fab1.venprod(0)
fab1.aggprod(Abbigliamento("Pantaloni", 8, 10, 30))
fab1.aggprod(Cibo("Patatine", 1.50, 2.50, "30/06/28"))
fab1()
fab1.resiprodotto(cibo1)
fab1()