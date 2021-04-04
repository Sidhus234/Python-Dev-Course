total = 0

def count():
    total += 1
    return total

print(count())
# Function can't use global variable without explictly stating it

def count():
    total = 0
    total += 1
    return total

print(count())
print(count())
print(count())

def count():
    global total
    total += 1
    return total

print(count())
print(count())
print(count())

print(total)
# not a good way (As shown above) .. it is confusing

