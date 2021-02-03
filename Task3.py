class Worker:
    name = 0
    surname = 0
    position = 0
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, _income):
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


r = Position({"wage": 5000, "bonus": 1000})
r.name = "Ivan"
r.surname = "Petrov"
r.position = "Economist"
print(r.get_full_name())
print(r.get_total_income())
