# Wyszukiwanie prostych wzorców tekstowych w łańcuchach znaków


## Zależności
import re

## Dane
text = 'król Karol kupił królowej Karolinie korale koloru koralowego'

## Jednowierszowiec
result = re.findall('k.*?r.*?l', text)

## Wynik
print(result)
'''
['król', 'kupił król', 'koral', 'koloru koral']
'''
