import sys

words = sys.argv[1:]
for i, word in enumerate(words):
	print('Argv of ' + str(i) + ' is ' + word)
words.sort(key=len, reverse=True)
for word in words:
	print(word)
