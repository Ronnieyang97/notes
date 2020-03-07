from inspect import signature
from operator import itemgetter
from functools import partial

# 归约函数
test = [1, 2, 0, 1, 1, 1]
print(all(test))  # 当可迭代对象内全部为真值，返回true
print(any(test))  # 当对象有一个为真值返回true

# 匿名函数只适合作为参数传给高阶函数
# lambda创造的是函数对象
fruit = ['banana', 'apple', 'pineapple', 'cherry', 'strawberry']
print(sorted(fruit, key=lambda fruit: fruit[1:]))  # 以字符串的第二个字符为标准排序


def tag(name, *content, cls=None, **attrs):
    print('name', name, type(name))
    print('content', content, type(content))
    print('cls', cls, type(cls))
    print('attrs', attrs, type(attrs))


tag('yyh', 'yyh play', 'yyh sleep', 10, 100, cls='test', dis='i donnot know')

# name传入了一个参数，*content接受了任意个参数，并将他们储存为元组的形式，cls接受一个指定关键字的参数
# **attrs接受任意个指定关键字名字的参数，并将它们以字典的形式储存

sig = signature(tag)
print(str(sig))  # 可以查阅该函数所需要的参数
my_tag = {'name': 'ronnie', 'cls': 'number', 'title': 'ohmy', 'src': 'tag.jpg'}
bound_args = signature(tag).bind(**my_tag)  # 当不加**符号，函数会将my_tag看作一个整体传参给name
for name, value in bound_args.arguments.items():
    print(name, '|', value)
new_tag = partial(tag, 'img', 'many many photos!!', cls='picture')
new_tag('test')  # 使用partial冻结了name和cls参数，默认输入content为'many many photos',
# 当new_tag函数任然获取到对content的输入时， 会将新的字符串'test'加到content元组中


def clip(text, max_len: 'int > 0' = 80) -> str:  # 'int>0'和'->str'均为注解表达式，表示max_len要大于0，以及返回值为str
    pass


data = [('tokyo', 'jp', 2000), ('shanghai', 'cn', 20000), ('london', 'uk', 4000), ('new york', 'us', 4000)]
print(sorted(data, key=itemgetter(0)))  # 按照第三个参数升序
print(sorted(data, key=itemgetter(2), reverse=True))  # 按照第一个参数降序
# 上述两次sorted的组合使用达成了优先按照第三个参数降序，第一个参数升序的排序方式
