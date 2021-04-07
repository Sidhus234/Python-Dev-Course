import os
os.chdir('C:/Users/sidhu/OneDrive/Desktop')

# using with open, we don't have to close the file
with open('test.txt', mode='r') as my_file:
    print(my_file.readlines())
    
with open('test.txt', mode='r+') as my_file:
    text = my_file.write("Hey its me")
    print(text)
    
with open('test.txt', mode='r+') as my_file:
    text = my_file.write(";)")
    print(text)
    
# When we write, the cursor goes to zero and over writes everything
# To write to end of file use, append mode
with open('test.txt', mode='a') as my_file:
    text = my_file.write(";)")
    print(text)


with open('test.txt', mode='r') as my_file:
    print(my_file.readlines())