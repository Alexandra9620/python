f = open('input_files/Task4.txt', 'r')
translations = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

f2 = open('Task4_output.txt', 'w')
for line in f:
    parts = line.split()
    parts[0] = translations[parts[0]]
    f2.writelines(" ".join(parts) + "\n")

f.close()
f2.close()
