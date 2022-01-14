# Modyfikowanie wzorców wyrażeń regularnych w wielowierszowym łańcuchu znaków


## Zależności
import re

## Dane
text = '''
Anna Kowalska wyszła za mąż za Jana Nowaka.
Dawna 'Anna Kowalska' nazywa się teraz Anna Nowak.
Anna Kowalska zmieniła swoje poprzednie nazwisko 'Kowalska' na 'Nowak'.
Siostra Anny, Janina Kowalska, nadal nosi swoje dotychczasowe nazwisko.
'''

## Jednowierszowiec
updated_text = re.sub("Anna Kowalska(?!')", 'Anna Nowak', text)

## Wynik
print(updated_text)
'''

Anna Nowak wyszła za mąż za Jana Nowaka.
Dawna 'Anna Kowalska' nazywa się teraz Anna Nowak.
Anna Nowak zmieniła swoje poprzednie nazwisko 'Kowalska' na 'Nowak'.
Siostra Anny, Janina Kowalska, nadal nosi swoje dotychczasowe nazwisko.

'''
