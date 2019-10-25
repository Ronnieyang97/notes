# 翻转单词顺序
# “student. a am I”正确的句子应该是“I am a student.”

test = 'student. a am I'
x = test.split()
x.reverse()
print(' '.join(x))
