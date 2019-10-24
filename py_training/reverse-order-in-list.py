# .数组中的逆序对
# 题目：在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007


test = [5, 4, 3, 2, 1]
count = 0
for i in range(len(test)):
    for j in range(1, len(test)):
        if test[i] > test[j]:
            count += 1
        else:
            continue
print(count)

# 一定会超时
