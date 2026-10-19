
class Studente:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def __str__(self):
        return "Studente: " + self.nome +", età: " + str(self.eta) #return deve essere una stringa sola

studente1 = Studente("Mario", 22)

print(studente1)


class Squadra:
    def __init__(self, nome, giocatori):
        self.nome = nome
        self.giocatori = giocatori

    def __len__(self):
        return len(self.giocatori)

squadra1 = Squadra("Funghi", ["Mario", "Luigi", "Wario", "Waluigi"])
print(len(squadra1))

class Moltiplicatore:
    def __init__(self, numero):
        self.numero = numero

    def __call__(self, valore):
        return valore*self.numero

doppio = Moltiplicatore(2)

print(doppio(11))
