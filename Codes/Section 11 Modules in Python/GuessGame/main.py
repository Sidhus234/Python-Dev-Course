import sys
import random

min_value = int(sys.argv[1])
max_value = int(sys.argv[2])
print(f'Please guess a number between {min_value} and {max_value}')

while(True):
    print(f"Is your number {random.randint(min_value, max_value)}?")
    user_input = input("Please enter Y for Yes and N for No")
    if(user_input.lower() == 'y'):
        print("Yay!!!!!")
        break

import game12
