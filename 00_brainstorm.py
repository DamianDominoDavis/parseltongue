from random import choice
import time

categories = ['Animals', 'Food', 'Brands', 'Jobs', 'tv shows', 'movies']
width = 80

question = choice(categories)
answers = [0]*10
start = time.time()
for i in range(10):
	answers[i] = raw_input(question + ': ')
	#answers[i] = input(question + ': ')
print(' ' + '*' * (width + 2))
for answer in answers:
	print '*',
	print answer.center(width),
	print '*'
	#print('*', end='')
	#print(answer.center(width), end='')
	#print('*')
print(' ' + '*' * (width + 2))
end = time.time()
print(str(end - start))
