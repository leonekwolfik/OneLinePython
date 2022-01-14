# Użycie funkcji lambda i map

## Dane
txt = ['Funkcje lambda to funkcje anonimowe.',
       'Funkcje anonimowe nie mają nazwy.',
       'Funkcje w Pythonie są obiektami.']

## Jednowierszowiec
mark = map(lambda s: (True, s) if 'anonimowe' in s else (False, s), txt)

## Wynik
print(list(mark))
'''
[(True, 'Funkcje lambda to funkcje anonimowe.'),
(True, 'Funkcje anonimowe nie mają nazwy.'),
(False, 'Funkcje w Pythonie są obiektami.')]
'''
