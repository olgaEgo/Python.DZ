# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроенных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

inp_number = int(input('Введите двоичное число: '))

number = inp_number
binary_list = []
while number != 0:
    if number % 2 == 0:
        binary_list.append(0)
    else:
        binary_list.append(1)
    number //= 2

print(f'Результат перевода десятичного числа {inp_number} в двоичную систему: ', end='')
print(*binary_list[::-1], sep='')
