# Użycie wycinania do ekstrakcji środowisk dopasowanych łańcuchów podrzędnych

## Dane
letters_amazon = '''
Spędziliśmy kilka lat, budując własny silnik bazy danych, Amazon Aurora. 
Jest to w pełni zarządzana usługa zgodna z MySQL i PostgreSQL, która 
pod względem trwałości i dostępności dorównuje silnikom komercyjnym, 
a nawet je prześciga - ale za jedną dziesiątą kosztów. Nie byliśmy 
zaskoczeni, kiedy okazało się, że to działa.
'''

## Jednowierszowiec
find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1

## Wynik
print(find(letters_amazon, 'SQL'))
'''
usługa zgodna z MySQL i PostgreSQL, 
'''
