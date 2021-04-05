while(True):
    try:
        age = int(input('what is your age?'))
        10/(age)
        raise ValueError('hey cut it out')
    except ZeroDivisionError:
        print("Please enter age higher than 0")
        break
    else:
        print('Thank you')
        break
    finally:
        print('ok, I am finally done')
    print('can you hear me?')
