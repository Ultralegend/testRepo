import math

def getFact(x):
    if x == 0:
        return 1
    else:
        return x * getFact(x - 1)

def isOdd(x):
    return x % 2 != 0

print(getFact(5))
print(isOdd(6))