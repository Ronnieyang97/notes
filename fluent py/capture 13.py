import itertools

class Vector:
    def __init__(self, components: list):
        self._components = components

    def __neg__(self):
        return Vector([-x for x in self._components])

    def __pos__(self):
        return Vector(self._components)

    def __repr__(self):
        return 'vector{}'.format(self._components)

    def __add__(self, other):
        # return Vector([x1 + x2 for x1, x2 in zip(self._components, other._components)])
        return Vector([x1+x2 for x1, x2 in itertools.zip_longest(self._components, other._components, fillvalue=0)])


vector1 = Vector([1, 2, 3, 4])
vector2 = Vector([5, 6, 7])
print(vector1 + vector2)
