import urllib.request

search_phrase = 'Rosja'

with urllib.request.urlopen('https://tech.wp.pl/') as response:
    html = response.read().decode("utf8")
    first_pos = html.find(search_phrase)
    print(html[first_pos-12:first_pos+12])
