# Debugging: programs are full of bugs. Act of finding and removing bugs is 
# called debugging
# With time, one gets good at debugging. Keep writing more and more code

# Use linting
# Always use IDE/Editor like Pycharm / Visual Studio

# Learn to read errors
4 +' dvjdg' # trying to add int and string

4 + 'gkfdjgj # end of line error no '

# There are 15-20 errors which are more common

# Python Debugger
# https://docs.python.org/3/library/pdb.html

def add(num1, num2):
    print(num1, num2)
    return num1 + num2

add(4, 'dsdafj')

import pdb
def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

add(4, 'dsdafj')
 # allows interacting with program while running
 # 
