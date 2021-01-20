a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print("Error!")


s = divide(a, b)
if s is not None:
    print(s)
