# Tuples are immutable lists

my_tuple = (1,2,3,4,5)
my_tuple[1] = 'z'

my_tuple[1]
my_tuple[4]

5 in my_tuple

# tuples can't be changed
# tuples are faster than list

# Tuple methods: https://www.w3schools.com/python/python_ref_tuple.asp

new_tuple = my_tuple[1:3]
new_tuple

new_tuple = my_tuple[1:2]
new_tuple


x,y,z, *other = (1,2,3,4,5)
other

my_tuple.count(5)

my_tuple.index(5)

len(my_tuple)
