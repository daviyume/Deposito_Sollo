#incapsulamento, ereditarietà, polimorfismo e type() per oggetti e metodi variatici.
#software per officina di elettrodomestici e riparazione con ticket.
#classe base elettrodomestico con derivate.
#regola 1: attributi tutti privati e accessibili solo tramite getter e setter
#regola 2: super()
#ogni sottoclasse ha la sua versione di stimacostobase(self)
#classe TicketRiparazione
#classe Officina
#type() per controllo tipo di oggetto per statistichepertipo().

annocorrente = 2026

class Elettrodomestico:

    def __init__ (self, marca="?", modello="?", anno=annocorrente, guasto="?", costo=50):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno #anno acquisto
        self.__guasto = guasto
        self.__costo = 50

    def getmarca(self):
        return self.__marca
    def getmodello(self):
        return self.__modello
    def getanno(self):
        return self.__anno
    def getguasto(self):
        return self.__guasto

        

    def setmarca(self):
        marca = ""
        while marca == "":
            marca = input("Inserisci il nome della marca: ")
        self.__marca = marca
    def setmodello(self):
        modello = ""
        while modello == "":
            modello = input("Inserisci il nome del modello: ")
        self.__modello = modello
    def setanno(self):
        anno = ""
        while anno == "" or anno > annocorrente or type(anno)!=int:
            anno = input("Inserisci l'anno: ")
        self.__anno = anno
    def setguasto(self):
        guasto = ""
        while guasto == "":
            guasto = input("Descrivere il guasto: ")
        self.__guasto = guasto

    def descrizione(self):
        print("Marca: "+self.__marca)
        print("Modello: "+self.__modello)
        print("Anno di acquisto:"+self.__anno)
        print("Guasto: "+self.__guasto)

    def stimacostobase(self):
        return self.__costo

class Lavatrice(Elettrodomestico):

    def __init__ (self, marca="?", modello="?", anno=annocorrente, guasto="?", costo=50, capacita =0, giri=0):
        super().__init__(marca, modello, anno, guasto, costo) #richiamata super
        self.__capacita_kg = capacita
        self.__giricentrifuga = giri

    def stimacostobase(self):
        costofinale = self.__costo
        if self.__capacita_kg > 40:
            costofinale += 10
        elif self.__capacita_kg > 80:
            costofinale += 30
        return costofinale



class Frigorifero(Elettrodomestico):
    def __init__ (self, marca="?", modello="?", anno=annocorrente, guasto="?", costo=50, litri=0, hafreezer=False):
        super().__init__(marca, modello, anno, guasto, costo) #richiamata super
        self.__litri = litri
        self.__hafreezer = hafreezer

    def stimacostobase(self):
        costofinale = self.__costo
        if self.litri > 50:
            costofinale += 20
        if self.__hafreezer:
            costofinale += 40
        return costofinale
    
class Forno():
    def __init__ (self, marca="?", modello="?", anno=annocorrente, guasto="?", costo=50, alim=0, vent=False):
            super().__init__(marca, modello, anno, guasto, costo) #richiamata super
            self.__tipoalimentazione = alim
            self.__haventilazione = vent

    def stimacostobase(self):
        costofinale = self.__costo
        if self.__alimentazione == "elettrico":
            costofinale += 20
        if self.__haventilazione:
            costofinale += 20
        return costofinale


class TicketRiparazione:
    __stato = "aperto"
    __note = []

    def __init__ (self, id, Ed):
        self.__id = id
        self.__elettrodomestico = Ed

    def getstato(self):
        return self.__stato
    def getnote(self):
        return self.__note
    def setstato(self, stato):
        self.__stato = stato
    def setnote(self, note):
        self.__note = note

    def aggnota(self, testo):
        self.__note.append(testo)

    #per il metodo variadico ero assente
    def calcolapreventivo(self, elettrodomestico, *vociextra):
        costo = elettrodomestico.stimacostobase() + len(*vociextra)*10
        return costo

#to do: Officina e metodi
class Officina:
    pass

l1 = Lavatrice()
print(l1.costo)
l1.getmarca()
l1.getmodello()