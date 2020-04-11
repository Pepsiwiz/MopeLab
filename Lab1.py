import numpy

print("~" * 70)
while True:
    try:
        a0 = int(input("Введіть значення a0: "))
        a1 = int(input("Введіть значення a1: "))
        a2 = int(input("Введіть значення a2: "))
        a3 = int(input("Введіть значення a3: "))
        n = int(input("Введіть діапазон чисел: "))
        break
    except (NameError, ValueError):
        print("Виникла помилка, спробуйте ще раз")

# матриця
print("~" * 70)
matrix = numpy.floor(n * numpy.random.random((8, 3)))
print("Матриця планування 8x3: \n", numpy.matrix(matrix))
print("~" * 70)

y = []  # регресія У
for i in range(len(matrix)): y.append(a0 + a1 * matrix[i][0] + a2 * matrix[i][1] + a3 * matrix[i][2])
print("Значення регресії Y: " + str(y))
print("~" * 70)

# значення фактора x0
# інтервал зміни фактора
lst_x0 = []
lst_dx = []
for i in range(3):
    lst = []
    for j in range(8):
        lst.append(matrix[j][i])
    min_x = min(lst)
    max_x = max(lst)
    x0 = (max_x + min_x) / 2
    dx = x0 - min_x
    lst_x0.append(x0)
    lst_dx.append(dx)
    lst.clear()

print("Значення фактора x0 = " + str(lst_x0))
print("~" * 70)
print("Інтервал зміни фактора dx: " + str(lst_dx))
print("~" * 70)

nx = []  # нормоване значення
for i in range(len(matrix)):
    nx.append([])
    for j in range(len(matrix[i])):
        nx[i].append(round((matrix[i][j] - lst_x0[j]) / lst_dx[j], 1))
print("Нормоване значення Хн: \n", numpy.matrix(nx))
print("~" * 70)
# середне значення Y
y_s = (min(y) + max(y)) / 2
print("Ys = " + str(y_s))
print("~" * 70)

# еталонне значення Ует
y_etalon = a0 + a1 * lst_x0[0] + a2 * lst_x0[1] + a3 * lst_x0[2]
print("Функція відгуку від нульових рівнів факторів Yeт: " + str(y_etalon))
print("~" * 70)

# Завдання за варіантом ->Уs
my_list = y[:]
my_list.sort()
for element in my_list:
    if element >= y_s:
        print("->Ys" + str(element))
        print("~" * 70)
        indx = my_list.index(element)
        print("Наша точка:" + str(matrix[indx]))
        break
print("~" * 70)
