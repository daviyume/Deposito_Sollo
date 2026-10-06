#creare un if else: nell'if struttura creazione dati per nome, password e id
#nel else controllo automatico con valori default

account = ["Mario", "Super", 200]

if input("Sei ", account[0], " ", account[1], "? (s/n)") == "n":
    #creazione account
    account[0] = input("Inserisci il tuo nome: ")
    account[1] = input("Inserisci il tuo cognome: ")
    account[2] = input("ID: ")
else:
    #login
    print("Benvenuto ", account[0])