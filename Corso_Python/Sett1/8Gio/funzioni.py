def buongiorno(nome: str): #definizione
    print("Buongiorno ", nome, ", preparati a splendere anche oggi!") #corpo

def max(a = 0, b = 0):
    if a>b:
        print(a)
    if b>a:
        print(b)

def dimezza(n: int):
    return n/2

def urla (parola: str):
    print(parola.upper())

buongiorno("Mario") #chiamata
max(2, 6)

x = 8
y = dimezza(x)
print (y)

urla("ciao")