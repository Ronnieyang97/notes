# 检查输入的项是否为顺子


def check(given):
    given = sorted(given)
    num0 = given.count(0)
    for i in range(given.count(0), 4):
        if given[i+1] - given[i] == 1:
            continue
        else:
            if num0 > 0:
                given[i] += 1
                num0 -= 1
            else:
                return False
    return True


print(check([0, 2, 6, 4, 5]))


