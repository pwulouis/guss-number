import random 
start = input('Give me a start number: ')
end = input('give me a end number: ')
start = int(start)
end = int(end)

r = random.randint(start,end)
count = 0
while True:
	count +=1
	num = input('please enter a number: ')
	num = int(num)
	if num == r:
		print('you r ringt','\n' + 'you guess', count, 'times')
		break
	elif num > r:
		print('biger than the number','\n' + 'please guess again:')
	elif num < r:
		print('smaller than the number','\n' + 'please guess again:')
	print('you guess', count, 'times')