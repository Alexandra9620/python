count = int(input("Сколько чисел хотите ввести: "))
numbers = []

while len(numbers) < count:
    n = int(input("Введите число: "))
    numbers.append(n)

l = len(numbers)
if l % 2 == 1:
    l = l - 1

numbers[:l:2], numbers[1:l:2] = numbers[1:l:2], numbers[:l:2]

print("Измененный список: ", numbers)
