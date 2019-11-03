from collections import namedtuple

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
a = [str(i) if i > 3 else i*i for i in range(5) if i % 2 == 0]
# 上式相当于
a = []
for i in range(5):
    if i % 2 == 0:
        if i > 3:
            a.append(str(i))
        else:
            a.append(i*i)
# 多重迭代
test = [(a, b)for a in ['a', 5, '8'] for b in ['f', '5', '8'] if a != b]
print(test)  # 多重迭代会对a,b所在的列表求笛卡尔积，并根据条件筛选

