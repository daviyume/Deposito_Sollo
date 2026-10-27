import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

knc = KNeighborsClassifier(n_neighbors=5)
knc.fit(X_train, y_train)

y_pred = knc.predict(X_test)

# Compare actual labels with predicted labels
cm = metrics.confusion_matrix(y_test, y_pred)

# Display the confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=iris.target_names,
    yticklabels=iris.target_names
)

plt.xlabel('Predicted species')
plt.ylabel('Actual species')
plt.title('Iris Confusion Matrix')
plt.tight_layout()
plt.show()

#LLM example