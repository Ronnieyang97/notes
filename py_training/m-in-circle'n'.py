# 在一个长度为m的数组中，去除掉第n个数字（如果n>m，则从头继续数）反复执行此操作直到数组中只剩下一个数字请找出这个数字


def rol(li, n):
    while n > len(li):
        n -= len(li)
    return li[n:] + li[:n]


def getnum(li, n):
    while len(li) > 1:
        li = rol(li, n)
        li.pop()
    print(li)


test = [0, 1, 2, 3, 4]
n = 3

getnum(test, n)
