while True:
        print("[s] Somma [p] Parola [c] Conta [x] Esci")
        sel = input("Quale azione vuoi svolgere?")

        match sel.lower():
            case 's':
                ## 1. ciclo while, inserire numeri da sommare finché 0
                somma = 0
                while(True):
                    n = int(input("Inserire un numero da aggiungere (0 per interrompere): "))
                    if(n!=0):
                        somma += n
                    else:
                        break
                print("Somma: ", somma)
            case 'p':
                ## 2. parola inserita, ciclo for per stampare ogni lettera sulla propria riga
                parola = input("Inserisci una parola: ")
                for a in parola:
                    print(a)
            case 'c':
                ## 3. Ciclo range per stampare fino a un massimo
                goal = int(input("A quale numero vuoi contare? "))
                step = int(input("A step di? "))

                for x in [*range(0, goal+1, step)]:
                    print(x)
            case 'x':
                break
            case _:
                print("Scelta invalida: riprovare.")