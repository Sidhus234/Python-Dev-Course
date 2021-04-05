# Decorators supercharges a function
    
def my_decorator(func):
    def wrap_func(x, y):
        print('***************')
        func(x, y)
        print('***************')
    return wrap_func

@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)
    
hello('hihi', ':)')
    
# Other way to do this
# Decorator Pattern
# Allows to pass as many as inputs as required
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***************')
        func(*args, **kwargs)
        print('***************')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':(')):
    print(greeting, emoji)
    
hello('hihi', ':)')
    
