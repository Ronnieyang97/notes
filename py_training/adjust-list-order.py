# 调整数组顺序使奇数位于偶数前面
# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，奇数在前，偶数在后,并保证奇数和奇数，偶数和偶数之间的相对位置不变。


def change(list1):
    lenth = len(list1)
    i = 0
    while i < lenth:
        if list1[i] % 2 == 0:
            x = list1[i]
            list1.remove(list1[i])
            list1.append(x)
            lenth -= 1
            i += 1
        else:
            i += 1

    return list1


print(change([1, 2, 3, 4, 5]))
