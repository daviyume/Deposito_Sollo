#creare lista con nome, età, sesso e premium bool inseriti da utente
#dopo chiedi quale modificare
#poi regola valori per sistemare valori invalidi o incorretti

utente = []

utente.append(input("Nome: "))

eta = input("Età: ")
if int(eta) >= 0 or int(eta) < 0:
    utente.append(int(eta))
else:
    utente.append(13)

utente.append(input("Sesso (m/f): ").lower())
if utente[2] != 'm' and utente[2] != 'f':
    utente[2] = 'm'

utente.append(input("Hai premium? (True / False): "))
if utente[3] != True and utente[3] != False:
    utente[3] = False

print("Quale vuoi modificare? (nome / eta / sesso / premium) ")
sel = input()

match sel:
    case "nome":
        utente[0] = input("Inserire il nuovo nome: ")
        if utente[0] == "":
            utente[0] = "Mario"

    case "eta":
        eta = int(input("Inserire la nuova età: "))
        if not eta > 0 and not eta <= 0:
            pass
        else:
            utente[2] = eta
    case "sesso":
            utente[2] = input("Inserire il nuovo sesso (m/f): ").lower()
            if utente[2] != 'm' and utente[2] != 'f':
                pass
    case "nome":
            utente[3] = bool(input("Inserire il nuovo stato Premium (True / False): "))
            if utente[3] != True and utente[3] != False:
                utente[3] = False

print("Nome: ", utente[0])
print("Età: ", utente[1])
print("Sesso: ", utente[2])
print("Premium: ", utente[3])
            


