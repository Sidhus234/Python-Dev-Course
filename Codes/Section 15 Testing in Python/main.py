# Debugging costs lot of money
# Testing: individual units of code are tested

def do_stuff(num = 0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'please enter number'
    except ValueError as err:
        return err
