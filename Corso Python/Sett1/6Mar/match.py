#comando del match
comando = input("Inserisci un comando: ")

#selezione in base al comando
match comando:
    case "on":
        print("acceso")
    case "off":
        print("spento")
    case _:
        #default
        print("errore")

