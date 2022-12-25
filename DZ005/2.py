# 2. Создайте программу для игры в ""Крестики-нолики"".(tkinter)
import random

field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

victory_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def first_turn() -> str:
    f_t = random.randint(0, 1)
    if f_t == 0:
        turn = 'X'
    else:
        turn = 'O'
    return turn


def switch_turn(next_turn) -> str:
    if next_turn == 'X':
        next_turn = 'O'
    else:
        next_turn = 'X'
    return next_turn


def make_move(whose_turn, play_f):
    while True:
        num = input(f'Выберете ячейку для {whose_turn}: ')
        if num.isdigit():
            num = int(num)
            if 0 < num < 10 and play_f[num - 1] != 'X' and play_f[num - 1] != 'O':
                play_f[int(num) - 1] = whose_turn
            else:
                num = int(input(f'Введите номер существующей свободной ячейки для {whose_turn}: '))
                play_f[int(num) - 1] = whose_turn
        else:
            num = input(f'Ошибка ввода. Выберете ячейку для {whose_turn}: ')
            play_f[int(num) - 1] = whose_turn

        print(f' {play_f[0]} | {play_f[1]} | {play_f[2]}')
        print(f'-----------\n {play_f[3]} | {play_f[4]} | {play_f[5]}')
        print(f'-----------\n {play_f[6]} | {play_f[7]} | {play_f[8]}')
        print()
        return play_f


def check_win(v_c, play_f) -> bool:
    for comb in v_c:
        if play_f[comb[0]] == play_f[comb[1]] == play_f[comb[2]]:
            return True
    return False


def check_no_winner(play_f):
    for n in play_f:
        if n.isdigit():
            return False
    else:
        return True


turn = first_turn()
print(f'Первым ходят {turn}')
print()

print(f' {field[0]} | {field[1]} | {field[2]}')
print(f'-----------\n {field[3]} | {field[4]} | {field[5]}')
print(f'-----------\n {field[6]} | {field[7]} | {field[8]}')
print()

for i in range(0, len(field)):
    field = make_move(turn, field)
    if not check_win(victory_comb, field):
        if check_no_winner(field):
            print('Ничья! Победила дружба!!!')
            break
        else:
            turn = switch_turn(turn)
            print(f'Ходят {turn}')
    else:
        if turn == 'X':
            print('Победили X')
        else:
            print('Победили O')
        break

