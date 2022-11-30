# 1. Напишите программу, которая принимает на вход вещественное число и
# показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
# # Первый способ:

# number = abs(input('Введите число: '))
# number1 = number.replace('.', '0')
# result = 0
# for i in number1:
#     result += int(i)
#
# print(f'Сумма цифр числа {number} равна {result}')
#

# Второй способ:
from decimal import Decimal

number = abs(Decimal(input('Введите число: ')))
result_sum = 0

if number != int(number):
    while number % 1 > 0:
        number *= 10
#       print(number)
    while number >= 1:
        result_sum += int(number % 10)
        number /= 10
else:
    while number >= 1:
        result_sum += int(number % 10)
        number /= 10
        # print(f'sum {result_sum}')
        # print(f'number {number}')

print(result_sum)
