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

duplicates = re.findall('([^\s]*(?P<x>[^\s])(?P=x)[^\s]*)', text)
duplicates2 = re.findall('([a-z]*(?P<x>[a-z])(?P=x)[a-z]*)', text)

print(duplicates)
print(duplicates2)
