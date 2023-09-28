# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)




import random

class Matrix:

    def __init__(self, row, col):
        self.n = row
        self.matrix = [[random.randrange(0, 10) for a in range(col)] for b in range(row)]

    def print(self):
        matrix = self.matrix
        for im in range(len(matrix)):
            print(matrix[im])

    def find_max(self):
        max_sum = 0
        n = self.n
        m = self.matrix
        index = -1
        for x in range(n):
            if sum(m[x]) > max_sum:
                max_sum = sum(m[x])
                index = x
        print("максимум: %s, индекс: %s" % (max_sum, index))
        return max_sum, index

    def remove_max_row(self):
        matrix = self.matrix
        n = self.n
        max_value, index = self.find_max()
        matrix.remove(matrix[index])
        for im in range(n-1):
            print(matrix[im])

Matrix(5, 5).print()
print('-'*100)
Matrix(5, 5).find_max()
print('='*100)
Matrix(5, 5).remove_max_row()
