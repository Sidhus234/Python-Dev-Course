# while loop: 
# while a condition is true, keep working

i = 0
while(i<50):
    print(i)
    i+=1
# really important to ensure that loop end condition is used

# break: keyword to end any loop

i = 0
while(i<50):
    print(i)
    break
else:
    print("Done with all the work")

# else block will only execute if there is no break statement
i = 0
while(i<50):
    print(i)
    i+=1
else:
    print("Done with all the work")

# Else statement can be used to see if the while loop ran till the end
# While loop is used when we are not sure of how many times we want to run


while True:
    input('say something: ')
    break


while True:
    response = input('say something: ')
    if(response == 'bye'):
        break