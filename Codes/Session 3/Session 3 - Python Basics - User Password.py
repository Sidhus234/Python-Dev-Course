user_name = input("Please enter your username")
user_password = input("Please enter your password")

star_password = '*' * len(user_password)

print(f'{user_name}, your password, {star_password}, is {len(user_password)} characters long')
