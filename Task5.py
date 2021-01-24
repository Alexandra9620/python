def input_sum():
    """Выполняет ввод чисел с клавиатуры и возвращает их сумму"""
    total_sum = 0

    while True:
        nums = input("Введите цела числа через пробел или * для выхода: ").split()
        nums_sum = 0
        for n in nums:
            try:
                total_sum += int(n)
                nums_sum += int(n)
            except ValueError:
                if n == "*":
                    return total_sum
                else:
                    print(n, "не является целым числом")

        print("Сумма введенных чисел:", nums_sum)

    return total_sum


print("Сумма всех введенных чисел:", input_sum())
