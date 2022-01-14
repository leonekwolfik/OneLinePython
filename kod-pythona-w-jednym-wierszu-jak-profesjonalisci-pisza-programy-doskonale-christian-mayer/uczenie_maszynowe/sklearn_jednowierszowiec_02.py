# Regresja logistyczna
from sklearn.linear_model import LogisticRegression
import numpy as np

## Dane (liczba papierosów, rak)
X = np.array([[0, "Nie"],
              [10, "Nie"],
              [60, "Tak"],
              [90, "Tak"]])

## Jednowierszowiec
model = LogisticRegression().fit(X[:,0].reshape(-1,1), X[:,1])

## Wynik
print(model.predict([[2],[12],[13],[40],[90]]))
'''
['Nie' 'Nie' 'Nie' 'Tak' 'Tak']
'''
