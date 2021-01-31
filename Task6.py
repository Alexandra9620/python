f = open('input_files/Task6.txt', 'r', encoding='utf-8')

result = {}

for line in f:
    name, p1, p2, p3 = line.split()
    name = name[:-1]
    if result.get(name) == None:
        result[name] = 0

    for lesson in [p1, p2, p3]:
        count = lesson.split('(')[0]
        if count.isnumeric():
            result[name] += int(count)
print(result)
