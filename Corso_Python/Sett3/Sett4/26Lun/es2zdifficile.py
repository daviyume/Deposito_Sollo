import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

#fig = plt.figure()
#axes = fig.add_subplot(1, 1, 1)

fig, axes = plt.subplots(1, 3)

#number examples, each example has 2 input features, 
X1, y1 = make_classification(n_samples=300, n_features=2, n_informative=2, n_redundant=0, random_state=42, class_sep=0.5)
X2, y2 = make_classification(n_samples=300, n_features=2, n_informative=2, n_redundant=0, random_state=42, class_sep=1.0)
X3, y3 = make_classification(n_samples=300, n_features=2, n_informative=2, n_redundant=0, random_state=42, class_sep=2.0)

#Cycles through every axis and tuple of 3 elements in the zip.
#zip pairs items together. Each iteration it brings the ax of the plot and the 3 cycled elements in the list.
#scatter: first feature (horizontal axis), second feature (vertical axis),
# color is equal to the class (target result),
# color map is viridis
#point size is 15
for ax, (X, y, titolo) in zip(axes, [(X1, y1, "make_classification"), (X2, y2, "make_classification"), (X3, y3, "make_classification")]):
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap="viridis", s=15)   # colore = classe
    ax.set_title(titolo)
plt.show()