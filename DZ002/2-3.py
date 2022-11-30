# 3. Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать!
# Реализовать свой метод
import random

rand_list = []
for i in range(1, 6):
    rand_list.append(random.randint(1, 100))
print(rand_list)

res_list = []
for i in range(1, 6):
    index = random.randint(0, len(rand_list) - 1)
    res_list.append(rand_list[index])
    rand_list.remove(rand_list[index])
print(res_list)
