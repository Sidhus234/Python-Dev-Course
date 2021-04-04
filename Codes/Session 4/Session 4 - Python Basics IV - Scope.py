# Scope: what variables do I have access to

print(name)
# error as name is not defined

# Global scope
total = 100
print(total)

def some_func():
    # here total1 is within scope of function
    total1 = 100
print(total1)

# sample
a = 1
def confusion():
    a = 5
    return a

print(a)
print(confusion())

# 1 Start with local scope
# 2 If there is nothing in local scope, then is there a parent local scope
# 3 Global: indentation of nothing is global
# 4 Built in function
def confusion():
    return a
print(a)
print(confusion())


def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(a)
print(confusion())


print(parent())
print(a)




def parent():
    def confusion():
        return a
    return confusion()

print(a)
print(confusion())


print(parent())
print(a)


def parent():
    def confusion():
        return sum
    return confusion()

print(parent())
