import math

def getFact(x):
    if x == 0:
        return 1
    else:
        return x * getFact(x - 1)

print(getFact(5))