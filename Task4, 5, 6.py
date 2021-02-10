class Storage:
    _items = {}

    def add_equipment(self, item, count):
        items_count = self._items.get(item.name)
        if items_count == None:
            items_count = 0
        self._items[item.name] = items_count + count

    def remove_equipment(self, item, count):
        items_count = self._items.get(item.name)
        if items_count == None:
            items_count = 0
        self._items[item.name] = max(0, items_count - count)

    def print_equipment(self):
        print("Оборудование на складе: ")
        for name in self._items.keys():
            print(f"Количество оборудования типа '{name}': {self._items[name]}")


class OfficeEquipment:
    model_name = ""
    name = ""


class Printer:
    name = "принтер"
    paper_count = 0
    is_colored = False


class Scanner:
    name = "сканер"
    scans_count = 0


class Copier:
    name = "копир"
    paper_count = 0


storage = Storage()
while True:
    name = input("Введите тип оборудования (принтер, сканер, копир): ")
    action = input("Введите действие (добавить, забрать): ")
    count = 0
    try:
        count = int(input("Введите количество единиц оборудования: "))
    except ValueError:
        print("Количетво должно быть целым числом")
        continue

    item = None
    if name == "принтер":
        item = Printer()
    elif name == "сканер":
        item = Scanner()
    elif name == "копир":
        item = Copier()
    else:
        print("Неверный тип оборудования")
        continue

    if action == "добавить":
        storage.add_equipment(item, count)
    else:
        storage.remove_equipment(item, count)

    print("")
    storage.print_equipment()
    print("")
