from numpy import array, argwhere, vstack

# argwhere直接返回矩阵中所有符合目标的值

test = array([['a', 'b', 'c', 'e'],
              ['s', 'f', 'c', 's'],
              ['a', 'd', 'e', 'e']])
path = []
target = 'bccec'
cursor = 0


def getall(target):
    maybe = []
    for i in target:
        if argwhere(test == i).size > 0:
            maybe.append(argwhere(test == i))
        else:
            return 0
    # maybe中的每一项都是字符的可能位置
    path = []
    for i in range(0, len(maybe) - 1):
        temp = []
        for x in maybe[i]:
            for y in maybe[i + 1]:
                if check(x, y):
                    temp.append([x, y])
        path.append(temp)
    while len(path) > 1:
        temp = []
        for x in path[0]:
            for y in path[1]:
                if splice(x, y):
                    temp.append(vstack((x, y[-1])))
        path[0] = temp
        del path[1]
    if path[0]:
        return 1
    else:
        return 0


def check(a, b):  # a,b为单个数组对
    if (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 == 1:
        return 1
    else:
        return 0


def splice(a, b):
    if a[-1][0] == b[0][0] and a[-1][1] == b[0][1] and not (a[-2][0] == b[-1][0] or a[-2][1] == b[-1][0]):
        return 1
    else:
        return 0


print(getall(target))
