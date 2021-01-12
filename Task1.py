number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
sign = input("Введите желаемую операцию (+, -, *, /): ")
if sign == "+":
    result = number1 + number2
    print(result)
elif sign == "-":
    result = number1 - number2
    print(result)
elif sign == "*":
    result = number1 * number2
    print(result)
elif sign == '/':
    result = number1 / number2
    print(result)
else:
    print("Неправильная операция")
