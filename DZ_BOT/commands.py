import random

from aiogram import types

from config import dp, bot

TOTAL = 150


@dp.message_handler(commands='start')
async def start(message: types.Message):
    print(message.text)
    await message.answer(f'Привет, {message.from_user.first_name}! '
                         f'Я Boty! Со мной можно играть в конфеты. '
                         'Условие игры: На столе лежит 150 конфета. '
                         'Играем вдвоём, делая ход друг за другом. '
                         'Первый ход определяется жеребьёвкой. За один ход '
                         'можно забрать не более 28 конфет. Все конфеты '
                         'достаются сделавшему последний ход.\n'
                         'Начинаем игру? /game')


@dp.message_handler(commands='game')
async def coin(message: types.Message):
    coin_n = random.randint(1, 2)
    if coin_n == 1:
        await bot.send_message(
            message.from_user.id, 'Твой ход!\nСколько конфет возьмёшь? ')
    else:
        await bot.send_message(message.from_user.id, 'Я хожу!')
        await boty_first(message)


@dp.message_handler()
async def player_first(message: types.Message):
    global TOTAL
    print('player')
    if TOTAL > 0:
        player = message.text
        amount = int(player)
        if amount > 28 or TOTAL < 0:
            await bot.send_message(message.from_user.id,
                                   f'{message.from_user.first_name}, '
                                   f'очень много взял/а!')
        elif amount == 0:
            await message.reply('Надо обязательно взять хоть одну конфетку!')
        else:
            TOTAL -= amount
            await bot.send_message(message.from_user.id,
                                   f'{message.from_user.first_name}, '
                                   f'взял {amount} конфет/ты. '
                                   f'На столе осталось {TOTAL} конфет/ты')
            if TOTAL == 0:
                await bot.send_message(
                    message.from_user.id, 'Все конфеты достаются тебе((( '
                                          'Поделишься?)')
                TOTAL = 150
            else:
                await bot.send_message(
                    message.from_user.id, 'Моя очередь ходить!')
                while TOTAL > 28:
                    boty = TOTAL % 29
                    TOTAL -= boty
                    if boty == 0:
                        boty = random.randint(1, 28)
                        TOTAL -= boty
                    await bot.send_message(
                        message.from_user.id, f'Boty, взял {boty} конфет/ты. '
                        f'На столе осталось {TOTAL} конфет/ты\n'
                                              f'Твоя очередь ходить!')
                    break
                else:
                    boty = TOTAL
                    TOTAL -= boty
                    await bot.send_message(
                        message.from_user.id, f'Boty, взял {boty} конфет/ты. '
                        f'На столе осталось {TOTAL} конфет/ты')
                    await bot.send_message(
                        message.from_user.id, 'Все конфеты мои!!!')
                    TOTAL = 150


@dp.message_handler()
async def boty_first(message: types.Message):
    global TOTAL
    print("boty")
    if TOTAL > 0:
        while TOTAL > 29:
            boty = TOTAL % 29
            TOTAL -= boty
            await bot.send_message(
                message.from_user.id, f'Boty, взял {boty} конфет/ты. '
                f'На столе осталось {TOTAL} конфет/ты')
            break
        else:
            boty = TOTAL
            TOTAL -= boty
            await bot.send_message(
                message.from_user.id, f'Boty, взял {boty} конфет/ты. '
                'На столе осталось {TOTAL} конфет/ты')
            await bot.send_message(message.from_user.id, 'Все конфеты мои!!!')

        await bot.send_message(
            message.from_user.id, 'Сколько конфет возьмёшь? ')
