# Rekurencyjny algorytm wyszukiwania binarnego


## Dane
l = [3, 6, 14, 16, 33, 55, 56, 89]
x = 33

## Jednowierszowiec
bs = lambda l, x, lo, hi: -1 if lo>hi else(lo+hi)//2 if l[(lo+hi)//2] == x else bs(l, x, lo, (lo+hi)//2-1) if l[(lo+hi)//2] > x else bs(l, x, (lo+hi)//2+1, hi)

## Wynik
print(bs(l, x, 0, len(l)-1))
'''
4
'''
