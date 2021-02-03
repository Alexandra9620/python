class Car:
    speed = 0
    is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def go(self, speed):
        self.speed = speed
        print(f'Машина {self.name} поехала')

    def stop(self):
        self.speed = 0
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула {direction}')

    def showspeed(self):
        print(f'Скорость {self.name} равна {self.speed}')


class TownCar(Car):
    def showspeed(self):
        if self.speed > 60:
            print('Превышение скорости!')


class WorkCar(Car):
    def showspeed(self):
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    is_polise = True


car1 = TownCar('Lada Vesta', 'grey')
car1.go(100)
car1.showspeed()
car1.turn("налево")

car2 = WorkCar('УАЗ', 'white')
car2.go(30)
car2.showspeed()
car2.stop()
