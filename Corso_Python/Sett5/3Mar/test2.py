import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

digits = load_digits()
X = digits.data                                       # 64 pixel con valori da 0 a 16 (stessa scala)

#decide quante feature
pca_tutte = PCA().fit(X)

#percentuale dati
cumulata = np.cumsum(pca_tutte.explained_variance_ratio_)
#feature che superano 0.95. Decide 29
print("Componenti per il 95% della varianza:", np.argmax(cumulata >= 0.95) + 1)

#se tra 0-1 n_components cambia comportamento: spiega percentuale dei dati che i componenti coprono
pca95 = PCA(n_components=0.95).fit(X)                 # decimale = frazione di varianza da conservare
print("Con n_components=0.95:", pca95.n_components_, "componenti")

fig, axes = plt.subplots(1, 4, figsize=(12, 3))
axes[0].plot(range(1, 65), cumulata); axes[0].set_title("Varianza cumulata")
axes[0].set_xlabel("n. componenti")
for ax, k in zip(axes[1:], [5, 15, 40]):
    #choose amount of PCs
    pca_k = PCA(n_components=k).fit(X)
    # create a variable that decompresses the compression of the first element
    ricostruita = pca_k.inverse_transform(pca_k.transform(X[:1]))
    ax.imshow(ricostruita.reshape(8, 8), cmap="gray"); ax.set_title(f"{k} componenti")
plt.show()