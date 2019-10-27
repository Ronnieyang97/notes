# .滑动窗口的最大值
#
# 题目：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
# 那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}


def maxinsilde(li, width):
    result = []
    while len(li) >= width:
        result.append(max(li[:width]))
        del li[0]
    return result


test = [2, 3, 4, 2, 6, 2, 5, 1]
print(maxinsilde(test, 3))
