# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:               Вывод:
# 7                   3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 





n = int(input("Введите количество элементов в первом массиве: "))
a = []
for i in range(n):
    a.append(int(input("Введите элемент массива: ")))

m = int(input("Введите количество элементов во втором массиве: "))
b = []
for i in range(m):
    b.append(int(input("Введите элемент массива: ")))

result = []
for x in a:
    if x not in b:
        result.append(x)

print("Элементы первого массива, которых нет во втором массиве:", result)
