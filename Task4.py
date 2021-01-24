def my_func1(x, y):
    """Возвращает x в степени y"""
    return x ** y


def my_func2(x, y):
    """Возвращает x в отрицательной степени y"""
    i = 0
    p = 1
    while i < abs(y):
        i += 1
        p = x * p
    return 1 / p


print(my_func1(2, -3))

print(my_func2(2, -3))
