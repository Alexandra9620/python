class Matrix:
    def __init__(self, matrixlist):
        self.matrixlist = matrixlist

    def __str__(self):
        result = ""

        for row in self.matrixlist:
            for value in row:
                result += str(value) + " "

            result += "\n"

        return result

    def __add__(self, other):
        result = []
        for i, row in enumerate(self.matrixlist):
            result.append([])
            for j, value in enumerate(row):
                result[i].append(value + other.matrixlist[i][j])

        return Matrix(result)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
matrix_2 = Matrix([[7, 8], [9, 10], [11, 12]])

print(matrix_1 + matrix_2)
# превратить в строку и вшить /n
