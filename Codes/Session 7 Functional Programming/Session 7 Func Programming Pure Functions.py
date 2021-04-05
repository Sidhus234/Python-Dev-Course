# Functional Programming
# Separation of concerns - each part concerns itself with one thing that it is good at
# Data and methods are separated

# Clear and Understandable
# Easy to extend
# easy to maintain
# memory efficient
# DRY: Donot repeat yourself

# PURE Functions: data and behavior of program are separated
# PURE Func has below two factors:
# 1. Given the same input, return the same output (no matter how many time)
# 2. Function should not produce any side effect
# Printing is outside world, and hence should not be done in function
# Function  should not touch a variable which lives in outside world

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3,4]))

##############
# This has side effects, and hence not a pure function
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return print(new_list)
multiply_by2([1,2,3,4])


# Outside variable in manipulated. Hence not a PURE func
new_list = []
def multiply_by2(li):
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3,4]))

# PURE Functions are important to have less buggy code
# Its impossible to have PURE functions everywhere, but try to limit them 
