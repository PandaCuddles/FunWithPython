# Example of annotations in python

VAR1 : int
VAR2 : str
VAR3 : list

print(__annotations__)

def func() -> int:
  return 1

print(func.__annotations__)
