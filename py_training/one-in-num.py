# 整数中1出现的次数（从1到n整数中1出现的次数）


def checkone(num):  # 较为简单的处理方法，将所有字符串遍历转为str然后计算1出现的次数，但是复杂度太高
    times = 0
    for i in range(num + 1):
        times += str(i).count('1')
    print(times)




checkone(113)
