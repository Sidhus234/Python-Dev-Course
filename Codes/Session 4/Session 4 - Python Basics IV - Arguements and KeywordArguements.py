
# *args: arguements
# **kwargs: keyword arguements

def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))


def super_func(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args)

super_func(1,2,3,4,5, num1=5, num2=10) 

def super_func(*args, **kwargs):
    print(args)
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total

super_func(1,2,3,4,5, num1=5, num2=10)

# Rule of order:
# First are actual parameters
# * args
# Default parameters
# **Kwargs

def super_func(name, *args, i="hi", **kwargs):
    return