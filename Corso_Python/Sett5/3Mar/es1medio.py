#5.1
# Obiettivo: su load_breast_cancer() (30 feature, standardizzate) disegna 
# lo scree plot e la curva della varianza cumulata. Quante componenti 
# servono per il 90% e per il 99%? Stampa le 3 feature con il peso 
# (in valore assoluto) maggiore nella prima componente.
from sklearn.datasets import load_breast_cancer
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

bc = load_breast_cancer()

