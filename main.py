import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

import emoji

import currency_support
from  utils.config_processor import DotEnvHelper

env: DotEnvHelper  = DotEnvHelper()
storage: MemoryStorage = MemoryStorage()
bot: Bot = Bot(env.get_value(env.BOT_TOKEN_FIELD))
dp: Dispatcher = Dispatcher(bot, storage=storage)

async def set_main_menu(dp: Dispatcher):
    print("set")
    main_menu_commands = [
        types.BotCommand(command='/help', description='Справка по работе бота'),
        types.BotCommand(command='/start', description='Выбрать валюту для быстрого перевода')
    ]
    await dp.bot.set_my_commands(main_menu_commands)

class FSMFChooseCPair(StatesGroup):
    first_currency = State()
    second_currency = State()
    pair_created = State()

def createButton(cur: currency_support.Currency)->InlineKeyboardButton:
    return InlineKeyboardButton(text=emoji.emojize(cur.name+' '+cur.emoji), callback_data=cur.curryncyCode)

def makeCurrencyKeyboard(excluded = list()) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width = 2)
    [markup.insert(createButton(item)) for item in currency_support.createInitalCurrenciesList() if item.curryncyCode not in excluded]
    return markup

def addMenu(markup: InlineKeyboardMarkup) -> InlineKeyboardMarkup:
    acceptButton = InlineKeyboardButton(text=emoji.emojize("Принять"+':check_mark_button:'), callback_data="accept")
    cancelButton = InlineKeyboardButton(text=emoji.emojize("Отменить"+':X:'), callback_data="cancel")
    backButton = InlineKeyboardButton(text=emoji.emojize("Назад"+':BACK_arrow:'), callback_data="back")
    
    markup.row(acceptButton, cancelButton, backButton)
    
    return markup
    
async def process_help_command(message: Message):
    await message.answer(text='Этот бот демонстрирует работу FSM\n\n'
                              'Чтобы перейти к заполнению анкеты - '
                              'отправьте команду /start')

async def process_start_command(message: Message):
    markup = makeCurrencyKeyboard()
    await message.answer(text='Выберите конвертиртируемую валюту\n',
                         reply_markup=markup)
    await FSMFChooseCPair.first_currency.set()
    print("Setting first state....")

async def process_set_second(callback: CallbackQuery, state: FSMFChooseCPair):
    cur = callback.data
    
    async with state.proxy() as data:
        data['from'] = cur
    
    markup = makeCurrencyKeyboard(cur)
    markup = addMenu(markup)

    await callback.message.edit_text(text='Выберите валюту для ковертации\n',
                         reply_markup=markup)
    await FSMFChooseCPair.second_currency.set()

async def process_finish(callback: CallbackQuery, state: FSMFChooseCPair):
    cur = callback.data
    
    async with state.proxy() as data:
        data['to'] = cur
    
    fromC, to = data['from'], data['to']
    
    await  callback.message.edit_text(text=f'{fromC}-{to}!\n')
    await FSMFChooseCPair.pair_created.set()


dp.register_message_handler(process_help_command,
                            commands='help')

dp.register_message_handler(process_start_command,
                            commands='start')

dp.register_callback_query_handler(process_set_second,
                            state=FSMFChooseCPair.first_currency)

dp.register_callback_query_handler(process_finish,
                            state=FSMFChooseCPair.second_currency)

set_main_menu(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_main_menu)
