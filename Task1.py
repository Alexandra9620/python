import time


class TrafficLight:
    # атрибуты класса
    color = ['Красный', 'Желтый', 'Зеленый']

    # методы класса
    def running(self):
        s = 0
        while True:
            if s == 0:
                print(f'{TrafficLight.color[s]}')
                time.sleep(420)
            elif s == 1:
                print(f'{TrafficLight.color[s]}')
                time.sleep(120)
            elif s == 2:
                print(f'{TrafficLight.color[s]}')
                time.sleep(420)
            s += 1


a = TrafficLight()
# print(a)
# print(type(a))
a.running()
