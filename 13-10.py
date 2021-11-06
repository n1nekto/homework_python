# Написать класс Матрица, при инициализации принимает вложенный список (матрицу),
# но проверяет, что длины строк равны.
# Написать в классе метод, который транспонирует матрицу и возвращает её.


from random import randint

class Matrix():
    def __init__(self, arg):
        for i in range(len(arg)):
            if len(arg[0]) == len(arg[i]):
                pass
            else:
                raise Exception('Не матрица')
        self.mt = arg[:]

    def Transpose(self):
        mat = []
        m = len(self.mt[0])
        n = len(self.mt)

        for i in range(m):
            mat.append([])
            for j in range(n):
                mat[i].append(0)

        for i in range(m):
            for j in range(n):
                mat[i][j] = self.mt[j][i]
        self.mt = mat[:]

    def show(self):
        for i in range(len(self.mt)):
            print(*self.mt[i])

n, m = map(int, input().split())
a = []
for i in range(n):
    tmp = []
    for j in range(m):
        tmp.append(randint(0, 100))
    a.append(tmp)

b = Matrix(a)
b.show()
print()
b.Transpose()
b.show()
