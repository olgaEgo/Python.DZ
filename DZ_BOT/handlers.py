from aiogram import types, Dispatcher

import commands


def registered_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands='start')
    dp.register_message_handler(commands.coin, commands='game')
    dp.register_message_handler(commands.player_first)
