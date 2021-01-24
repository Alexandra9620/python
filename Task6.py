def int_func(word):
    """Возвращает слово с заглавной буквы"""
    return word.title()


words = input("Введите слова, разделенные пробелом: ").split()
title_words = []
for i, k in enumerate(words):
    if k.isascii():
        title_words.append(int_func(k))
    else:
        print(k, "не состоит из латинских букв")

print(" ".join(title_words))
