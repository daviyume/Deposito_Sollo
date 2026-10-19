#classe MetodoPagamento con derivate.

class MetodoPagamento:

    def effettuapagamento(self, importo):
        print("Pagamento di ", importo, " effettuato.")

class CartaDiCredito(MetodoPagamento):

    def effettuapagamento(self, importo):
        print("Pagamento di ", importo, " effettuato tramite carta.")

class PayPal(MetodoPagamento):

    def effettuapagamento(self, importo):
        print("Pagamento di ", importo, " effettuato tramite PayPal.")

class BonificoBancario(MetodoPagamento):

    def effettuapagamento(self, importo):
        print("Pagamento di ", importo, " effettuato tramite bonifico.")

class GestorePagamenti:
    def paga(metodo, importo):
        metodo.effettuapagamento(importo)

Metodo1 = CartaDiCredito()
Metodo2 = PayPal()
Metodo3 = BonificoBancario()
default = Metodo1

GestorePagamenti.paga(default, 80)
GestorePagamenti.paga(Metodo2, 20)
GestorePagamenti.paga(Metodo3, 140)