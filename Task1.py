my_f = open("Task1.txt", "w")
while True:
    line = input('Введите необходимые данные: ')
    if line == '':
        break
    else:
        my_f.writelines(line + '\n')
my_f.close()
print('Файл закрыт: ', my_f.closed)
