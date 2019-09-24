def opentxt():
    # rt读取
    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\test1.txt', 'rt') as f:
        for line in f:
            print(line)
    f.close()

    # wt清楚原有文件并覆盖
    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\test2.txt', 'wt') as f:
        f.write("this is a second file")  # 原文件中为乱码
        f.write("this is the second line")

    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\test2.txt', 'rt') as f:
        for line in f:
            print(line)

    # 使用print重写数据
    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\test2.txt', 'wt') as f:
        print("using print to cover the old txt file", file=f)

    # 二进制读写
    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\testbin.txt', 'wb') as f:
        f.write(b'Hello World')
    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\testbin.txt', 'rb') as f:
        data = f.read()
        print(data)

    a = "hello world"
    b = b"hello world"
    for x in a:
        print(x)  # 显示的是字符
    for x in b:
        print(x)  # 显示的是ascii码

    # 二进制转码
    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\testbin.txt', 'rb') as f:
        data = f.read()
        text = data.decode('utf-8')  # 解码
        print(text)

    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\testbin.txt', 'wb') as f:
        text = 'encoding............'
        f.write(text.encode('utf-8'))

    # 将数组作为二进制数据写入（这种对象会直接暴露其底层的内存缓冲区给能处理它的操作。）
    import array
    test = array.array('i', [1, 2, 3, 4])
    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\array.txt', 'wb') as f:
        f.write(test)

    out = array.array('i', [0, 0, 0, 0, 0, 0])
    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\array.txt', 'rb') as f:
        f.readinto(out)
    print(out)


def format_print():
    print('ACME', 50, 91.5, sep=',', end='!!\n')  # 简单格式化输出，sep为间隔，end为结尾
    print('*'.join('test', 222, 6.23))
    test = ('test1', 232, 89.3)
    print('@'.join(str(x) for x in test))
    print(*test, sep='#')


def teststr():
    import io
    s = io.StringIO()
    s.write('Hello World\n')
    print('This is a test', file=s)
    print(s.getvalue())

    s = io.StringIO('Hello,World\n')
    print(s.read(4))
    print(s.read())

    # 模拟一个普通的文件的时候StringIO 和BytesIO 类是很有用的。在单元测试中，你可以使用StringIO 来创建一个包含测试数据的类文件对象，这个对象
    # 可以被传给某个参数为普通文件对象的函数。
    # 需要注意的是， StringIO 和BytesIO 实例并没有正确的整数类型的文件描述符。
    # 因此，它们不能在那些需要使用真实的系统级文件如文件，管道或者是套接字的程序中使用。




teststr()
