import re

text = '''
"Nigdy się nie ma za dużo skarpetek", powiedział Dumbledore.
"minęło jeszcze jedno Boże Narodzenie, a ja znowu nie dostałem ani jednej pary.
Wszyscy wciąż dają mi ksiązki".
Cytat na Boże Narodzenie
'''

regex = 'Boże.*'

print(re.match(regex, text))

print(re.search(regex, text))

print(re.findall(regex, text))

