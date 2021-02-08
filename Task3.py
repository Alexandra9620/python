class Cells:
    def __init__(self, cell_count):
        self._cell_count = cell_count

    def __add__(self, other):
        return Cells(self._cell_count + other._cell_count)

    def __sub__(self, other):
        count = self._cell_count - other._cell_count
        if count < 0:
            print("Нельзя выполнить вычитание")
            return Cells(0)
        return Cells(count)

    def __mul__(self, other):
        return Cells(self._cell_count * other._cell_count)

    def __mul__(self, other):
        return Cells(int(self._cell_count.other._cell_count))

    def make_order(self, row_cells):
        cell_str = "*" * min(row_cells, self._cell_count)
        result = ""

        for i in range(int(self._cell_count / row_cells)):
            result += cell_str + "\n"

        if self._cell_count % row_cells > 0:
            result += "*" * (self._cell_count % row_cells)

        return result


cells1 = Cells(6)
cells2 = Cells(7)
result_cells = cells1 + cells2
print(result_cells.make_order(5))
