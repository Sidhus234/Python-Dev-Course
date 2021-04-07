# How to read files in other directories

# Give relative path (to code files)
# or give absolute path
# ./ means from current folder
# .. means go one directory back


# pathlib is a new library , and it works with both (windows, and unix)

try:
    with open('test.txt', mode = 'r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print("File not found")
    raise err
except IOError as err:
    print('Having issue reading the file')
    raise err