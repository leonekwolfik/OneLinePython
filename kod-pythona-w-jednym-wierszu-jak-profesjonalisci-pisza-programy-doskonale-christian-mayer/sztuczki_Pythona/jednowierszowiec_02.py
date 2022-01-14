# Użycie listy składanej do wyszukiwania słów o dużej wartości informacyjnej


## Dane
text = '''
Imię moje: Izmael. Przed kilku laty — mniejsza o ścisłość jak dawno temu 
— mając niewiele czy też nie mając wcale pieniędzy w sakiewce, a nie widząc 
nic szczególnego, co by mnie interesowało na lądzie, pomyślałem sobie, że 
pożegluję nieco po morzach i obejrzę wodną część świata. Taki mam właśnie 
sposób odpędzania splinu i regulowania krwiobiegu. - Moby Dick'''

## Jednowierszowiec
w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]

## Wynik
print(w)
'''
[[], ['Imię', 'moje:', 'Izmael.', 'Przed', 'kilku', 'laty', 'mniejsza', 'ścisłość', 'dawno', 'temu'], 
['mając', 'niewiele', 'mając', 'wcale', 'pieniędzy', 'sakiewce,', 'widząc'], 
['szczególnego,', 'mnie', 'interesowało', 'lądzie,', 'pomyślałem', 'sobie,'], 
['pożegluję', 'nieco', 'morzach', 'obejrzę', 'wodną', 'część', 'świata.', 'Taki', 'właśnie'], 
['sposób', 'odpędzania', 'splinu', 'regulowania', 'krwiobiegu.', 'Moby', 'Dick']]
'''
