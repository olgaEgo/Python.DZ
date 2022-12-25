# Пройтись по своим предыдущим ДЗ и где возможно использовать
# ускореную обработку данных (достаточно 3 примеров).

# # 2. Задайте список из n чисел последовательности (1 + 1/n)^n.
# # Вывести в консоль сам список и сумму его элементов.
#
# number = int(input('Введите число: '))
# my_list = []
#
# for i in range(1, number + 1):
#     my_list.append((1 + 1 / i) ** i)
#
# print(my_list, sep=', ')
# print(sum(my_list))


number = int(input('Введите число: '))
my_list = [i for i in range(1, number + 1)] # comprehension
l = lambda x: (1 + 1 / x) ** x #lambda
my_list = list(map(l, my_list)) # map

print(my_list, sep=', ')
print(sum(my_list))

