# Wyszukiwanie palindromów za pomocą funkcji lambda i wycinania ujemnego


## Jednowierszowiec
is_palindrome = lambda phrase: phrase == phrase[::-1]

## Wynik
print(is_palindrome("anna"))
print(is_palindrome("kdljfasjf"))
print(is_palindrome("igor łamał rogi"))
'''
True
False
True
'''
