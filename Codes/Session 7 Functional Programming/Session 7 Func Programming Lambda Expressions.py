# Lambda functions are for those occasions: only used once
# Hence don't need to name them as they are not used

# lambda param: action(param)
from functools import reduce
my_list = [1,2,3]

def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, my_list)))

print(list(map(lambda item: item*2, my_list)))

print(my_list)

# Lambda: are one time aynmous functions that are used only once
# Once used they are not stored in memory and are discarded

print(list(filter(lambda item: item%2, my_list)))

print((reduce(lambda item, acc: item+acc, my_list, 0)))
