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

data = np.random.normal(size=100)

#Histogram plot
#Kernel Density Estimation.
# It’s a way to show the shape of a data distribution as a smooth curve.
sns.histplot(data, kde=True)
plt.title('Grafico')
plt.show()