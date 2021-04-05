my_set = {char for char in 'hello'}
print(my_set)
my_set2 = {num for num in range(0, 100)}
my_set3 = {num*2 for num in range(0, 100)}
#print(my_set3)

my_set4 = {num**2 for num in range(0, 100) if num%2 ==0}
print(my_set4)

# Dictionary Comprehensions
simple_dict = {
        'a':1,
        'b':2
        }
my_dict = {key:value**2 for key,value in simple_dict.items()}
print(my_dict)

my_dict = {key:value**2 for key,value in simple_dict.items() if value%2}
print(my_dict)

my_dict1 = {num:num*2 for num in [1,2,3]}
print(my_dict1)