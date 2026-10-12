#programma chiede se maggiorenne o no.
#se sì, mostra film, sennò no. usando match.

print("Benvenuto al cinema!")
anni = int(input("Quanti anni hai? "))

if anni >=18:
    eta = "maggiorenne"
else:
    eta = "minorenne"

match eta:
    case "maggiorenne":
        print("Buona visione!")
    case "minorenne":
        print("Vai via!!")
