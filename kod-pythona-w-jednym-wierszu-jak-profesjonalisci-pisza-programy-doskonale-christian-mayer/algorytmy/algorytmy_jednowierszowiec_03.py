# Obliczanie permutacji z użyciem rekurencyjnych funkcji silni


## Dane
n = 5

## Jednowierszowiec
factorial = lambda n: n * factorial(n-1) if n > 1 else 1

## Wynik
print(factorial(n))
'''
120
'''
