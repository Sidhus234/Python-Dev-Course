# Decorators
# some are in classes
# @classmethod and @staticmethod

from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f'It took {end_time - start_time} s')
        return result
    return wrapper



@performance
def long_time():
    for i in range(100000000):
        i*5

long_time()