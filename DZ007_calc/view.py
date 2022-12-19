def result_data(data):
    print(f'Результат вычислений: {data}')


def first_input():
    fst_inp = input('Введите число: ')
    return fst_inp


def input_num() -> float:
    num = float(input('Введите следующее число: '))
    return num

    # try:
    #     num = float(input('Введите следующее число: '))
    #     return num
    # except :
    #     print('Неверный ввод')


def input_oper():
    oper = input('Введите операцию (+, -, *, /, =): ')
    return oper
