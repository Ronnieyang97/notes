# 斐波那契数列  递归过于简单  迭代实现

def feb(num):
    if num == 1:
        return [1]
    elif num == 2:
        return [1, 1]
    elif num >= 3:
        result = [1, 1]
        while num > 2:
            result.append(result[-1] + result[-2])
            num -= 1
        return result
    else:
        return 0


print(feb(7))
