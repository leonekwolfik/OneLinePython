# Walidacja formatu zapisu czasu wprowadzanego przez użytkownika, część I


## Zależności
import re

## Dane
inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

## Jednowierszowiec
input_ok = lambda x: re.fullmatch('[0-9]{2}:[0-9]{2}', x) != None

## Wynik
for x in inputs:
    print(input_ok(x))
'''
True
True
False
False
False
True
'''
