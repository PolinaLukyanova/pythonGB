# Задача №41. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод:               Ввод:
# 5                   5
# 1 2 3 4 5           1 5 1 5 1
# Вывод:              Вывод:
# 0                   2
def find_elem(a):
    count = 0
    for i in range(1, n - 1):
        if a[i] > a[i - 1] and a[i] > a[i+1]:
            count += 1
    return count

n = int(input('Введите количесво элементов в массиве: '))
a = []
for i in range(n):
    a.append(int(input('Введите элемент массива: ')))


print('Количество элементов, у которых два соседних и, при этом,'\
      ' оба соседних элемента меньше данного:', find_elem(a))