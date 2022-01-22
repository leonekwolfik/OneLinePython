is_palindrome = lambda phrase: phrase == phrase[::-1]

print(is_palindrome("anna"))
print(is_palindrome("kdljfasjf"))
print(is_palindrome("igor łamał rogi"))
print(is_palindrome("igor łamał  rogi"))

import re
is_palindrome = lambda phrase: re.sub('\s', '', phrase) == re.sub('\s', '', phrase)[::-1]

print(is_palindrome("anna"))
print(is_palindrome("kdljfasjf"))
print(is_palindrome("igor łamał rogi"))
print(is_palindrome("igor łamał  rogi"))

is_palindrome = lambda phrase: str(phrase).strip() == str(phrase).strip()[::-1]

print(is_palindrome("anna"))
print(is_palindrome("kdljfasjf"))
print(is_palindrome("igor łamał rogi"))
print(is_palindrome("igor łamał  rogi"))
