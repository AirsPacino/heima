import re

patten = "itcast"
string = "itcastha"

result = re.match(patten, string)
print(result.group())