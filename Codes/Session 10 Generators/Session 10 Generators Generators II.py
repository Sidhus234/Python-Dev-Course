# LIST is iterable
# Iterable is any item through which we can iter through

# Generators are iterable
# Not everything that is iterable, is generator


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result



def generator_function(num):
    for i in range(num):
        yield i*2
        
g = generator_function(100)
print(g)
print(next(g))
print(next(g))
print(next(g))

for item in generator_function(1000):
    print(item)

# yield pauses the function, and comes back to it when we do 'next'
# yield keyword converts the function to generator
        

        
        
        
        