import re
import itertools

RE_WORD = re.compile(r'\w+')  # 匹配多个数字字母及下划线


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'sentense:{}'.format(self.text)

    def __iter__(self):
        for word in RE_WORD.finditer(self.text):  # 构建迭代器
            yield word.group()  # 从实例中提取匹配正则表达式的具体文本
        return  # 此处的return非必要
        # return (match.group() for match in RE_WORD.finditer(self.text))


#  等差数列生成器


def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index


x = aritprog_gen(3, 10, 100)  # x是一个生成器
for i in x:
    print(i)

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1.0, 0.5))
