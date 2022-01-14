# Szyfrowanie szyfrem Cezara przy użyciu zaawansowanego indeksowania i listy składanej


## Dane
abc = "abcdefghijklmnopqrstuvwxyz"
s = "xrosjaniexnadchodza"

## Jednowierszowiec
rt13 = lambda x: "".join([abc[(abc.find(c) + 13) % 26] for c in x])

## Wynik
print(rt13(s))
print(rt13(rt13(s)))
'''
kebfwnavrkanqpubqmn
xrosjaniexnadchodza
'''
