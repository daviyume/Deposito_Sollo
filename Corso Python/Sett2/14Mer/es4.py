#classe posto con numero, fila e occupato.
#metodi prenota, libera e getter per informazioni.

#posto vip ha servizi extra
#posto standard ha un costo per essere prenotato, e prenota chiede soldi

#classe teatro con tutti i posti
#agg posto, prenota posto, stampa posti occupati

class Posto:
    costo = 20

    def __init__(self, numero, fila, occupato=False):
        self._numero = numero
        self._fila = fila
        self._occupato = occupato

    def getter(self, att):
        match att:
            case "numero":
                return self._numero
            case "fila":
                return self._fila
            case "occupato":
                return self._occupato
    
    def prenota(self):
        if self._occupato:
            print("Il posto è occupato.")
        else:
            print("Il posto è libero. Vuoi pagare ", self.costo, " ? (lascia vuoto se no)")
            if input():
                self._occupato = True
                print("Il posto è ora tuo.")
            else:
                print("Annullato.")
    
    def libera(self):
        if(self._occupato):
            self._occupato = False
            print("Il posto è ora libero.")
        else:
            print("Il posto è gia libero.")

    def __eq__(self, posto2):
        return self._numero == posto2._numero and self._fila == posto2._fila

class PostoVIP(Posto):
    costo = 40
    serviziextra = []
    extracosto = 20

    def __init__(self, numero, fila, occupato="False"):
            self._numero = numero
            self._fila = fila
            self._occupato = occupato

    def prenota(self):
            if self._occupato:
                print("Il posto è occupato.")
            else:
                print("Il posto è libero. Vuoi pagare ", self.costo, " ? (lascia vuoto se no)")
                if input():
                    self._occupato = True
                    print("Il posto è ora tuo.")
                    print("Extra: [1] Servizio al posto, [2] mMassaggio [0] Nessuno")
                    print("Ogni servizio extra costa ", self.extracosto, ". Quale vuoi? ")
                    match input():
                        case "1":
                            self.serviziextra.append("Servizio al posto")
                            print("Servizio extra aggiunto (Servizio al posto).")
                        case "2":
                            self.serviziextra.append("Massaggio")
                            print("Servizio extra aggiunto (Massaggio).")
                        case _:
                            print("Nessun extra scelto.")
                else:
                    print("Annullato.")

class PostoStandard(Posto):

    def prenota(self):
        if self._occupato:
            print("Il posto standard è occupato.")
        else:
            print("Il posto standard è libero. Vuoi pagare ", self.costo, " ? (lascia vuoto se no)")
            if input():
                self._occupato = True
                print("Il posto standard è ora tuo.")
            else:
                print("Annullato.")

class Teatro:
    _posti = []

    def saluta(self):
        print("ciao")

    def aggiungiposto(self, PostoG):
        self._posti.append(PostoG)

    def prenotaposto(self, numero, fila):
        valid = False
        for pos in self._posti:
            if pos._numero == numero and pos._fila == fila:
                pos.prenota()
                valid = True
                break
        if not valid:
            print("Il posto non esiste")

    def stampapostioccupati(self):
        print("POSTI OCCUPATI: ")
        for pos in self._posti:
            if pos._occupato:
                print("N:", pos._numero, "F:", pos._fila)

    def stampapostiliberi(self):
        print("POSTI LIBERI: ")
        for pos in self._posti:
            if not pos._occupato:
                print("N:", pos._numero, "F:", pos._fila)

Posto1 = PostoVIP(10, 2)
Posto2 = PostoStandard(72, 8)

Teatro1 = Teatro()

Teatro1.aggiungiposto(Posto1)
Teatro1.aggiungiposto(Posto2)
Teatro1.prenotaposto(9, 2)
Teatro1.prenotaposto(10, 2)

Teatro1.stampapostioccupati()
Teatro1.stampapostiliberi()

#possibile interfaccia
'''
while True:
    match input("Seleziona l'azione da svolgere [a] Aggiungi posto [p] Prenota [L] vedi posti liberi [O] vedi posti occupati").lower():
        case 'a':
            
'''