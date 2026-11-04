#5.3
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

iris = load_iris()
X = iris.data
scaler = StandardScaler()
X_s = scaler.fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_s)

inertias = []
silhouettes = []
ks = range(2, 8+1)

for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=42)
    km.fit(X_pca)
    #analizziamo la mappa. Le predizioni sono caricate, 
    # ma non le mettiamo in una variabile come in es1facile.py

    inertias.append(km.inertia_)
    silhouettes.append(silhouette_score(X_pca, km.labels_))

fig, ax = plt.subplots(1, 2, figsize= (8, 4))
plt.subplots_adjust(wspace=0.4, hspace=0.4)

ax[0].plot(ks, inertias)
ax[0].set_xlabel("Valori k")
ax[0].set_xticks(ks)
ax[0].set_ylabel("Inertia")

ax[1].plot(ks, silhouettes)
ax[1].set_xlabel("Valori k")
ax[1].set_xticks(ks)
ax[1].set_ylabel("Silhouette score")
plt.show()

# risultato: 2 dei fiori sono più simili tra loro

####
import pandas as pd
df = pd.DataFrame()
df.index = ks
#df.set_index(col) for columns
df['Inertia'] = inertias
df['Silhouette scores'] = silhouettes
print(df)