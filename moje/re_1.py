import re

text = '''Blockchain (lacuch bloków lub lancuch blokowy) to rosnaca lista rekordów, 
tzw. bloków, tkóre są powiązane za pomocą funkcji kryptograficznych.
'''

print(re.findall('b..k', text))

#  asterysk
print(re.findall('y.*y', text))

print(re.findall('abc*', text))

print(re.findall('abc*', "wwww ab, abc, abcc, abccdc, ababa, asdfef"))

print(re.findall('blokó?', text))

txt = '<div>Witaj, świecie</div>'

# zachłanny
print(re.findall('<.*>', txt))

# niezachłanny
print(re.findall('<.*?>', txt))


string = "itajświecie"

regex_1 = 'witaj(świecie)'
regex_2 = '(witaj(świecie))'

res_1 = re.findall(regex_1, string)
res_2 = re.findall(regex_2, string)

print(res_1)
print(res_2)
