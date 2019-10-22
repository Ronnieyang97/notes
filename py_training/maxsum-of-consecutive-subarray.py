# 连续子数组的最大和
# {6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)

# 关键点在于正数后面跟着的负数个数
# 先找到第一个正数，如果后面仍然是在正数就相加，
# 如果是负数（一个或多个）就一直加上负数直到出现下一个正数或是和小于等于0，下一个是正数的情况就将正数和若干个负数收敛成一个新的正数
# 如果是负数就舍弃前段数据，将下一个正数作为start重复
test = [6, -3, -2, 7, -15, 10, -2, -2, -4, 7, 6]
start = 0
end = 1
result = []
lenth = len(test)
while end < lenth:
    judge = 0
    if test[end] >= 0:
        end += 1
        if end < lenth:
            continue
        else:
            result.append([start, end-1])
    elif test[end] < 0:
        if sum(test[start:end+1]) > 0:
            end += 1
            if end == lenth-1:
                while end > start:
                    if test[end] <= 0:
                        end -= 1
                    else:
                        break
                result.append([start, end+1])
                break
            continue
        elif sum(test[start:end+1]) <= 0:  # 将上一组数据储存，并开始下一组
            end1 = end
            while end1 > start:
                if test[end1] <= 0:
                    end1 -= 1
                else:
                    break
            result.append([start, end1+1])  # 从当前end回溯到[start:end]中最靠近右侧的正数位置
            for i in test[end:]:
                if i > 0:
                    start = end + test[end:].index(i)  # 得到下一个正数即start开始的位置
                    end = start + 1
                    if end < len(test):
                        judge = 1
                        break
                    else:
                        result.append([start, end-1])
            if judge == 0:
                break
            else:
                continue

print(result)
resultsum = []
for i in result:
    resultsum.append(sum(test[i[0]:i[1]]))
print(result[resultsum.index(max(resultsum))])



