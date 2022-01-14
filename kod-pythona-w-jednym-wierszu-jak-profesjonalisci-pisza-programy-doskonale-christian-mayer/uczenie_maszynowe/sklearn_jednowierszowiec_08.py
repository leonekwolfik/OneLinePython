# Podstawowe parametry statystyczne


## Zależności
import numpy as np

## Dane o cenach akcji: 5 spółek
# (wiersz=[cena_w_1_dniu, cena_w_2_dniu, ...])
x = np.array([[8, 9, 11, 12],
              [1, 2, 2, 1],
              [2, 8, 9, 9],
              [9, 6, 6, 3],
              [3, 3, 3, 3]])

## Jednowierszowiec
avg, var, std = np.average(x, axis=1), np.var(x, axis=1), np.std(x, axis=1)

## Wynik
print("Średnie: " + str(avg))
print("Wariancje: " + str(var))
print("Odchylenia standardowe: " + str(std))
'''
Średnie: [10.   1.5  7.   6.   3. ]
Wariancje: [2.5  0.25 8.5  4.5  0.  ]
Odchylenia standardowe: [1.58113883 0.5        2.91547595 2.12132034 0.        ]
'''
