import re

string = 'search inside of this text please!'

print('search' in string)

a = re.search('search', string)
print(a.span())
print(a.end())
print(a.start())
print(a.group())
# re library provides way more option

# re returns a match model or None

pattern = re.compile('this')
string = 'search this inside of this text please'

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
print(c)
d = pattern.match((string))
print(d)