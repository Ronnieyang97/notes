# 跳台阶
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。

from itertools import permutations


def jump(num):
    # int(num/2)为一级台阶与两级台阶的组合方式
    if not isinstance(num, int):
        return 0
    if num % 2 == 0:
        prob = []
        for i in range(int(num / 2)+1):
            com = []
            for x in range(i):
                com.append(2)
            for y in range(num - 2*i):
                com.append(1)
            prob.append(com)
    result = 0
    for com in prob:
        temp = set()
        for maybe in permutations(com):  # 可能出现重复排列的情况，因此用集合
            temp.add(maybe)
        result += len(temp)

    print(result)

jump(4)
