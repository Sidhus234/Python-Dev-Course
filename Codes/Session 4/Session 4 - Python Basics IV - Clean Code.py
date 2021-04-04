# Clean code

def is_even(num):
    if(num % 2 == 0):
        return True
    elif (num % 2 != 0):
        return False

print(is_even(10))

print(is_even(13))

# How to clean it up
def is_even(num):
    if(num % 2 ==0):
        return True
    return False

print(is_even(51))


# Less lines of code and clean code
def is_even(num):
    return(num % 2 ==0)
    
print(is_even(51))