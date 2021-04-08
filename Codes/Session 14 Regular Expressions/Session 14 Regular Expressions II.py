import re
# More details can be found here: https://www.w3schools.com/python/python_regex.asp

# Regular Expressions come useful for advanced patterns

# search for a-z(lower or capital) followed by any char and then small 'a'
pattern = r'[a-zA-Z].([a])'
string = 'Hey how are you!?'

a = re.search(pattern, string)
print(a)
print(a.start())
print(a.group())

# r means raw string in Python
pattern = r'[a-zA-Z].([a])'

print(a.group(0))
print(a.group(1))

# More problems about regex can be found here:
# https://regexone.com/