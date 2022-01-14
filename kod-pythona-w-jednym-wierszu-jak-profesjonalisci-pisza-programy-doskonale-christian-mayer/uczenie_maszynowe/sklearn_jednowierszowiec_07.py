# Wyszukiwanie wiersza z minimalną wariancją


## Zależności
import numpy as np

## Dane (wiersze: akcje / kolumny: ceny akcji)
X = np.array([[25,27,29,30],
              [1,5,3,2],
              [12,11,8,3],
              [1,1,2,2],
              [2,6,2,2]])

## Jednowierszowiec: wyszukiwanie akcji z najmniejszą wariancją
min_row = min([(i,np.var(X[i,:])) for i in range(len(X))], key=lambda x: x[1])

## Wynik
print("Wiersz z minimalną wariancją: " + str(min_row[0]))
print("Wariancja: " + str(min_row[1]))
'''
Wiersz z minimalną wariancją: 3
Wariancja: 0.25
'''
