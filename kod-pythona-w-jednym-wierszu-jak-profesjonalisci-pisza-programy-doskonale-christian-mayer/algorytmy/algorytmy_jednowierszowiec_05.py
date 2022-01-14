# Obliczanie zbioru potęgowego przy użyciu programowania funkcyjnego


# Zależności
from functools import reduce

# Dane
s = {1, 2, 3}

# Jednowierszowiec
ps = lambda s: reduce(lambda P, x: P + [subset | {x} for subset in P], s, [set()])

# Wynik
print(ps(s))
'''
[set(), {1}, {2}, {1, 2}, {3}, {1, 3}, {2, 3}, {1, 2, 3}]
'''
