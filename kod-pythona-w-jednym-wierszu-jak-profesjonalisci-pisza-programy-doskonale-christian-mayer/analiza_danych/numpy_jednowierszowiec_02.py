# Praca z tablicami NumPy: wycinanie, rozgłaszanie i typy tablic


## Zależności
import numpy as np

## Dane: wynagrodzenie roczne (w tysiącach) za lata [2025, 2026, 2027]
dataScientist = [130, 132, 137]
productManager = [127, 140, 145]
designer = [118, 118, 127]
softwareEngineer = [129, 131, 137]
employees = np.array([dataScientist,
                      productManager,
                      designer,
                      softwareEngineer])

## Jednowierszowiec
employees[0,::2] = employees[0,::2] * 1.1

## Wynik
print(employees)
'''
[[143 132 150]
 [127 140 145]
 [118 118 127]
 [129 131 137]]
'''
