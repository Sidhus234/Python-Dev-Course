def sum(num1, num2):
    try:
        return num1 + num2
    except:
        print("Something is wrong")

print(sum('1', 2))

# Good practice is to always capture specific type of exceptions

def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print(f"Please enter a number {err}")

print(sum('1', 2))

# Handling two errors at same time
def div(num1, num2):
    try:
        return num1/num2
    except(TabError, ZeroDivisionError):
        print('oops')
    
print(div(1,0))