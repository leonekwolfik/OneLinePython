# Użycie wyrażeń generatora do wyszukania firm, które płacą poniżej płacy minimalnej

## Dane
companies = {
    'FajnaFirma' : {'Alicja' : 62, 'Robert' : 53, 'Franciszek' : 55},
    'SkąpaFirma' : {'Anna' : 8, 'Leszek' : 17, 'Krystyna' : 13},
    'TakaSobieFirma' : {'Elżbieta' : 72, 'Karol' : 15, 'Paweł' : 34}
    }

## Jednowierszowiec
illegal = [x for x in companies if any(y<17 for y in companies[x].values())]

## Wynik
print(illegal)
'''
['SkąpaFirma', 'TakaSobieFirma']
'''

