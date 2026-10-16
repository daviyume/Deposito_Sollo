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
        self.__costo = costo

    def getmarca(self):
        return self.__marca
    def getmodello(self):
        return self.__modello
    def getanno(self):
        return self.__anno
    def getguasto(self):
        return self.__guasto
    def getcosto(self):
            return self.__costo
        

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

    def __init__ (self, marca="?", modello="?", anno=annocorrente, guasto="?", capacita =0, giri=0, costo=50):
        super().__init__(marca, modello, anno, guasto, costo) #richiamata super
        self.__capacita_kg = capacita
        self.__giricentrifuga = giri

    def stimacostobase(self):
        costofinale = self.getcosto()
        if self.__capacita_kg > 40:
            costofinale += 10
        elif self.__capacita_kg > 80:
            costofinale += 30
        return costofinale



class Frigorifero(Elettrodomestico):
    def __init__ (self, marca="?", modello="?", anno=annocorrente, guasto="?", litri=0, hafreezer=False, costo=50):
        super().__init__(marca, modello, anno, guasto, costo) #richiamata super
        self.__litri = litri
        self.__hafreezer = hafreezer

    def stimacostobase(self):
        costofinale = self.getcosto()
        if self.__litri > 50:
            costofinale += 20
        if self.__hafreezer:
            costofinale += 40
        return costofinale
    
class Forno(Elettrodomestico):
    def __init__ (self, marca="?", modello="?", anno=annocorrente, guasto="?", alim="gas", vent=False, costo=50):
            super().__init__(marca, modello, anno, guasto, costo) #richiamata super
            self.__alimentazione = alim
            self.__haventilazione = vent

    def stimacostobase(self):
        costofinale = self.getcosto()
        if self.__alimentazione == "elettrico":
            costofinale += 20
        if self.__haventilazione:
            costofinale += 20
        return costofinale


class TicketRiparazione:
    def __init__ (self, id, Ed, stato="aperto", note=[]):
        self.__id = id
        self.__elettrodomestico = Ed
        self.__stato = stato
        self.__note = note

    def geted(self):
        return self.__elettrodomestico

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

    def __str__(self):
        string = "ID: "+str(self.__id)+" | Tipo elettrodomestico: "+ type(self.__elettrodomestico).__name__ +" | Stato: "+self.__stato
        return string

#to do: Officina e metodi
class Officina(Lavatrice, Frigorifero, Forno):
    def __init__ (self, nome, tickets=[]):
        self.__nome = nome
        self.__tickets = tickets

    def aggticket(self, ticket):
        self.__tickets.append(ticket)
    def rimticket(self, ticket):
        self.__tickets.remove(ticket)
    def stampaticketaperti(self):
        for tic in self.__tickets:
            if tic.getstato()=="aperto":
                print(str(tic))
                
    def sommapreventivi(self):
        somma=0
        for tic in self.__tickets:
            somma += tic.geted().stimacostobase()
        return somma

    def statistichepertipo(self):
        lavatrici = 0
        frigoriferi = 0
        forni = 0
        for tic in self.__tickets:
            if isinstance(tic.geted(), Lavatrice):
                lavatrici +=1
            if isinstance(tic.geted(), Frigorifero):
                frigoriferi +=1
            if isinstance(tic.geted(), Forno):
                forni +=1

        print("Lavatrici in riparazione: ", lavatrici)
        print("Frigoriferi in riparazione: ", frigoriferi)
        print("Forni in riparazione: ", forni)
        #alternativa è isinstance(oggetto, classe)

off = Officina("Super")

lava1 = Lavatrice("Sony", "2000", 2000, "Lenta", 50, 400)
frieza = Frigorifero("Dragon Technologies", "Ball9001", 2012, "Surriscaldamento", 91, True)
forno1 = Forno("Xiaomi", "f4", 2022, "Il forno si spegne da solo circa ogni 30 minuti.", "elettrico", True)

ticket1 = TicketRiparazione(8000, lava1)
off.aggticket(ticket1)
off.stampaticketaperti()

ticket2 = TicketRiparazione(2452, frieza, "aperto", ["pericoloso", "laser"])
off.aggticket(ticket2)

ticket3 = TicketRiparazione(6767, forno1)
off.aggticket(ticket3)

print("Somma preventivi: ", off.sommapreventivi())

off.rimticket(ticket3)
print("Somma preventivi: ", off.sommapreventivi())

off.statistichepertipo()

print(ticket2.getnote())