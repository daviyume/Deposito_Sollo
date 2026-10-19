#crea classe conto corrente dove l'oggetto ha intestatario e saldo.
#come metodi, deposita, ritira e saldo dell'intestatario.
class ContoCorrente:
    def __init__ (self, inputintestatario, inputsaldo=0):
        self.intestatario = inputintestatario
        saldo = inputsaldo

    def deposita(self, inputsaldo):
        if inputsaldo > 0:
            saldo += inputsaldo
        else:
             print("Errore: la somma da depositare è invalida.")
    def preleva(self, inputsaldo):
            if inputsaldo <= saldo:
                saldo -= inputsaldo
            else:
                print("Errore: il saldo non è sufficiente.")

    def stampasaldo(self):
         print("Il saldo di ", self.intestatario, " è di ", self.saldo)

ContoX = ContoCorrente("nessuno")

while True:
    sel = input("Quale azione vuoi svolgere? deposita (d)  /  Preleva (p)  /  Stampa saldo (s): ")

    match sel.lower():
        case 'd':
            intestatario = input("Inserisci l'intestatario: ")
            ContoX.intestatario = intestatario
            saldo = int(input("Inserisci il saldo: "))
            ContoX.deposita(saldo)
        case 'p':
                    intestatario = input("Inserisci l'intestatario: ")
                    ContoX.intestatario = intestatario
                    saldo = int(input("Inserisci il saldo: "))
                    ContoX.preleva(saldo)
        case 's':
              ContoX.stampasaldo()