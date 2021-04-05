# Most libraries in python use 'Generators' to optimize performance
from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'It took {end_time - start_time} s')
        return result
    return wrapper


# This one use generators (and is more efficient)
@performance
def long_time():
    print('1')
    for i in range(1000000000):
        i*5

# This uses memory and hence is slow (As it stores list in memory)
@performance
def long_time2():
    print('2')
    for i in list(range(1000000000)):
        i*5

long_time()

long_time2()