# Wyszukiwanie anagramów za pomocą funkcji lambda i sortowania


## Jednowierszowiec
is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)

## Wynik
print(is_anagram("urwis", "wirus"))
print(is_anagram("urwisu", "wiruus"))
print(is_anagram("urwis", "jeden"))
'''
True
True
False
'''
