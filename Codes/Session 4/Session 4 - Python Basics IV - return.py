# return is keyword used a lot in function

def sum(num1, num2):
    return (num1 + num2)

print(sum(4,5))

# A function should do one thing really well
# A function should return something

total = sum(5, 10)
print(total)

print(sum(10, total))


def sum(num1, num2):
    def another_func(num1, num2):
        return num1+num2
    return another_func(num1, num2)
    
total = sum(10, 20)
print(total)


# First "Return" statement ends the function. Anything after that is useles
