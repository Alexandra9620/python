with open('input_files/Task3.txt', 'r') as f:
    total_salary = 0
    size = 0
    for line in f:
        name, salary = line.split()
        salary = float(salary)
        size += 1
        if salary < 20000:
            print(name)
        total_salary += salary
    print(f'Средняя величина дохода сотрудников: {total_salary / size}')
