# 2. Задайте список из n чисел последовательности (1 + 1/n)^n.
# Вывести в консоль сам список и сумму его элементов.

number = int(input('Введите число: '))
my_list = []

for i in range(1, number + 1):
    my_list.append((1 + 1 / i) ** i)

print(my_list, sep=', ')
print(sum(my_list))
