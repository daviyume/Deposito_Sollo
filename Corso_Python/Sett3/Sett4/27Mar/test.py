#EX AVANZATO
#Compare k (n_neighbors) between 1 and 30.

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.inspection import DecisionBoundaryDisplay

X, y = load_iris(return_X_y=True)
X2 = X[:, [0, 1]]             # solo 2 feature per poter disegnare sul piano
#only X2 is used, simplified version with only 2 features (0, 1)

fig, axes = plt.subplots(1, 2, figsize=(11, 4))

#for each subplot use different k
for ax, k in zip(axes, [1, 30]):
    knn = KNeighborsClassifier(n_neighbors=k).fit(X2, y)
    #model instance creation and fit in one line
    DecisionBoundaryDisplay.from_estimator(
        knn, X2, response_method="predict", alpha=0.4, ax=ax)
      #draw decision regions on the graph (colors the axis based on the class)
      # knn: model used
      # X2: input features
      # response_method="predict" — predicts the class for each point in that area.
      # alpha: transparency of the display
      # ax=ax draws on our axis.
        
    ax.scatter(X2[:, 0], X2[:, 1], c=y, edgecolor="k", s=20)
    #scatter
    # place several points on the axis using the 2 features as coordinates for each.
    # color is coded based on class.
    # edgecolor is border color, set to black. Has nothing to do with k used for n_neighbors
    # s is size
    
    ax.set_title(f"k = {k}")
    ax.set_xlabel("lunghezza sepalo"); ax.set_ylabel("larghezza sepalo")
    
plt.show()

#Con k = 1 il confine è frastagliato e crea "isole" attorno a singoli punti: il modello insegue il rumore.
#Con k = 30 il confine è molto più liscio: il modello è più stabile ma può perdere dettagli.