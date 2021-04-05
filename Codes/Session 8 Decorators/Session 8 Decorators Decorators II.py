# Decorators supercharges a function
    
def my_decorator(func):
    def wrap_func():
        print('***************')
        func()
        print('***************')
    return wrap_func

@my_decorator
def hello():
    print('helloooo')

hello()

def bye():
    print('see ya later')

bye()

@my_decorator
def bye():
    print('see ya later')

bye()
# Decorator allows us to reuse functionality for different functions


def hello1():
    print('helloooo')

# above code does
hello2 = my_decorator(hello1)
hello2()
