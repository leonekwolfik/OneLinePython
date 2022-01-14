# Wykrywanie powtórzeń słów


## Zależności
import re

## Dane
text = 'zbyt czeste uzywanie slow powoduje zuzywanie sie slow'

## Jednowierszowiec
style_problems = re.search('\s(?P<x>[a-z]+)\s+([a-z]+\s+){0,10}(?P=x)\s', ' ' + text + ' ')

## Wynik
print(style_problems)
'''
<re.Match object; span=(21, 55), match=' slow powoduje zuzywanie sie slow '>
'''
