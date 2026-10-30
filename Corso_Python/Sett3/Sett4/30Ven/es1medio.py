#2.5
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np

#load
X, y = load_digits().data, load_digits().target

#split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, stratify=y, random_state=144)

#scale
scaler = MinMaxScaler().fit(X_train)
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

#train
dtc = DecisionTreeClassifier().fit(X_train_s, y_train)

#predict
y_pred = dtc.predict(X_test_s)

#classification
print("CLASSIFICATION REPORT: ")
print(classification_report(y_test, y_pred))

#matrix
cm = confusion_matrix(y_test, y_pred)

matrixdisplay = ConfusionMatrixDisplay(confusion_matrix=cm)
matrixdisplay.plot()
plt.show()

#matrix = numpy array
min = cm.argmin()
print(min)
print(cm)

#trova valore con confusione più alta (che non sia vero)
max_conf_r = 0
max_conf_c = 1 #diverso da zero per selezionare un valore falso
for r in range(cm.shape[0]):
    for c in range(cm.shape[1]):
        if r != c and cm[r, c] > cm[max_conf_r, max_conf_c]:
            max_conf_r = r
            max_conf_c = c

print("La confusione più probabile è di ", max_conf_r, " scambiato per ", max_conf_c)