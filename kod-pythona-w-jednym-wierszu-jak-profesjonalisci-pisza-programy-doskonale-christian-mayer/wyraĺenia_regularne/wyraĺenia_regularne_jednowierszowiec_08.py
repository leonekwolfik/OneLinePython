# Wykrywanie zduplikowanych znaków w łańcuchach


## Zależności
import re

## Dane
text = '''
Jak lekko, żwawo skacze rtęć
I rośnie słupek w termometrze —
Trzydzieści siedem, kresek pięć!
Ach, tak niewinnie się zaczyna!
Tylko oddechy coraz prędsze,
I pod oczami sine piętna...
Jak po drabinie rtęć się wspina,
Po kreskach — srebrna, obojętna...
-- Jerzy Liebert, Pieśń o zagładzie, 1934
'''

## Jednowierszowiec
duplicates = re.findall('([^\s]*(?P<x>[^\s])(?P=x)[^\s]*)', text)

## Wynik
print(duplicates)
'''
[('lekko,', 'k'), ('niewinnie', 'n'), ('oddechy', 'd'), 
('piętna...', '.'), ('obojętna...', '.'), ('--', '-')]
'''
