from sys import argv

path, output_in_hours, rate_per_hour, award = argv
try:
    a = int(output_in_hours) * int(rate_per_hour) + int(award)
    print(f"Ваша заработная плата: {a}")
except ValueError:
    print("Введите целочисленное значение")
