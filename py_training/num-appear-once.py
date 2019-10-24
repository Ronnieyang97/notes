test = [2, 2, 6, 4, 8, 8, 6]

result = 0
for i in test:
    result = result ^ i  # 使用^异或运算符时不需要将数字转为BIN
print(result)
