# Obliczanie ciągów Fibonacciego za pomocą funkcji reduce()


# Zależności
from functools import reduce

# Dane
n = 10

# Jednowierszowiec
fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1])

# Wynik
print(fibs)
'''
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''
