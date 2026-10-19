file = open("Corso_Python/Sett3/19Lun/testo.txt", "r")
print(file) #stampa dettagli del file
print(file.read())

riga = file.readline(1)
print(riga)
file.close()

file = open("Corso_Python/Sett3/19Lun/testo.txt", "w")
file.write("test")