# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 150 конфета. Игрок и компьютер ходят поочереди.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# (Подумайте как наделить бота "интеллектом")
import random

total = 150
n = random.randint(1, 2)
if n == 1:
    while total > 0:
        player = int(input('Сколько конфет возьмёшь? '))
        if player > 28 or total < 0:
            input('Слишком много взял!')
        elif player == 0:
            input('Надо обязательно взять хоть одну конфетку!')
        else:
            total -= player
            print(player, total)
            if total == 0:
                input('Все конфеты достаются тебе((( Поделишься?)')
            else:
                print(f'Моя очередь ходить!')
                while total > 28:
                    bot = total % 29
                    total -= bot
                    if bot == 0:
                        bot = random.randint(1, 28)
                        total -= bot
                    print(bot, total)
                    break
                else:
                    bot = total
                    total -= bot
                    print(bot, total)
                    input('Все конфеты мои!!!')
                    break
else:
    while total > 0:
        print(f'Я хожу!')
        while total > 29:
            bot = total % 29
            total -= bot
            print(bot, total)
            break
        else:
            bot = total
            total -= bot
            print(bot, total)
            input('Все конфеты мои!!!')
            break
        player = int(input('Сколько конфет возьмёшь? '))

        if player > 28 or total < 0:
            input('Слишком много взял!')
        elif player == 0:
            input('Надо обязательно взять хотя бы одну конфетку!')
        else:
            total -= player
            print(player, total)
            if total == 0:
                input('Все конфеты достаются тебе((( Поделишься?)')
