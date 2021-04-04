for i, char in enumerate('Hellooo'):
    print(i, char)
    
    
for i, char in enumerate([1,2,3,4]):
    print(i, char)
    
for i, char in enumerate((1,2,3,4,5)):
    print(i, char)

# Enumerate gives index, and value of iterable item
for i, char in enumerate(list(range(100))):
    if (char == 50):
        print (i, char)