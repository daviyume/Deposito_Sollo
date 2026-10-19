#classe chiamata Punto con x e y, con un metodo Muovi che fa inserire all'utente 
#x e y della traslazione.
#Inoltre un metodo che dà la distanza dall'origine

class Punto:

    def __init__ (self, x=0, y=0):
        self.x = x
        self.y = y

    
    def ShiftX (self, xshift):
        self.x += xshift
    def ShiftY (self, yshift):
            self.y += yshift
    

    def MoveX (self, destx):
        self.x = destx
    def MoveY (self, desty):
        self.y = desty

    def Distanza (self):
        print("Distanza X: ", self.x)
        print("Distanza Y: ", self.y)

Punto1 = Punto()

while True:
    Punto1.Distanza()

    dest = int(input("Inserisci destinazione X: "))
    Punto1.MoveX(dest)

    dest = int(input("Inserisci il movimento Y: "))
    Punto1.MoveY(dest)
    
