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
data2 = np.random.normal(size=100)


fig = plt.figure()
sns.histplot(data, kde=True) #ax=ax1 (default)
plt.title('Seaborn Graph')  # Title of figure 1

fig2 = plt.figure()
ax = fig2.add_subplot(111)
#The 111 means:
# First 1: 1 row.
# Second 1: 1 column.
# Third 1: select the first subplot.
ax.hist(data2)
plt.title('Matplotlib Graph')  # Title of figure 2


plt.show()