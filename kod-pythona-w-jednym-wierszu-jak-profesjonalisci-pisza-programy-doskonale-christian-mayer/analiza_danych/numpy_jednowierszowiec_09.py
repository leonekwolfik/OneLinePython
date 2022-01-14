# Prosta analiza asocjacji: klienci, którzy kupili X, kupili również Y


## Zależności
import numpy as np

## Dane: wiersz to koszyk zakupów klienta
## wiersz = [kurs 1, kurs 2, e-book 1, e-book 2]
## wartość 1 oznacza, że dany produkt został zakupiony
basket = np.array([[0, 1, 1, 0],
                   [0, 0, 0, 1],
                   [1, 1, 0, 0],
                   [0, 1, 1, 1],
                   [1, 1, 1, 0],
                   [0, 1, 1, 0],
                   [1, 1, 0, 1],
                   [1, 1, 1, 1]])

## Jednowierszowiec
copurchases = np.sum(np.all(basket[:,2:], axis = 1)) / basket.shape[0]

## Wynik
print(copurchases)
'''
0.25
'''
