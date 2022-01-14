# Walidacja formatu zapisu czasu wprowadzanego przez użytkownika, część II


## Zależności
import re

## Dane
inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

## Jednowierszowiec
input_ok = lambda x: re.fullmatch('([01][0-9]|2[0-3]):[0-5][0-9]', x) != None

## Wynik
for x in inputs:
    print(input_ok(x))
'''
True
True
False
False
False
False
'''
