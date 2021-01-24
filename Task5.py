def get_sum(nums_str):
    """Возвращает сумму чисел, содержащихся в строке и разделенных пробелом"""
    nums = nums_str.split()
    nums_sum = 0

    for n in nums:
        try:
            nums_sum += int(n)
        except ValueError:
            print(n, "не является числом")

    return nums_sum

total_sum = 0

while True:
    nums = input("Введите строку чисел, разделенных пробелом: ")
    total_sum += get_sum(nums)
    print("Общая сумма: ", total_sum)