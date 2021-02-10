class DivisionByZero(Exception):
    def __init__(self, message="Попытка деления на ноль"):
        super().__init__(message)

n1, n2 = input("Введите делимое и делитель через пробел: ").split()
n1 = int(n1)
n2 = int(n2)

if n2 == 0:
    raise DivisionByZero()

print(f"{n1} / {n2} = {n1 / n2}")