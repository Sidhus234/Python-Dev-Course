# Exercise function

def highest_even(num_list):
    highest_even_num = 0
    for x in num_list:
        if ((x % 2 == 0) and (x > highest_even_num)):
            highest_even_num = x
    return highest_even_num

print(highest_even([10,2,3,4,8,11]))