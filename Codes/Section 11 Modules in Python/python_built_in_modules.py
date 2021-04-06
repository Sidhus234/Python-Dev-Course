# More details can be found here: https://docs.python.org/3/py-modindex.html

# random
import random
print(random)
help(random)

print(dir(random))

print(random.random()) # gives random number between 0 and 1
print(random.randint(0, 100)) # givsn random number between a and b
print(random.choice([1,2,3,4,5])) # Picks a random choice from given list
my_list = [1,2,3,4,5]
print(random.shuffle(my_list))
print(my_list)