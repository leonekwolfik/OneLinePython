# Podstawowe działania na tablicach dwuwymiarowych


## Zależności
import numpy as np

## Dane: wynagrodzenie roczne (w tysiącach) za lata [2017, 2018, 2019]
alicja = [99, 101, 103]
robert = [110, 108, 105]
tomasz = [90, 88, 85]
salaries = np.array([alicja, robert, tomasz])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])

## Jednowierszowiec
max_income = np.max(salaries - salaries * taxation)

## Wynik
print(max_income)
'''
81.0
'''
