from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

wine = load_wine()
X = wine.data
scaler = StandardScaler()
X_s = scaler.fit_transform(X)

pca = PCA(n_components=2)
#new features
X_pca = pca.fit_transform(X_s)

print("Varianza spiegata:", pca.explained_variance_ratio_.round(3))

#### no scale
pca2 = PCA(n_components=2)
X_pca2 = pca.fit_transform(X)
####

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.scatter(X_pca[:, 0], X_pca[:, 1], c=wine.target, cmap="Blues", edgecolor="k")
ax1.set_xlabel("Prima componente principale"); plt.ylabel("Seconda componente principale")
ax1.set_title("Wines dopo la PCA")

ax2.scatter(X_pca2[:, 0], X_pca2[:, 1], c=wine.target, cmap="Blues", edgecolor="k")
ax2.set_xlabel("Prima componente principale"); plt.ylabel("Seconda componente principale")
ax2.set_title("Wines dopo la PCA (non scalato)")
#set_ for ax

plt.show()

#quella più accurata è PCA1, perché senza lo scaling le feature che 
# variano di più vengono individuate correttamente.