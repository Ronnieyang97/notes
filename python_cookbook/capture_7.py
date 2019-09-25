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


def road():
    import os
    path = 'C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\test1.txt'
    dirpath = 'C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\'
    print(os.path.basename(path))  # 获取文件名
    print(os.path.dirname(path))  # 获取路径名字
    print(os.path.join("temp", "data", os.path.basename(path)))  # 添加路径名
    print(os.path.exists('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7'))  # 测试路径是否存在
    print(os.path.isfile(path))  # 测试文件是否存在
    # os.path.isdir() 是否为目录
    # os.path.islink() 是否为符号链接
    # os.path.getsize() 获取文件大小
    # time.ctime(os.path.getmtime('/etc/passwd')) 获取文件修改日期

    print(os.listdir(dirpath))  # 获取路径下属子文件

    import glob
    print(glob.glob(dirpath + '/*.py'))  # 匹配文件名

    import fnmatch
    print([name for name in os.listdir(dirpath) if fnmatch.fnmatch(name, '*.py')])  # 匹配文件名


def tempfile():  # 创建临时文件和目录
    from tempfile import TemporaryDirectory, TemporaryFile
    with TemporaryFile('w+t', delete=False) as f:  # 读写,将delete设置为false则文件关闭时不会自动删除
        f.write('Hello World\n')
        f.write('Testing\n')
        f.seek(0)  # 将指针指回文件开始处
        data = f.read()
        print(data)

    with TemporaryDirectory() as dirname:
        print('dirname is:', dirname)


def communication():  # 串口通信
    import serial  # 通过pip install pySerial安装
    ser = serial.Serial('/dev/tty.usbmodem641',  # 设备样例
                        baudrate=9600,
                        bytesize=8,
                        parity='N',
                        stopbits=1)
    # 时刻记住所有涉及到串口的I/O 都是二进制模式的。因此，确保你的代码使用的是字节而不是文本(或有时候执行文本的编码/解码操作)


def serialization():  # 序列化python对象成为一个字节流，便于保存到文件或数据库或通过网络传输它
    import pickle
    data = ['test', 'test1', '1234', '34.789', ('tuple1', 'tuple2'), {"dict": 110, "dict2": 12.12}]
    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\io.txt', 'wb') as f:
        pickle.dump(data, f)
    print(pickle.dumps(data))  # 将data存储为字符串,即以二进制格式存入文本中的内容

    with open('C:\\Users\\Ronnie Yang\\PycharmProjects\\notes\\python_cookbook\\capture_7\\io.txt', 'rb') as f:
        print(pickle.load(f))



serialization()
