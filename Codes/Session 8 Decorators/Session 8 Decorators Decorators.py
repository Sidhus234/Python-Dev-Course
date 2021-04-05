# Decorators
# start with @ sign
# for example: @classmethod
# for example: @staticmethod

# Functions in python are "First class citizens". They can be passed around 
# like variables, they can arguements in a function

def hello():
    print('helloooo')

greet = hello
print(greet())

del hello
# delete deltes name reference to hello function. Hence hello won't work, 
# but greet will work as it is still pointing to that location in memory
print(greet())
print(hello()) # this won't work

###################################
def hello(func):
    func()
    
def greet():
    print('still here')

print(hello(greet))

# Decorators are possible due to ability of functions to act as variables
# Decorators supercharge our function

# Higher order function: HOC 
# Can be one of two things:
# 1. it can a function which accepts other function
def greet(func):
    func()

# 2. If it returns another function
def greet2():
    def func():
        return 5
    return func

# Hence map, reduce, filter and others are higher order funcitons
    


