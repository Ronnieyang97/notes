test = 'test str'
print(test.encode('utf_8'))  # 编码

test = bytes('test', encoding='utf_8')
print(test[:2])

# memoryview 用于访问其他二进制序列、打包的数组和缓冲中的数据切片，是共享内存而非复制字节序列

# chardet库可以用于检测字节序列的编码

# 不能依赖默认编码
