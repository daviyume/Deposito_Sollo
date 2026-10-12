class Libro:

    cont = 0

    def __init__ (self, intitolo="Nessun titolo", inautore="Sconosciuto", inpagine=0):
        self.titolo = intitolo
        self.autore = inautore
        self.pagine = inpagine

    def Descrizione(self):
        return ("Il libro ", self.titolo, "è stato scritto da ", self.autore, "ed ha ", self.pagine, "pagine.")

Libri = []

while True:
    sel = input("Crea libro (c)  /  Vedi tutti (v)  /  Esci (x): ")

    match sel.lower():
        case 'c':
            titolo = input("Inserisci il titolo: ")
            autore = input("Inserisci l'autore: ")
            pagine = input("Inserisci il numero di pagine: ")
            Libri.append(Libro(titolo, autore, pagine))

            print(Libri[0].Descrizione())

            Libro.cont +=1

        case 'v':
            for lib in Libri:
                print(lib.Descrizione())

        case _:
            break