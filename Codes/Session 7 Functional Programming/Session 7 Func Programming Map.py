# map
# Map takes the function, and iterable
# then runs the function over every item in the iterable
def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3,4]))

# simplify above code
def multiply_by2up(item):
    return item*2

print(list(map(multiply_by2up, [1,2,3,4])))