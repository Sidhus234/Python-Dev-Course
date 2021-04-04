picture = [
	[0,0,0,1,0,0,0],
	[0,0,1,1,1,0,0],
	[0,1,1,1,1,1,0],
	[1,1,1,1,1,1,1],
	[0,0,0,1,0,0,0],
	[0,0,0,1,0,0,0]
	]

for row in picture:
	for val in row:
		if(val):
			print('*', end="")
		else:
			print(' ', end="")
	print('')
