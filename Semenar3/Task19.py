# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
 
# # Решение 1
# list = [1, 2, 3, 4, 5]
# k = 4 % len(list)
# print(list)
# print(list[k:] + list[:k])


# # Решение 2
# list = [1, 2, 3, 4, 5]
# print(list)
# n,k = len(list),4

# while k > 0:
#     list.append(list.pop(0))
#     k -= 1
#     print(list)


# Решение 3
list = [1, 2, 3, 4, 5]
k = 3 % len(list)
# используем фор в диапазоне к
for i in range(k-1):
    num = list.pop(-1)
    list.insert(0, num)
print(list)

