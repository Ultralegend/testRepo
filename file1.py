import math

def getFact(x):
    if x == 0:
        return 1
    else:
        return x * getFact(x - 1)

def isOdd(x):
    return x % 2 != 0

def isEven(x):
    return not isOdd(x)

def arrayToInt(array): return [int(i) for i in array]

print(getFact(5))
print(isOdd(6))
print(isEven(6))

