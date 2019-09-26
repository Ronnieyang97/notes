def parameter():  # 自定义函数中参数相关
    # 位置参数：就是在给函数传参数时，按照顺序，依次传值
    # 位置参数在前，默认参数在后
    # 关键字参数：允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。在调用函数时，可以只传入必选参数
    def avg(first, *rest):  # *rest接受任意数量的位置参数,这些参数将放在一个元组中储存
        print(first / sum(rest))
        print(type(rest))
    avg(1, 2, 3, 4)

    def element(name, age, **other):  # **other接受任意数量的关键字参数,储存形式为字典
        print(name, age)
        print(other)
    element("ronnie", "22", weight=60, height=168)

    def recv(maxsize, *, block):  # block为强制关键字，放在*或带有*的参数后面，可以设置为强制关键字
        pass
    # recv(1024, True)  # TypeError
    recv(1024, block=True)  # success






parameter()
