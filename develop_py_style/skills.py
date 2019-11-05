from collections import namedtuple
import operator
import collections
import pandas as pd


season = namedtuple('seasons', ['spring', 'summer', 'autumn', 'winter'])._make(range(4))
print(season.spring)


# seasons的作用在于使用nametuple时会先自动构建一个seasons类，在执行赋值操作时该seasons类被命名为season，相当于中间变量的作用
# ----------------------------------------------------------------------------------

class Userint(int):
    def __init__(self):
        pass


print(isinstance(Userint, int))

# 可以看到虽然Userint继承自int但是他的类型判断并不为int
# ------------------------------------------------------------------

print(eval("__import__('os').system('dir')"))
# eval的本意是用来对输入的参数执行数学运算或字符串拼接，但是在输入特定的，如以上的参数会使eval执行不安全的操作
# 因此必须使用ast.literal_eval代替
# --------------------------------------------------------------------
test = ['a', 'b', 'c', 'd', 'e', 'f']
for x, y in zip(range(len(test)), test):
    print(x, y)
for x, y in enumerate(test):
    print(x, y)
# 上例中zip()和enumerate()的效果相同，如单纯只为获取索引值，则使用enumerate更简易和清晰，不适用于字典循环
# ————————————————————————————————————————————————————————————————————
i = 0
while i < 5:
    i += 2
    if i == 4:
        break
else:
    print(i)


# 当循环是由while后的条件触发终止则执行else语句，如果是由break触发的终止，则不执行else（try中的else用法相似）
# ————————————————————————————————————————————————————————————
# 在使用多个except捕获异常时要注意不同异常的从属关系
# 当try中的异常并未出现在except中时，会暂时将异常保存，如果后续代码中出现break或return则会导致该异常丢失的情况
# ————————————————————————————————————————————————————————————
class Student:
    def __init__(self, name, course=[]):
        self.name = name
        self.course = course

    def addcourse(self, course):
        self.course.append(course)

    def printcourse(self):
        print(self.course)


a = Student('ronnie')
a.addcourse('math')
a.addcourse('chinese')
b = Student('may')
b.addcourse('english')
a.printcourse()
b.printcourse()
# 此时a和b的结果会都是['math', 'chinese', 'english']，实例化时默认参数course只会评估一次，因此在a和b的实例化中，course的地址为同一个
# --------------------------------------------------------------------------------------------------------------------
test1 = ['a', 'b', 'c']
test2 = test1  # test1和test2的地址其实是相同的
test3 = test2[:]  # test3相当于test2的浅拷贝，地址与test2不同，因此test2的变化与test3无关
test2.append('d')
# str的相关操作与list不同，不会相互影响
# ————————————————————————————————————————————————————————————————————————
a = [str(i) if i > 3 else i * i for i in range(5) if i % 2 == 0]
# 上式相当于
a = []
for i in range(5):
    if i % 2 == 0:
        if i > 3:
            a.append(str(i))
        else:
            a.append(i * i)
# 多重迭代
test = [(a, b) for a in ['a', 5, '8'] for b in ['f', '5', '8'] if a != b]
print(test)  # 多重迭代会对a,b所在的列表求笛卡尔积，并根据条件筛选


# ————————————————————————————————————————————————
class Fruit:
    total = 0

    def __init__(self):
        self.price = 0

    @classmethod
    def print_tatal(cls):
        print(cls.total)
        print(id(Fruit.total))
        print(id(cls.total))

    @classmethod
    def set_total(cls, value):
        cls.total = value

    def set_price(self, value):
        self.price = value


class Orange(Fruit):
    pass


org1 = Orange()
org2 = Orange()
org1.set_total(300)
org1.set_price(10)
org2.set_total(600)
org2.set_price(20)
org1.print_tatal()  # 可以看到org1 和 org2 所用的total其实是同一个地址
print(org1.price, org2.price)  # 此时org1和org2的price互不影响
# ——————————————————————————————————————————————
# sort一般用于列表，sorted可用范围更广,sorted会返回一个新生成的列表，而sort直接在原列表中排序
persons = [{'name': 'ronnie', 'age': 22}, {'name': 'may', 'age': 20},
           {'name': 'yyh', 'age': 18}, {'name': 'yyh', 'age': 3}]
grades = [['ronnie', 'a', 93], ['may', 'a', 98], ['yyh', 'b', 80], ['cc', 'a', 93]]
mydict = [{'chun': ['c', 4]}, {'jiang': ['j', 5]}, {'yang': ['y', 4]}, {'yyh': ['y', 3]}]
x = sorted(persons, key=lambda x: (x['name'], -x['age']))  # 表示名字升序，年龄降序排列, x代表的是迭代的每一个字典
print(x)
y = sorted(grades, key=operator.itemgetter(1, 2, 0))  # 按照等第，分数，名字的顺序升序  使用opertateor.intemgetter默认升序
print(y)
y = sorted(grades, key=lambda x: (x[1], -x[2], x[0]))  # 等第升序，分数降序，名字升序  使用lambda可以自定义不同项的升降序
print(y)
z = sorted(mydict, key=lambda x: ([i for i in x.keys()], [i for i in x.values()][0][0], -[i for i in x.values()][0][1]))
print(z)  # 名字升序，首字母升序，名字长度降序  使用迭代读取处单个字典内的信息
# ——————————————————————————————————————————————————
"""
    浅拷贝拷贝的是对象的地址，深拷贝拷贝的的对象的值
"""
# ——————————————————————————
test = ['a', '2', 2, 4, 5, '2', 'b', 4, 7, 'a', 5, 'd', 'a', 'z']
print(collections.Counter(test))
# -----------------------------------------------------
"""
data = pd.read_csv("telelist.csv", usecols=[0, 1, 2, 3, 4], chunksize=15, iterator=True)
usecols为所需列，chunksize将所有数据分块每次显示15,data为一个可迭代对象
"""
# ---------------------------------------------------------------------
"""
element tree解析xml格式的文件
pickle 执行序列化的操作
json 也可以用来处理处理序列化的操作
发布订阅模式用blinker或python-message
"""


# ——————————————————————————————————————————————————————
def work():
    print('work hard')


def rest():
    print('enjoy')


class Person:
    pass


people = Person()
for i in range(1, 8):
    if i > 5:
        people.day = rest
    else:
        people.day = work
    people.day()


# 根据不同的需要，将实例的方法替换掉
# -------------------------------
"""
使用自带的gc模块控制垃圾回收
显式调用gc.collect()进行垃圾回收
或检查并设置threshold的阈值

"""
