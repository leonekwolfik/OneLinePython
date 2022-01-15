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


avg, var, std = np.average(x, axis=1), np.var(x, axis=1), np.std(x, axis=1)

a, v, s = [f(x, axis=1) for f in (np.average, np.var, np.std)]

print(avg, var, std)
print(a, v, s)