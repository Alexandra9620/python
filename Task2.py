from abc import ABC


class Clothes(ABC):
    def __init__(self, name):
        self._name = name

    @property
    def size(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        self._name = name
        self._v = v

    @property
    def size(self):
        return self._v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, h):
        self._name = name
        self._h = h

    @property
    def size(self):
        return 2 * self._h + 0.3


coat1 = Coat("Серое пальто", 42)
print("Количество ткани для пальто:", coat1.size)

suit1 = Suit("Строгий костюм", 170)
print("Количество ткани для костюма:", suit1.size)
