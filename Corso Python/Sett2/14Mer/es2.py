#Sistema Gestione studenti
#classe persona con figli studente e professore con attributi privati.

class Persona:
    def __init__(self, nome="", eta=0):
        self.__nome = nome
        self.__eta = eta

    def presentazione(self):
        print("Sono "+self.__nome+" e ho "+str(self.__eta)+" anni.")

class Studente(Persona):
    
    #attributi vengono ridichiarati perché attributi della classe padre non sono accessibili.
    def __init__(self, nome="", eta=0):
        self.__nome = nome
        self.__eta = eta
        self.voti = []

    def getvoti(self):
        return self.voti

    def calcolamedia(self):
        somma = 0
        cont = 0
        for val in self.voti:
            somma += val
            cont += 1
        return somma/cont
    def presentazione(self):
        print("Sono "+self.__nome+" e ho "+str(self.__eta)+" anni.")
        print("Ho una media dei voti di "+str(self.calcolamedia()))

class Professore(Persona):
    def __init__(self, nome="", eta=0, materia="generale"):
        self.__nome = nome
        self.__eta = eta
        self.materia = materia
    def presentazione(self):
            print("Sono "+self.__nome+" e ho "+str(self.__eta)+" anni.")
            print("La materia che insegno è "+self.materia)

class Preside(Studente, Professore):

    def aggvoto(self, Stud, voto):
        Stud.voti.append(voto)
    def rimvoto(self, Stud, voto):
            Stud.voti.remove(voto)

Stud1 = Studente("Mario", 22)
Stud2 = Studente("Luigi", 21)

Prof1 = Professore("Bowser", 30, "Psicologia")
Pres1 = Preside("Toad", 60)

Pres1.aggvoto(Stud1, 9)
Pres1.aggvoto(Stud1, 8)
Pres1.aggvoto(Stud2, 6)
Pres1.aggvoto(Stud2, 10)

Stud1.presentazione()
Stud2.presentazione()

Prof1.presentazione()

Pres1.rimvoto(Stud2, 6)
Stud2.presentazione()