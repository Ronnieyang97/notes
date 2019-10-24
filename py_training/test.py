from time import time

def get(index):
    # write code here
    if index < 1:
        return 0
    res = [1]
    t2 = t3 = t5 = 0

    nextdex = 1
    while nextdex < index:
        minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
        res.append(minNum)
        while res[t2] * 2 <= minNum:
            t2 += 1
        while res[t3] * 3 <= minNum:
            t3 += 1
        while res[t5] * 5 <= minNum:
            t5 += 1

        nextdex += 1

    print(res[nextdex - 1])


a = set()
a.add(2)
a.add(6)
a.add(4)
print(a)
