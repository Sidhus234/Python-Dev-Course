# Set: unordered collection of unique things

my_set = {1,2,3,4,5,1,1,4}
my_set
my_set.add(100)
my_set.add(2)
my_set


# set is in one location in memory
my_list = [1,2,3,4,5,5,6]
my_list = list(set(my_list))
my_list
# set can be used to remove duplicates easily

# set object doesn't support indexing
1 in my_set
len(my_set)
abc_set = my_set.copy()

my_set.clear()

abc_set

# Methods in set: https://www.w3schools.com/python/python_ref_set.asp

my_set = {1,2,3,4,5,6}
your_set = {4,5,7,8,9,10}
# calculates the difference between two or more sets
abc = my_set.difference(your_set)
print(abc)

# discards the given element
my_set.discard(5)
my_set


my_set.difference_update(your_set)
my_set

my_set
# intersection
my_set.intersection(your_set)
my_set


my_set.isdisjoint(your_set)

my_set.union(your_set)
my_set


my_set.issubset(your_set)


my_set.issuperset(your_set)
