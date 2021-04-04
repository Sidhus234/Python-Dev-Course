# Exercise
picture = [
        [0,0,0,1,0,0,0],
        [0,0,1,1,1,0,0],
        [0,1,1,1,1,1,0],
        [1,1,1,1,1,1,1],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0]
        ]

# Loop through list of list and and everytime encounter zero, display empty space on screen
# replace 1 as * and 0 as <<space>>
for item in picture:
    outp = []
    for val in item:
        if(val==0):
            outp.append(" ")
        else:
            outp.append("*")            
    print("".join(str(x) for x in outp))


for item in picture:
    for val in item:
        if(val == 0):
            print(' ', end='')
        else:
            print('*', end='')
    print()