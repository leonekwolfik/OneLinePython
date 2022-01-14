# Wyznaczanie liczb pierwszych za pomocą sita Eratostenesa


## Zależności
from functools import reduce

## Dane
n = 100

## Jednowierszowiec
primes = reduce(lambda r, x: r - set(range(x**2, n, x)) if x in r else r, range(2, int(n**0.5) + 1), set(range(2, n)))

## Wynik
print(primes)
'''
{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
'''
