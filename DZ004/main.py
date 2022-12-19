# А. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as RI

print(f'Задача А')
k = RI(0, 10)
print(f'Задана натуральная степень k = {k}.')


def generate_polynom(k: int) -> str:
    polynom = ''
    for i in range(k, -1, -1):
        if k == 0:
            polynom = f'0'
        else:
            coef = RI(-100, 100)
            if coef == 0:
                polynom += f''

            elif coef == 1:
                if i == k:
                    polynom += f'x**{i}'
                elif i == 1:
                    polynom += f' + x'
                elif i == k and i == 1:
                    polynom += f'x'
                elif i == 0:
                    polynom += f' + {coef}'
                else:
                    polynom += f' + x**{i}'

            elif coef == -1:
                if i == k:
                    polynom += f'-x'
                elif i == 1:
                    polynom += f' - (-x)'
                elif i == k and i == 1:
                    polynom += f'-x'
                elif i == 0:
                    polynom += f' - {-coef}'
                else:
                    polynom += f' - x**{i}'

            elif coef < -1:
                if i == k and k == 1:
                    polynom += f'{coef}*x'
                elif i == k and i == 1:
                    polynom += f'{coef}*x'
                elif i == k:
                    polynom += f'{coef}*x**{i}'
                elif i == 1:
                    polynom += f' - {-coef}*x'
                elif i == 0:
                    polynom += f' - {-coef}'
                else:
                    polynom += f' - {-coef}*x**{i}'

            elif coef > 1:
                if i == k and k == 1:
                    polynom += f'{coef}*x'
                elif i == k and i == 1:
                    polynom += f'{coef}*x'
                elif i == k:
                    polynom += f'{coef}*x**{i}'
                elif i == 1:
                    polynom += f' + {coef}*x'
                elif i == 0:
                    polynom += f' + {coef}'
                else:
                    polynom += f' + {coef}*x**{i}'

    if polynom.startswith(' + '):
        polynom = polynom[3:]
    elif polynom.startswith(' - '):
        polynom = polynom.replace(' - ', '-')
    polynom += ' = 0'
    return polynom


pol_str = generate_polynom(k)
print(f'Запишем в файл многочлен степени k:\n{pol_str}')
print()

with open('A_polynom.txt', 'w') as f:
    f.write(pol_str)

# В. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

print(f'Задача В')

k1 = RI(0, 10)
with open('First_polynomial.txt', 'w') as f1:
    f1.write(generate_polynom(k1))

k2 = RI(0, 10)
with open('Second_polynomial.txt', 'w') as f2:
    f2.write(generate_polynom(k2))

with open('First_polynomial.txt', 'r') as file:
    first_pol = file.readline()
with open('Second_polynomial.txt', 'r') as file:
    second_pol = file.readline()

print(f'Первый полином: {first_pol}')
print(f'Второй полином: {second_pol}')


def polynomial_to_dict(polynomial_str: str) -> dict:
    item_list = []
    polynomial_str = polynomial_str.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').split(' ')
    for item in polynomial_str:
        if "*x**" in item:
            item = item.replace("*x**", ' ')
        elif 'x**' in item:
            item = item.replace("x**", '1 ')
        elif '*x' in item:
            item = item.replace("*x", ' 1')
        elif 'x' in item:
            item = item.replace('x', '1 1')
        elif 'x' not in item:
            item += ' 0'
        item = item.split(' ')
        #  print(item, end=' ')
        item[0], item[1] = int(item[1]), int(item[0])
        item_list.append(item)
    pol_dict = {}
    for item in item_list:
        pol_dict[item[0]] = item[1]
    return pol_dict


first_dict = polynomial_to_dict(first_pol)
second_dict = polynomial_to_dict(second_pol)


def dicts_sum(first: dict, second: dict) -> dict:
    sum_dict = first | second
    zero_list = []
    for i in sum_dict:
        if i in first and second:
            sum_dict[i] = first.get(i, 0) + second.get(i, 0)
            if sum_dict.get(i) == 0:
                zero_list.append(i)
        elif first.get(i):
            sum_dict[i] = first.get(i)
        else:
            second.get(i)
            sum_dict[i] = second.get(i)
    for item in zero_list:
        del sum_dict[item]

    sum_dict_sort = dict(sorted(sum_dict.items())[::-1])

    return sum_dict_sort


d_s = dicts_sum(first_dict, second_dict)


def polynomial_result(poli_dict: dict):
    res_str = ''
    first = True
    for (key, value) in poli_dict.items():
        if value != 0:
            if first:
                if value > 0:
                    res_str += f'{value}*x**{key} '
                else:
                    res_str += f'-{value * (-1)}*x**{key} '
                first = False
            else:
                if value == 1:
                    if key == 1:
                        res_str += f'+ x '
                    elif key == 0:
                        res_str += f'+ 1 '
                    else:
                        res_str += f'+ x**{key} '
                elif value > 1:
                    if key == 1:
                        res_str += f'+ {value}*x '
                    elif key == 0:
                        res_str += f'+ {value} '
                    else:
                        res_str += f'+ {value}*x**{key} '
                elif value == -1:
                    if key == 1:
                        res_str += f'- x '
                    elif key == 0:
                        res_str += f'- 1 '
                    else:
                        res_str += f'- x**{key} '
                elif value < 1:
                    if key == 1:
                        res_str += f'- {abs(value)}*x '
                    elif key == 0:
                        res_str += f'- {abs(value)} '
                    else:
                        res_str += f'- {abs(value)}*x**{key} '
    return res_str + '= 0'


print(f'Сумма полиномов: {polynomial_result(d_s)}')

with open('Sum_polynomials.txt', 'w') as f:
    f.write(polynomial_result(d_s))
