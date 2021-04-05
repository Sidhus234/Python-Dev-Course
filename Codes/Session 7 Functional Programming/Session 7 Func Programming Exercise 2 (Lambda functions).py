# Create lambda function to square the list
# input: my_list = [5,4,3]
# output: print - [25, 16, 9]

# Challenge 2: list sorting
# input a = [(0,2), (4,3), (9,9), (10,-1)]
# sort based on second value of tuple
# output [(10, -1), (0,2), (4,3), (9,9)]

my_list = [5, 4, 3]
print(list(map(lambda item: item**2, my_list)))

a = [(0,2), (4,3), (9,9), (10,-1)]
a.sort()
print(a)

a.sort(key = lambda x: x[1])
print(a)