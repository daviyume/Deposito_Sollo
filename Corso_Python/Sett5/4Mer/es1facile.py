#5.3
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X, _ = make_blobs(n_samples=400, centers=3, cluster_std=1.0, random_state=7)

fig, ax = plt.subplots(1, 3, figsize = (12, 4))
plt.subplots_adjust(wspace=0.4, hspace=0.4)

for (k, n) in zip([3, 2, 5], range(3)):
    kmeans = KMeans(n_clusters=k, init="k-means++", n_init=8, random_state=42)
    labels = kmeans.fit_predict(X)
    #crea etichette

    #x & y in plot
    ax[n].scatter(X[:, 0], X[:, 1], c=labels, cmap="cividis")

    #clusters
    #T scambia x e y, * spacchetta in 2 elementi diversi
    ax[n].scatter(*kmeans.cluster_centers_.T, c="#FFBBFF", s=128, marker="X", alpha=0.5)
    
    
    ax[n].set_xlabel("X axis")
    ax[n].set_ylabel("Y axis")
    ax[n].set_title("Clusters con K con valore di "+str(k))

plt.show()