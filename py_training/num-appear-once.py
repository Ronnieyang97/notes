# 数组中只出现一次的数字
# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
test = [2, 2, 6, 4, 8, 8, 6]

result = 0
for i in test:
    result = result ^ i  # 使用^异或运算符时不需要将数字转为BIN
print(result)
