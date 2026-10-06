#Esercizio 6 ma con opzione di creare una nuova lista oppure eliminare un elemento della prima

utente = []

#CREAZIONE PRIMO UTENTE
utente.append(input("Nome: "))

eta = input("Età: ")
if int(eta) > 0:
    utente.append(int(eta))
else:
    utente.append(13)

utente.append(input("Sesso (m/f): ").lower())
if utente[2] != 'm' and utente[2] != 'f':
    utente[2] = 'm'

premiumbool = input("Inserire lo stato Premium (True / False): ")
if premiumbool == "True":
    utente.append(True)
else:
    utente.append(False)

print("Quale vuoi modificare? (nome / eta / sesso / premium) ")
sel = input()

match sel:
    #MODIFICA
    case "nome":
        utente[0] = input("Inserire il nuovo nome: ")
        if utente[0] == "":
            utente[0] = "Mario"

    case "eta":
        eta = int(input("Inserire la nuova età: "))
        if eta < 0:
            pass
        else:
            utente[2] = eta
    case "sesso":
            utente[2] = input("Inserire il nuovo sesso (m/f): ").lower()
            if utente[2] != 'm' and utente[2] != 'f':
                pass
    case "premium":
            premiumbool = input("Inserire il nuovo stato Premium (True / False): ")

            if premiumbool == "True":
                utente[3] = True
            else:
                utente[3] = False

print("Nome: ", utente[0])
print("Età: ", utente[1])
print("Sesso: ", utente[2])
print("Premium: ", utente[3])

sel = (input("Vuoi creare una nuova lista [c] o eliminare un elemento dalla lista [e]?"))

match sel:
    case 'c':
        #CREA SECONDO UTENTE
        utente2 = []

        utente2.append(input("Nome: "))

        eta = input("Età: ")
        if int(eta) < 0:
            utente2.append(int(eta))
        else:
            utente2.append(13)
        
        utente2.append(input("Sesso (m/f): ").lower())
        if utente2[2] != 'm' and utente2[2] != 'f':
            utente2[2] = 'm'

        premiumbool = input("Inserire lo stato Premium (True / False): ")

        if premiumbool == "True":
            utente2.append(True)
        else:
            utente2.append(False)

        print("Quale vuoi modificare? (nome / eta / sesso / premium) ")
        sel = input()

        #MODIFICA 2
        match sel:
            case "nome":
                utente2[0] = input("Inserire il nuovo nome: ")
                if utente2[0] == "":
                    utente2[0] = "Mario"

            case "eta":
                eta = int(input("Inserire la nuova età: "))
                if not eta > 0 and not eta <= 0:
                    pass
                else:
                    utente2[2] = eta
            case "sesso":
                    utente2[2] = input("Inserire il nuovo sesso (m/f): ").lower()
                    if utente2[2] != 'm' and utente2[2] != 'f':
                        pass
            case "premium":
                    premiumbool = input("Inserire il nuovo stato Premium (True / False): ")

                    if premiumbool == "True":
                        utente2[3] = True
                    else:
                        utente2[3] = False
                

        print("Utente 2")
        print("Nome: ", utente2[0])
        print("Età: ", utente2[1])
        print("Sesso: ", utente2[2])
        print("Premium: ", utente2[3])
    case 'e':
        print("Inserire quale eliminare (0-", len(utente)-1, ")")
        eliinput = input()
        if not int(eliinput) > 0 and not int(eliinput) <= 0:
            eli = -1
        else:
            eli = int(eliinput)

        if eli >= 0 and eli < len(utente):
            utente.remove(utente[eli])
        else:
            print("Elemento invalido.")

        print(utente)

