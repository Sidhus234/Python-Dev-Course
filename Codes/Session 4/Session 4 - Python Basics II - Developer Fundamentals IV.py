# What is good code:
# 1. Clean: following python community endroses
# 2. Readability: read your own code, and able to understand
#       Variable name should make sense
#       Add comments to make code easier to read
# 3. Predictability: Code should be written in a manner to ensure easy to follow
# 4. DRY: Donot Repeat Yourself

picture = [
        [0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,1,1,1,1,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0]
        ]

fill = "*"
empty = " "


for item in picture:
    for val in item:
        if(val == 0):
            print(empty, end='')
        else:
            print(fill, end='')
    print()
