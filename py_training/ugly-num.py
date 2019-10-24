# 丑数
# 把只包含因子2、3和5的数称作丑数，6，8是，14不是，习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数
# 只要某个数不能包含其他素数为其因数


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
