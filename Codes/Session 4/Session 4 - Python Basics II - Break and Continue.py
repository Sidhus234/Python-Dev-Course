my_list = [1,2,3,4]
for item in my_list:
    print(item)
    break

my_list = [1,2,3,4]
for item in my_list:
    print(item)
    continue

# break means break the loop
# continue: go to top line of loop

my_list = [1,2,3,4]
for item in my_list:
    continue
    print(item)
    
i = 0
while i< len(my_list):
    i += 1
    continue
    print(my_list[i])
    
# Pass statement: does nothing
my_list = [1,2,3,4]
for item in my_list:
    pass
    print(item)
    
i = 0
while i< len(my_list):
    print(my_list[i])
    i += 1
    pass

# Pass is good way to have placeholder while working
for item in my_list:
    # thinking about it
    pass

# placeholder for a line of code when not sure what to do