with open('Task2.txt', 'r') as f:
    size = 0
    for line in f:
        size += 1
        words = len(line.split())
        print(f'Количество слов в строке: {words}')
    print(f'Количество строк: {size}')
