#Esercizio omnicomprensivo — Screening diagnostico con scikit-learn
#Un ospedale vuole un sistema di supporto allo screening dei tumori al seno.
#  Per ogni paziente dispone di 30 misure numeriche ricavate da un'immagineù
#  di un nodulo. Il sistema deve prevedere se il tumore è maligno o benigno.
#Il team clinico pone due vincoli:
#un tumore maligno non riconosciuto è l'errore più grave;
#il numero da comunicare alla direzione deve essere onesto,
#  cioè stimato su dati mai usati per addestrare o scegliere il modello.

###1 Definizione del problema
print("\nSEZIONE 1")
print("Questo è un problema di classificazione, dove andiamo ad utilizzare un modello supervisionato. Target è una lista binaria che ci dice se il tumore è maligno o benigno.")

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.dummy import DummyClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

import pandas as pd
import numpy as np

bc = load_breast_cancer()
X, y = bc.data, bc.target
df = load_breast_cancer(as_frame=True).frame

###2 Esplorazione dei dati
print("\nSEZIONE 2")
print("Forma di X: ", X.shape)
print("Forma di y: ", y.shape)
print("Nomi delle feature: ", bc.feature_names)
print("Nomi delle classi: ", bc.target_names)

print("Prime 5 righe: V\n", df.head())
print("DESCR: V\n", bc.DESCR)
print("Conto classi: V\n", df['target'].value_counts())

#divisione
dft = df['target']
df = df.drop(columns=['target'])
dfmax = df.describe().max()
print("Feature max: V\n", dfmax)
dfmin = df.describe().min()
print("Feature min: V\n", dfmin)

###3 Divisione dei dati
#split 60-20-20 (train, val, test)
print("\nSEZIONE 3")
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, train_size=0.75, random_state=42, stratify=y_temp)

print("Dimensioni train: ", X_train.shape[0])
print("Dimensioni valutazione: ", X_val.shape[0])
print("Dimensioni test: ", X_test.shape[0])

for name, group in [("Train", y_train), ("Valutazione", y_val), ("Test", y_test)]:
    perc =  sum(group==0) / group.shape[0] * 100
    print("Percentuale maligni in "+name+": "+str(perc)+"%")

#4 Baseline
print("\nSEZIONE 4")
dummy = DummyClassifier(strategy="most_frequent")

dummy.fit(X_train, y_train)

print("Punti Accuratezza dummy: ", accuracy_score(y_val, dummy.predict(X_val)))
print("Punti Recall dummy: ", recall_score(y_val, dummy.predict(X_val), pos_label=0, zero_division=0))
#Questa soglia va battuta perché i falsi positivi (che indicano erronoamente sanità) sono pericolosi per il problema che dobbiamo risolvere.
# L'accuratezza alta può ingannare perché questa indica solamente quante predizioni sono vere.

#5 Primo modello: KNN senza scaling
print("\nSEZIONE 5")

knc = KNeighborsClassifier(n_neighbors=5)
knc.fit(X_train, y_train)

y_pred_train = knc.predict(X_train)
y_pred = knc.predict(X_val)

acc_knc1_train = accuracy_score(y_train, y_pred_train)
acc_knc1_val = accuracy_score(y_val, y_pred)
print("Punti Accuratezza KNC su train: ", acc_knc1_train)
print("Punti Accuratezza KNC su val: ", acc_knc1_val)

idx = 10
dists, idxs = knc.kneighbors(X_val[idx:idx+1])

print("Distanze dei vicini a "+str(idx)+": "+str(dists))
print("Indici dei vicini a "+str(idx)+": "+str(idxs))
print("Classi dei vicini a "+str(idx)+": "+str(y_train[idxs]))

X_maxs = X.max(axis=0) #calculates going down rows. axis=1 calculates going across columns.
X_mins = X.min(axis=0)

scales = X_maxs - X_mins
max_scale_x = np.argmax(scales)
min_scale_x = np.argmin(scales)

print("Feature con scale massima: ", max_scale_x, bc.feature_names[max_scale_x])
print("Feature con scale minima: ", min_scale_x, bc.feature_names[min_scale_x])
print("Questo è un problema perché la scala di una feature può influire sulla valutazione, anche se quella X non è più o meno importante.")

#6 Scaling e regola d'oro
print("\nSEZIONE 6")

scaler = StandardScaler()

X_train_s = scaler.fit_transform(X_train) #train on X_train and transform
X_val_s = scaler.transform(X_val) #transform X_val & X_test
X_test_s = scaler.transform(X_test)

print("Scaler STD")
print("Media X Train:", X_train_s.mean()) #esce in notazione scientifica ma è vicina a 0
print("Deviazione standard X Train:", X_train_s.std()) # 1

print("Media X val:", X_val_s.mean()) #anche vicino a 0 ma molto di meno
print("Deviazione standard X val:", X_val_s.std()) #non esattamente 1
print("La differenza dei risultati indica che l'allenamento è stato effettuato solamente con i dati di X_train.")
print("Questo perché gli outlier di X_val non arrivano alla stessa proporzione di quelli del training.")

knc.fit(X_train_s, y_train)

y_pred_train = knc.predict(X_train_s)
y_pred = knc.predict(X_val_s)

acc_knc2_train = accuracy_score(y_train, y_pred_train)
acc_knc2_val = accuracy_score(y_val, y_pred)
print("\nScaler STD")
print("Punti Accuratezza KNC su train: ", acc_knc2_train)
print("Punti Accuratezza KNC su val: ", acc_knc2_val)
print("Punti Accuratezza KNC su train (scorsi): ", acc_knc1_train)
print("Punti Accuratezza KNC su val (scorsi): ", acc_knc1_val)

#confronto con MinMaxScaler
scaler = MinMaxScaler()

#transform again
X_train_s = scaler.fit_transform(X_train)
X_val_s = scaler.transform(X_val)
#X_test_s = scaler.transform(X_test)

#allena
knc.fit(X_train_s, y_train)

#predict
y_pred_train = knc.predict(X_train_s)
y_pred = knc.predict(X_val_s)

acc_knc2_train = accuracy_score(y_train, y_pred_train)
acc_knc2_val = accuracy_score(y_val, y_pred)
print("\nScaler MinMax")
print("Punti Accuratezza KNC su train: ", acc_knc2_train)
print("Punti Accuratezza KNC su val: ", acc_knc2_val)

#I modelli che hanno bisogno dello scaling sono quelli che misurano vicinanza dei valori come KNN, 
# ma altri come DecisionTreeClassifier che utilizzano risposte binarie possono mantenere efficacia senza scaling.
# In questo caso osserviamo che entrambi gli scaler si rivelano efficaci per KNN.

#7 Scelta di k e diagnosi del modello
print("\nSEZIONE 7")