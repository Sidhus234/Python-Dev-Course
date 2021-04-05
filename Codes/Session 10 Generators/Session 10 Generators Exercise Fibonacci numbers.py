# Return all the numbers till num to the function


def fib(num):
    last = 0
    current = 1
    for i in range(num):
        if (i <= 1):
            yield i
        else:
            yield (last + current)
            last = current
            current += last

fib_20 = fib(10000)
for i in fib_20:
    print(i)

