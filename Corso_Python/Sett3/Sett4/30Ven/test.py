import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score, confusion_matrix

X, y = make_classification(n_samples=2000, weights=[0.95, 0.05], random_state=42)   # 5% di positivi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y) #stratify target

pigro = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)   # prevede SEMPRE la classe 0
albero = DecisionTreeClassifier(max_depth=5, random_state=42).fit(X_train, y_train)

for nome, m in [("Dummy", pigro), ("Albero", albero)]:
    y_pred = m.predict(X_test)
    print(f"{nome:7s} accuracy={accuracy_score(y_test, y_pred):.3f} "
          f"recall={recall_score(y_test, y_pred, zero_division=0):.3f} "
          f"f1={f1_score(y_test, y_pred, zero_division=0):.3f}")
#test both

cm = confusion_matrix(y_test, albero.predict(X_test))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",              # annot: scrive i numeri nelle celle
            xticklabels=["neg", "pos"], yticklabels=["neg", "pos"])
plt.xlabel("Previsto"); plt.ylabel("Reale"); plt.title("Matrice di confusione - albero")
plt.show()