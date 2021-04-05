# filter
# it filter things for us

def only_odd(item):
    return bool(item%2)

print(list(filter(only_odd, [1,2,3,4,5,6])))