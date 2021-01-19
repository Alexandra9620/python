words = input('Введите слова через пробел: ')
for num, word in enumerate(words.split()):
    if len(word) > 10:
        print(num + 1, word[0:10])
    else:
        print(num + 1, word)
