# An interesting look as python metaclass awesomeness

def __add__(self, x):
	return x + x

Test = type('Test', (), {"__add__":__add__})
t = Test()

print(t + 4)
