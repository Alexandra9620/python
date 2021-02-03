import time


class TrafficLight:
    # атрибуты класса
    __color = ['Красный', 'Желтый', 'Зеленый']

    # методы класса
    def running(self):
        s = 0
        while True:
            if s == 0:
                print(f'{TrafficLight.__color[s]}')
                time.sleep(7)
            elif s == 1:
                print(f'{TrafficLight.__color[s]}')
                time.sleep(2)
            elif s == 2:
                print(f'{TrafficLight.__color[s]}')
                time.sleep(7)
                break
            s += 1


a = TrafficLight()
# print(a)
# print(type(a))
a.running()
