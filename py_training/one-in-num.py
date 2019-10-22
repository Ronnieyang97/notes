# 整数中1出现的次数（从1到n整数中1出现的次数）


def checkone(num):  # 较为简单的处理方法，将所有字符串遍历转为str然后计算1出现的次数，但是复杂度太高
    times = 0
    for i in range(num + 1):
        times += str(i).count('1')
    print(times)


def checkone_by_bit(num):  # 按照最后终止的num的各个位数的数字来判断1的个数
    num = str(num)
    lenth = len(num)
    pass

checkone(222)
