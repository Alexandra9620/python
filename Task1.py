my_f = open("My_text.txt", "w")
while True:
    line = input('Введите необходимые данные:')
    if line == '':
        my_f.close()
        print('Файл закрыт: ', my_f.closed)
        break
    else:
        my_f.writelines(line + '\n')
