# Password checker
# atleast 8 characters long
# contain any sort of letters, numbers, and these symbols $%#@

import re

while(True):
    password = input("Enter string to test: ")
    if re.fullmatch(r'[A-Za-z0-9@#$%]{8,}', password):
        print('correct')
        break
    else:
        print('please try again')
        
# To ensure last digit is a number
while(True):
    password = input("Enter string to test: ")
    if re.fullmatch(r'[A-Za-z0-9$%#@]{7,}[0-9]', password):
        print('correct')
        break
    else:
        print('please try again')