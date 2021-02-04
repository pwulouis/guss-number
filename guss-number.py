import random 
r = random.randint(1,100)
count = 0
while True:
	count +=1
	n = input('please enter a number: ')
	n = int(n)
	if n == r:
		print('you r ringt','\n' + 'you guss', count, 'times')
		break
	elif n > r:
		print('biger than the number','\n' + 'please guss again:')
	elif n < r:
		print('smaller than the number','\n' + 'please guss again:')
	print('you guss', count, 'times')