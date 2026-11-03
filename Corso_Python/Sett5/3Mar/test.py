import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

iris = load_iris()
X_scaled = StandardScaler().fit_transform(iris.data)    # prima lo scaling (qui nessun test set: solo esplorazione)

pca = PCA(n_components=2) #2 PC
X_pca = pca.fit_transform(X_scaled)                     # da length (150, 4) a (150, 2)

#varianza registrata da PC1 e da PC2
print("Varianza spiegata:", pca.explained_variance_ratio_.round(3))          # [0.73 0.229]
#indica alcuni dati persi
print("Totale conservato:", pca.explained_variance_ratio_.sum().round(3))

#print weights (c) for every iteration of a cycle defining c and f
print("PC1 =", {f: round(float(c), 2) for f, c in zip(iris.feature_names, pca.components_[0])})   # ricetta della PC1
print("PC2 =", {f: round(float(c), 2) for f, c in zip(iris.feature_names, pca.components_[1])})   # ricetta della PC2

# sono colorati perché c indica classi/colori
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=iris.target, cmap="viridis", edgecolor="k")
plt.xlabel("Prima componente principale"); plt.ylabel("Seconda componente principale")
plt.title("Iris dopo la PCA"); plt.show()