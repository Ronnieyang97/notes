# capture 4
def split():  # 分割字符串
    import re

    test = "asdf fjdk; afed,   fjek,asdf, foo"
    print(re.split(r'[;,\s]\s*', test))  # [;,\s]表明不允许有(;)(,)(空格)这三种分隔符；\s*表明不允许有分隔符周围任意个空格;分隔符只能出现一次

    print(re.split(r'(;|,|\s)\s*', test))  # (;|,|\s)为捕获分组，返回的结果中会包含分隔符组合

    print(re.split(r'(?:,|;|\s)\s*', test))  # (?:,|;|\s)为非捕获分组


def match():  # 匹配字符串
    # startswith 和 endswith的参数必须为元组
    import re
    url = 'http://www.python.org'
    print(re.match("http|ftp", url))  # 返回值为<re.Match object; span=(0, 4), match='http'>
    print(re.match("abc", url))  # 没有匹配的则返回None

    from fnmatch import fnmatch, fnmatchcase
    print(fnmatch("abcd", "cd"))
    print(fnmatch("abcd", "*cd"))  # *表示任意数量的任意字符  返回true
    print(fnmatch("abcd", "?cd"))  # ?表示任意一个字符  返回false
    print(fnmatch("abc12", "abc[0-2][0-4]"))  # [a-b]可以表示a，b间的任意一个数字

    # 在windows中忽略大小写，如果要严格区分大小写则使用fnmatchcase

    test1 = "09/23/1997"
    test2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    print(re.match(r"\d+/\d+/\d", test1))  # \d表示任意个数字
    datepat = re.compile(r'\d+/\d+/\d+')  # 预编译
    print(datepat.match(test1))
    print(datepat.findall(test2))  # 查找所有符合datepat格式的字段
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)')  # 使用捕获分组
    m = datepat.match(test1)
    print(m.group(0))  # "09/23/1997"
    print(m.group(1))  # "09"
    print(m.group(2))  # "23"
    print(m.group(3))  # "1997"
    print(m.groups())  # ("09", "23", "1997")
    print('{}-{}-{}'.format(m.group(1), m.group(2), m.group(3)))
    for m in datepat.finditer(test2):  # finditer会以迭代的方式返回搜索值
        print(m.groups())
    datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')  # $为精确匹配
    print(datepat.match("09/23/1997ghjg"))  # 返回为None

    str_pat = re.compile(r'\".*\"')  # .*表示任意数量的任意字符,除换行符
    text1 = 'Computer says "nonono"'
    print(str_pat.findall(text1))
    text2 = 'computer says "nonono", phone says "yesyesyesyes"'
    str_pat1 = re.compile(r'\".*?\"')
    print(str_pat.findall(text2))  # text2中有两组“”，直接用str_pat结果会产生问题（根源在于*的贪婪形式会找到最长的引号中内容，将两个引号理解为一个长引号）
    print(str_pat1.findall(text2))  # 加了？则会转变为非贪婪模式，最短匹配模式

    text2 = 'computer says "ab\ncd\nef", phone says "abc\ndef"'
    textpat = re.compile(r'\"(?:.|\n)*?\"')  # 加入换行符使其能填补.不能匹配换行符的缺陷;带有|符号为捕获组，因此需要加?:转为非捕获组
    print(textpat.findall(text2))
    textpat2 = re.compile(r'\".*?\"', re.DOTALL)
    print(textpat2.findall(text2))  # 在预编译时加入re.DOTALL参数可以使.符号匹配任意符号（包括换行符）；不适用于复杂情况


def standard():  # 标准化unicode
    import unicodedata
    t = unicodedata.normalize('NFC', "abcdef")  # NFC表示整体组成；NFD表示拆分组成


def clean():  # 清理格式
    test = "  hello world \n "
    print(test.strip())  # 返回结果为“hello world”
    print(test.lstrip())  # 返回结果为“hello world \n ”
    print(test.rstrip())  # 返回结果为“  hello world”

    test = "hello     world"
    import re
    print(re.sub(r"\s+", " ", test))  # \s+表示多个\s符号

    test1 = 'pýtĥöñ\fis\tawesome\r\n'
    remap = {ord('\t'): ' ', ord('\f'): ' ', ord('\r'): None}  # 创建指定字符映射的字典
    test = test1.translate(remap)  # 指定字符被映射为空格
    print(test)
    import sys
    import unicodedata
    remap = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))  # 将所有和音符都映射为None
    test = unicodedata.normalize('NFD', test)  # 拆分所有组合字符
    print(test)
    test = test.translate(remap)
    print(test)
    test = unicodedata.normalize('NFD', test1)  # 拆分所有组合字符
    print(test.encode('ascii', 'ignore').decode('ascii'))  # 编码时将非ascii码直接丢弃，再重新解码为ascii


def toformat():  # 格式化
    text = "test test1"
    print(text.ljust(20))
    print(text.rjust(20, '*'))
    print(text.center(20, 's'))  # 可接受一个可填充字符，只能为一个字符！

    print(format(text, '>20'))
    print(format(text, '*<20s'))
    print(format(text, 's^20s'))  # format也能完成相同的功能,在<,>,^符号前加字符即可实现字符填充空格

    print('{:*>10s}-{:s>10s}'.format('Hello', 'World'))  # 格式化多个值，填充字符在:符号后

    print(format(3.14159, '^10.2f'))  # 格式化数字

    parts = ['Is', 'Chicago', 'Not', 'Chicago?']
    print(' '.join(parts))  # 拼接字符串
    # .join 连接的对象可以是列表，元组，字典，文件，生成器，集合等

    data = ['abc', 1, 'bcd', 2, 'cde']
    print(',,'.join(str(d) for d in data))  # 单纯拼接字符串最好使用.join和生成器，而避免使用for循环和+=，后者会进行多余的内存复制和垃圾回收

    # I/O时，尽量避免f.write(str1 + str2),如果str1和str2较大则会产生一个较大的临时结果，复制大量内存数据。

    def sample():  # 处理大量小字符串
        yield 'is'
        yield 'Chicago'
        yield 'Not'
        yield 'Chicago?'

    print('..'.join(sample()))  # 拼接
    for part in sample():  # 输出重定向
        print(part)

    s = "Look into my eyes, look into my eyes, the eyes, the eyes, " \
        "the eyes, not around the eyes, don't look around the eyes, " \
        "look into my eyes, you're under."

    import textwrap
    print(textwrap.fill(s, 70))  # 使字符串长度限定为一行七十
    print(textwrap.fill(s, 40, initial_indent='  '))  # 开头缩进;使用initial_indent=' '参数则为除第一行其他行缩进指定字符串

    s = 'Elements are written as "<tag>text</tag>".'
    import html
    print(html.escape(s))  # 处理html中的<>符号
    print(html.escape(s, quote=False))  # 返回结果相较于上一个会少一项quote


def spilt_str():
    text = 'foo = 23 + 42 * 10'
    import re
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'  # ?P<TOKENNAME>用于给一个模式命名
    NUM = r'(?P<NUM>\d+)'
    PLUS = r'(?P<PLUS>\+)'
    TIMES = r'(?P<TIMES>\*)'
    EQ = r'(?P<EQ>=)'
    WS = r'(?P<WS>\s+)'
    master_pat = re.compile('j'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

    scanner = master_pat.scanner('foo = 23 + 42 * 10')
    first = scanner.match
    for m in iter(scanner.match, None):
        print(m.lastgroup, m.groups)




def replace_str():  # 替换
    test = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
    import re
    re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', test)  # \1,\2,\3为match后group（1， 2， 3）中的内容
    print(test)  # 结果为'Today is 2012-11-27. PyCon starts 2013-3-13.'
    datepad = re.compile(r'(\d+)/(\d+)/(\d+)')
    datepad.sub(r'\3-\1-\2', test)

    s = '{name} has {n} messages.'
    print(s.format(name="ronnie", n=10))  # 直接拼接
    name = "ronnieyang"
    n = 20
    print(s.format_map(vars()))  # 通过format_map和vars()完成拼接

    import string
    s = string.Template('$name has $n messages.')  # 使用string.Template初始化
    print(s.substitute(vars()))  # 使用substitute(vars())拼接

    # vars可用于对象实例
    class Info:
        def __init__(self, name, n):
            self.name = name
            self.n = n

    a = Info('yyh', 30)
    print(s.format_map(vars(a)))

    class safemode(dict):
        def __missing__(self, key):  # 防止找不到应有参数
            return '{' + key + '}'

    del n  # 确保n未定义
    print(s.format_map(safemode(vars())))


def ignore():  # 忽略大小写
    import re
    # 将flag参数设置为re.IGNORECASE


spilt_str()