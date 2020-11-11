# Example of using map in python

words = ["Hello", "Orange", "Paper", "Titan", "PANDA", "Bionic Borderline Bouncy Rabbit"]

def lower(word):
	return word.lower()

words = map(lower, words)

print(words)
