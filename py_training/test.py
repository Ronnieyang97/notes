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

        # 前进的步伐还是很小的，没一个数都考虑到了
        while res[t2] * 2 <= minNum:
            t2 += 1
        while res[t3] * 3 <= minNum:
            t3 += 1
        while res[t5] * 5 <= minNum:
            t5 += 1

        nextdex += 1

    print(res[nextdex - 1])


start = time()
get(999999)
end = time()

print(end-start)
