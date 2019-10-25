# 和为s的两个数字
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的

test = [2, 3, 5, 7, 8, 13, 17, 18, 20]
start = 0
end = len(test) - 1
target = 25
while start < end:
    if test[start] + test[end] > target:
        end -= 1
    elif test[start] + test[end] < target:
        start += 1
    else:
        print(test[start], test[end])
        break
