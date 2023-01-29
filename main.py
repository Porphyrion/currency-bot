from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message


from  utils.config_processor import DotEnvHelper

import handlers


env: DotEnvHelper  = DotEnvHelper()
storage: MemoryStorage = MemoryStorage()
bot: Bot = Bot(env.get_value(env.BOT_TOKEN_FIELD))
dp: Dispatcher = Dispatcher(bot, storage=storage)

handlers.finit(dp)


async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/help', description='Справка по работе бота'),
        types.BotCommand(command='/start', description='Выбрать валюту для быстрого перевода')
    ]
    await dp.bot.set_my_commands(main_menu_commands)

    
async def process_help_command(message: Message):
    await message.answer(text='Этот бот демонстрирует работу FSM\n\n'
                              'Чтобы перейти к заполнению анкеты - '
                              'отправьте команду /start')

dp.register_message_handler(process_help_command,
                            commands='help')        

set_main_menu(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_main_menu)
