# formatted strings
name = 'Johnny'
age = 55
print('hi ' + name + '. You are ' + str(age) + ' years old')

# formatted strings (new to Python 3)
print(f'hi {name}. You are {age} years old')

print(('hi {}. You are {} years old').format(name, str(age)))
