class Stationery:
    title = ""

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой "{self.title}"')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом "{self.title}"')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером "{self.title}"')


pencil = Pencil("Деревянный карандаш")
pencil.draw()

handle = Handle("Красный маркер")
handle.draw()

pen = Pen("Ручка 1")
pen.draw()

pen = Pen("Ручка 2")
pen.draw()
