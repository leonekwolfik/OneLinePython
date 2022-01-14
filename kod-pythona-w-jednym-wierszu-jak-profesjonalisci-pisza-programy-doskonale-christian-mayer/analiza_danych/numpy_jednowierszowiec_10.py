# Bardziej zaawansowana analiza asocjacji w celu wyszukania najlepiej sprzedających się pakietów


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
copurchases = [(i,j,np.sum(basket[:,i] + basket[:,j] == 2)) for i in range(4) for j in range(i+1,4)]

## Wynik
print(max(copurchases, key=lambda x:x[2]))
'''
(1, 2, 5)
'''
