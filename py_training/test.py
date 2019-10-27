from numpy import array, argwhere

test = array([['a', 'b', 'c', 'e'],
              ['s', 'f', 'c', 's'],
              ['a', 'd', 'e', 'e']])


def getall(target):
    maybe = []
    for i in target:
        if argwhere(test == i).size > 0:
            maybe.append(argwhere(test == i))
        else:
            return 0
    return maybe

def check(a, b):  # a,b为单个数组对
    if (a[0] - b[0])**2 + (a[1] - b[1])**2 == 1:
        return 1
    else:
        return 0


x = getall('bcced')

print(check(x[1][0], x[1][1]))


