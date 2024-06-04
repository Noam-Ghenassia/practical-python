from functools import reduce

a = ["vb", "ac", "q"]
b = reduce(lambda a, b: a+b, a)
print(b)