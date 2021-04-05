# Generators allows us to generate sequence of values over time
# for example: range


def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)

# This my_list lives in memory (and takes up physical space)

# range is a generator, and doesn't live in memory and only provides 
# one number at time

my_list = make_list(100000)
print(my_list)
# above example takes too much space and time
# Hence it is better to use Generators
