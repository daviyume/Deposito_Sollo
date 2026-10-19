#classe ContoBancario che incapsula info di un conto bancario e gestire il saldo.
#att privati titolare e saldo, metodi pubblici deposita, preleva e visualizza saldo.
#fai controllo per validi importi. Aggiungi metodi getter e setter.

class ContoBancario:
    __titolare = ""
    __saldo = 0

    def gettitolare(self):
        return self.__titolare
    def getsaldo(self):
        return self.__saldo
    def settitolare(self, titolare):
        self.__titolare = titolare
    def setsaldo(self, saldo):
        if saldo >=0:
            self.__saldo = saldo
        else:
            print("Errore: l'importo inserito non è valido.")
    
    def visualizzasaldo(self):
        print("Saldo: ", self.__saldo)

    def deposita(self, deposito):
        if deposito >=0:
            self.__saldo += deposito
            return deposito
        else:
            print("Errore: l'importo inserito per il deposito non è valido.")
            return 0

    def preleva(self, prelievo):
        if prelievo >=0:
            self.__saldo -= prelievo
            return prelievo
        else:
            print("Errore: l'importo inserito per il prelievo non è valido.")
            return 0

def tasca():
    print("Soldi in tasca: ", portafogli)

            
portafogli = 100
Conto1 = ContoBancario()
Conto1.settitolare("Mario")
Conto1.setsaldo(50)
x = 0

Conto1.visualizzasaldo()
x = int(input("Inserisci l'importo da depositare: "))

portafogli -= Conto1.deposita(x)
tasca()

x = 20
portafogli += Conto1.preleva(x)

tasca()
Conto1.visualizzasaldo()

#la variabile è privata e non può essere stampata
#print(Conto1.__titolare)