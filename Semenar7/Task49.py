# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# def find_farthest_orbit(list_of_orbits):
#     max_area = 0
#     farthest_orbit = None
#     for orbit in list_of_orbits:
#         a, b = orbit
#         if a != b: # исключаем круговые орбиты
#             area = a * b * 3.14
#             if area > max_area:
#                 max_area = area
#                 farthest_orbit = orbit
#     return farthest_orbit

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits)) # 2.5 10


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
orbits = [(a,b) for (a,b) in orbits if a!=b]
space = [a*b for (a,b) in orbits]
print(orbits[space.index(max(space))])


# def find(orbits):
#     orbits=[(a,b) for (a,b) in orbits if a!=b]
#     space=[a*b for (a,b) in orbits]
#     return(orbits[space.index(max(space))])

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find(orbits))

from math import pi
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
orbits = list(filter(lambda x: x[0] != x[1], orbits))
print(orbits)
x = list(map(lambda x: x[0] * x[1] * pi, orbits))
print(x)
orbits_dict = dict(zip(x, orbits))
print(orbits_dict)
print(orbits_dict[max(kei for kei in orbits_dict.keys())])