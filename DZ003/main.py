# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

random_list = [random.randint(1, 10) for i in range(1, 11)]
print(random_list)

# random_string = str(random_list)
# print(random_string[::2])

result_sum = 0
result_list = []
for i in range(1, len(random_list), 2):
    result_sum += random_list[i]
    result_list.append(random_list[i])

print(f'На нечётных позициях элементы {result_list},\nих сумма равна {result_sum}.')
