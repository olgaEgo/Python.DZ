# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов. (подробности в конце записи семинара).
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from decimal import Decimal
import random

n = random.randint(2, 10)
random_list = [round(random.uniform(0, 5), random.randint(0, 5)) for i in range(n)]
# random_list = [round(random.uniform(0, 5), random.randint(0, 5)) for i in range(random.randint(1, 10))]

print(random_list)
dec_list = []

for i in range(0, len(random_list)):
    if random_list[i] % 1 > 0:
        random_list[i] = (random_list[i])
        dec_list.append(round(random_list[i] % 1, 5))

if len(dec_list) == 1:
    print('В списке только один элемент с дробной частью.')
else:
    diff = round(max(dec_list) - min(dec_list), 5)
    print(f'Разница между максимальным {max(dec_list)} и минимальным {min(dec_list)}')
    print(f'значениями дробной части элементов равна: {diff}')
