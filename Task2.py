class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calculate(self, _weight, _thickness):
        return self._length * self._width * _weight * _thickness / 1000


a = Road(20, 5000)
print(a.calculate(25, 5), 'т.')
