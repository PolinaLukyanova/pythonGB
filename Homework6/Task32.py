# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


def find_index(arr, minimum, maximum):
    index = []
    for i in range(len(arr)):
        if minimum <= arr[i] <= maximum:
            index.append(i)
    return index

n = int(input('Введите количество элементов в списке: '))
arr = []
for i in range(n):
    arr.append(int(input('Введите элемент списка: ')))


minimum = int(input('Введите минимальное значение диапазона: '))
maximum = int(input('Введите максимальное значение диапазона: '))

index = find_index(arr, minimum, maximum)

print('Индексы элементов массива, значения которых находятся в диапазоне', minimum, 'до', maximum, ':', index)
