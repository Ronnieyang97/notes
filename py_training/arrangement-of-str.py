# 字符串的排列
# 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
# 例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

# 关键在于需要先排序
from itertools import permutations
test = 'cba'
test = sorted(list(test))  # 将test转换为字符数组,并排序
result = list(permutations(test))
for i in result:
    print(''.join(i))  # 将result中的字符元组（排列结果）转为字符串


