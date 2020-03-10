import reprlib
from numpy import array
import functools
import operator


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)  # 使用有限长度表示形式
        components = components[components.find('[') + 1:-2]  # 构造格式
        return 'vector({})'.format(components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    '''def __bytes__(self):
        return (bytes([ord(self.typecode)])) + bytes(self._components)

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)'''

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        return self._components[item]

    def __getattr__(self, item):  # 创建了某种默认的快速索引
        shortcut = 'xyzt'
        if len(item) == 1:
            return self._components[shortcut.index(item)]

    def __setattr__(self, key, value):  # 可以快速设置特定位置的值
        shortcut = 'xyzt'
        if len(key) == 1:  # 只单独处理特殊情况
            self._components[shortcut.index(key)] = value
        else:
            return super().__setattr__(key, value)

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        # 也可以用map的形式，hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)  # 0为初始值，只好设置一下


test = Vector([1, 2, 3, 4, 5])
print(test.y)
test.y = 10
print(test)


