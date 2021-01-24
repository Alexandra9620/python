def my_func(arg_1, arg_2, arg_3):
    """Возвращает сумму двух наибольших аргументов"""
    arg = [arg_1, arg_2, arg_3]
    arg.remove(min(arg))
    return sum(arg)


print(my_func(134, -67, 5))
