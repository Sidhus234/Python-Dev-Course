# List/set/dictionary comprehensions
# can be used with all above data types

# Quick way to create list/set/dictionaries

my_list = []

for char in 'hello':
    my_list.append(char)
    
print(my_list)

# Another way to do this
# my_list = [param for param in iterable]

my_list = [char for char in 'hello']
print(my_list)
my_list2 = [num for num in range(0, 100)]
my_list3 = [num*2 for num in range(0, 100)]
#print(my_list3)

my_list4 = [num**2 for num in range(0, 100) if num%2 ==0]
print(my_list4)

# Creating a set
my_set = {char for char in 'hello'}
print(my_set)