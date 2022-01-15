import re

text_1 = "kryptobot do handlu bitcoinami i innymi walutami"
text_2 = "kryptograficzne metody szyfrowania, które można łatwo złamać za pomocą komputerów kwantowych"

pattern = re.compile("krypto(.{1,30})coin")

print(pattern.match(text_1))
print(pattern.match(text_2))
