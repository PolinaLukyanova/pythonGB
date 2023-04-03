# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# k = 0
# n = int(input('Введите колличесво элементов: '))
# a = map(int, input(f'Введите {n} элемента через пробел: ').split())
# a = list(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         k += 1
# print(k)


start_list = [0, -1, 5, 2, 3]

count_nums = 0
for i in range(1, len(start_list)):
    if start_list[i] > start_list[i - 1]:
        count_nums += 1
print(count_nums)