import re

article = '''
Algorytm ma ważne praktyczne zastosowania
http://blog.finxter.com/applications/
w wielu podstawowych strukturach danych, takich jak zbiory, drzewa,
słowniki, zasobniki, drzewa zasobników, słowniki zasobników,
https://blog.finxter.com/sets-in-python/
tabele skrótów, mapy i tablice. http://blog.finxter.com/
http://nieprawidłowy-url
http:/bla.ba.com
http://bo.bo.bo.bo.bo.bo/
http://bo.bo.bo.bo.bo.bo/333483--33343-/
'''

stale_links = re.findall('http://[a-z0-9_\-\.]+\.[a-z0-9_\-/]+', article)

print(stale_links)
