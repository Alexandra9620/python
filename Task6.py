count = int(input("Введите количество товаров: "))
items = []
index = 1

while len(items) < count:
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    amount = int(input("Введите количество товара: "))
    unit = input("Введите единицу измерения: ")

    items.append((index, {"название": name, "цена": price, "количество": amount, "ед": unit}))
    index = index + 1

analytics_dict = {
    "название": [],
    "цена": [],
    "количество": [],
    "ед": [],
}

for item in items:
    data = item[1]
    analytics_dict.get("название").append(data.get("название"))
    analytics_dict.get("цена").append(data.get("цена"))
    analytics_dict.get("количество").append(data.get("количество"))
    analytics_dict.get("ед").append(data.get("ед"))

print(analytics_dict)
