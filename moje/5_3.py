import re

## Dane
page = '''
<!DOCTYPE html>
<html>
<body>
<h1>My Programming Links</h1>
<a href="https://app.finxter.com/">test your Python skills</a>
<a href="https://blog.finxter.com/recursion/">Learn recursion</a>
<a href="https://nostarch.com/">Great books from NoStarchPress</a>
<a href="http://finxter.com/">Solve more Python puzzles</a>
<a href="http://finxter.com/">Solve more Python  abc</a>
</body>
</html>
'''

practice_tests = re.findall("(<a.*?finxter.*?(test|abc|puzzle).*?>)", page)

print(practice_tests)
