def conta(max: int):
    cont = 0
    while cont < max:
        yield cont #yield è il valore che viene dato ad ogni iterazione
        cont+=1

x = 8
for i in conta(8): #funzione viene utilizzata come iteratore
    print(i)



def decoratore(saluta): #decoratore aggiunge istruzioni prima e dopo la chiamata di una funzione
    def wrapper():
        print("Prima")
        saluta()
        print("Dopo")
    return wrapper

@decoratore
def saluta():
    print("ciao")


saluta()