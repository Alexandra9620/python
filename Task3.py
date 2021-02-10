class ListContainsNonNumberValue(Exception):
    def __init__(self, message="Список содержит не только числа"):
        super().__init__(message)


my_list = []
while True:
    try:
        value = input("Введите число: ")
        if value == "stop":
            print("Список: ", my_list)
            break

        if not value.isnumeric():
            raise ListContainsNonNumberValue()

        my_list.append(int(value))
    except (ListContainsNonNumberValue):
        print("Введенное значение не является числом")
