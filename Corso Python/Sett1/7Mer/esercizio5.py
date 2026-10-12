## manipolazione lista

lista = []

while True:
    print("[v] visualizza [a] aggiungi [m] modifica [e] elimina [c] clear [x] esci")
    sel = input("Inserisci l'azione: ")

    match sel:
        case 'v':
            print(lista)
        case 'a':
            pos = int(input("In che posizione? "))
            lista.insert(pos, input("Inserisci l'elemento da aggiungere: "))
        case 'm':
            pos = int(input("In che posizione? "))
            lista[pos] = (input("Inserisci la modifica: "))
        case 'e':
            lista.remove(lista[int(input("Quale vuoi eliminare? "))])
        case 'c':
            lista.clear()
            print("Lista eliminata.")
        case 'x':
            break
        case _:
            print("Azione invalida.")
            