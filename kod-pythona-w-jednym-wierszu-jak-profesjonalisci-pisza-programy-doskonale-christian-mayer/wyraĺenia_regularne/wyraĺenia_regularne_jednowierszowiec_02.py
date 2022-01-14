# Napisz własny scraper stron WWW z użyciem wyrażeń regularnych


## Zależności
import re

## Dane
text_1 = "kryptobot do handlu bitcoinami i innymi walutami"
text_2 = "kryptograficzne metody szyfrowania, które można łatwo złamać za pomocą komputerów kwantowych"

## Jednowierszowiec
pattern = re.compile("krypto(.{1,30})coin")

## Wynik
print(pattern.match(text_1))
print(pattern.match(text_2))
'''
<re.Match object; span=(0, 27), match='kryptobot do handlu bitcoin'>
None
'''
