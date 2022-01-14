# Analiza danych dotyczących pracy serca za pomocą konkatenacji list

## Zależności
import matplotlib.pyplot as plt

## Dane
cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

## Jednowierszowiec
expected_cycles = cardiac_cycle[1:-2] * 10

## Wynik
plt.plot(expected_cycles)
plt.show()
