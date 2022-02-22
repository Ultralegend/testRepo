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

def arrayToInt(array):
    nArray = []

    for i in array: nArray.append(int(i))

    return nArray

print(getFact(5))
print(isOdd(6))
print(isEven(6))

tArray = ["1", "2", "3"]
print(tArray)
print(arrayToInt(tArray))