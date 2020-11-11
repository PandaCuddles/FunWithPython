# Example of using map in python

words = ["Hello", "Orange", "Paper", "Titan", "PANDA", "Bionic Borderline Bouncy Rabbit"]

def upper(word):
	return word.lower()

words = map(upper, words)

print(words)
