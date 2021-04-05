# Error Handling

age = input('What is your age?')
print(age)

# A user can still input non integar number

while(True):
    try:
        age = int(input('what is your age?'))
        print(age)
    except:
        print("Please enter a number")
    else:
        print('Thank you')
        break
    
while(True):
    try:
        age = int(input('what is your age?'))
        10/(age)
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    else:
        print('Thank you')
        break
    
# except > except > else run in order