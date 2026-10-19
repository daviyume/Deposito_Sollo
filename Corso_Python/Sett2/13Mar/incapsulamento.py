#incapsulamento
#__ privato
#_ protetta

class Parametriprivati():
    __nome = "Mario"
    _votocibopreferito = "funghi"

    def getnome(self):
        return self.__nome

    def setnome(self, nuovonome):
        self.__nome = nuovonome

    def __metodoprivato(self):
        print("ciao")

#print(Parametriprivati.__nome)

profilo1 = Parametriprivati()

profilo1.setnome("Luigi")
print(profilo1.getnome())