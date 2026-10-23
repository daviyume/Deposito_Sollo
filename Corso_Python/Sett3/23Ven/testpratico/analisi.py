import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
folderpath = os.path.dirname(os.path.abspath(__file__))+"/"
datapath = folderpath + "candy-data.csv"
venditepath = folderpath + "candy-vendite.csv"

plt.rcParams['figure.figsize'] = [18, 14]  
plt.rcParams['figure.dpi'] = 90
plt.rcParams['figure.facecolor'] = '#AACCFF'  # Colore di sfondo della figura
plt.rcParams['font.size'] = 8

#DATAFRAME UNITA' VENDUTE
vendite = pd.read_csv(venditepath)

#DATAFRAME VALORI CHOCO
data = pd.read_csv(datapath)
#swap valori sbagliati
data[['sugarpercent', 'winpercent']] = data[['winpercent', 'sugarpercent']]

#PULIZIA DEI DATI
vendite = vendite.drop(columns=['giacenza_magazzino'])
vendite = vendite.drop(columns=['valutazione_clienti'])
vendite = vendite.drop(columns=['area_vendita'])
vendite['choco']=data['chocolate']

#SORT
vendite = vendite.sort_values(by='unita_vendute')
print(vendite)

#MARCHE (Y)
marche = vendite['competitorname']
print(marche)

#VENDITE (X)
unita = vendite['unita_vendute']
print(unita)

#CHOCO
chocos = pd.Series(vendite['choco'] == 1)
chocos = chocos.replace(True, "#AA8800")
chocos = chocos.replace(False, "#44BBBB")
print(chocos)

# GRAFICO A BARRE UNITA' VENDUTE
plt.figure()
sns.barplot(x=unita, y=marche, palette=chocos.tolist(), hue=marche)

plt.xlabel('Vendite')
plt.ylabel('Marche')

plt.title('Grafico di vendite per ogni marca di dolce, tra cioccolato e altri gusti')

plt.tight_layout()
plt.show()

