# Example of using optional parameters in python

def func(word, freq=1, add=5):
	print(word*(freq+add))

call = func('hello', add=3)
