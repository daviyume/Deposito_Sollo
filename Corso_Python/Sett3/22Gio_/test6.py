import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

plt.rcParams['figure.figsize'] = [10, 6]  
# Imposta la dimensione predefinita delle figure

plt.rcParams['figure.dpi'] = 100          
# Imposta la risoluzione delle figure in DPI

plt.rcParams['figure.facecolor'] = '#AACCFF'  # Colore di sfondo della figura
#sns.set_theme(style="whitegrid")

#####################################################
# FIGURE = canvas
# AXES = plotting area
# 

data = np.random.normal(size=100)

#GRAFICO CARTESIANO
xcord = [-50, 0, 50, 10, 20, 30]
ycord = [0, 30, 40, 50, 60, 80]

plt.figure()
plt.plot(xcord, ycord) #draws graph with x and y

plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.title('Grafico')  # Title of figure 1

# GRAFICO A BARRE
categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values)

plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.title('Grafico a Barre')

#ISTOGRAMMA
data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.title('Istogramma')

#SCATTER PLOT
x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Scatter Plot')




plt.show()