import numpy as np
from sklearn.linear_model import LinearRegression

#devono essere array "D per il fit". Righe separate
temperatura = np.array([[18], [21], [24], [27], [30], [33]])
gelati_venduti = np.array([120, 150, 190, 230, 260, 310])

linreg = LinearRegression()
linreg.fit(temperatura, gelati_venduti)

print("Coefficiente w:", round(linreg.coef_[0]))
print("Intercetta b:", round(linreg.intercept_))
print("Il coefficiente indica la pendenza w, ovvero in media quanto y cambia per ogni unità (+1) di x")

n = 29
print("\nPrevisione per ", n, " gradi: ", linreg.predict([[n]]))