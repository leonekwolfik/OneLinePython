import re

text = '''
Anna Kowalska wyszła za mąż za Jana Nowaka.
Dawna 'Anna Kowalska' nazywa się teraz Anna Nowak.
Anna Kowalska zmieniła swoje poprzednie nazwisko 'Kowalska' na 'Nowak'.
Siostra Anny, Janina Kowalska, nadal nosi swoje dotychczasowe nazwisko.
'''

updated_text = re.sub("Anna Kowalska(?!')", 'Anna Nowak', text)

print(updated_text)

assert updated_text != text
assert updated_text.startswith("Anna Nowak")
