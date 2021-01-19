my_list = [9, 6, 4, 3, 3, 2, 2]
a = int(input("Введите число: "))
is_inserted = False
for i, d in enumerate(my_list):
    if a > d:
        my_list.insert(i, a)
        is_inserted = True
        break

if is_inserted == False:
    my_list.append(a)

print(f"Пользователь ввел число {a}. Результат: {my_list}")
