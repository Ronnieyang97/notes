# 第一个只出现一次的字符位置
# 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置

test = [1, 2, 3, 45, 1, 2, 3, 8, 3, 2]
for i in test:
    if test.count(i) == 1:
        print(test.index(i))
        break
    else:
        continue

