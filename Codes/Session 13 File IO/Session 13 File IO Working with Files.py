# I/O means to interact with something from outside world, 
# and write to outside world

import os
os.chdir('C:/Users/sidhu/OneDrive/Desktop')

myfile = open('test.txt')
print(myfile.read())
myfile.seek(0) # take cursor back to line 0
print(myfile.read())
myfile.seek(0) # take cursor back to line 0
print(myfile.read())

##################################3
# Read line by line
myfile = open('test.txt')
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())


# read all lines in a list
myfile = open('test.txt')
print(myfile.readlines())

myfile = open('test.txt')
abc = myfile.readlines()

# Important to close the file
myfile.close()
