# Regresja liniowa


## Zależności
from sklearn.linear_model import LinearRegression
import numpy as np

## Dane (ceny akcji firmy Apple)
apple = np.array([155, 156, 157])
n = len(apple)

## Jednowierszowiec
model = LinearRegression().fit(np.arange(n).reshape((n,1)), apple)

## Wynik
print(model.predict([[3],[4]]))
'''
[158. 159.]
'''
