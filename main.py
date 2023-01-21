from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, Message)

BOT_TOKEN = '424888719:AAFkATFsGPyA8-C34Y5ZMbGrXrDvXhZu0Zw'

storage: MemoryStorage = MemoryStorage()

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher(bot, storage=storage)

user_dict = {}


def Currency:
    def __init__(self, name: str, currencyCode:str):
        self.name = name
        self.curryncyCode = currencyCode



def makeCurrencyKeyboard() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()

    amd_button = InlineKeyboardButton(text='Армянский драм',
                                            callback_data='amd')
    rub_button = InlineKeyboardButton(text='Российский рубль',
                                         callback_data='rub')
    usd_button = InlineKeyboardButton(text='Американский доллар',
                                         callback_data='usd')
    eur_button = InlineKeyboardButton(text='Евро',
                                         callback_data='eur')

    markup.add(amd_button, rub_button).add(usd_button, eur_button)

async def process_help_command(message: Message):
    await message.answer(text='Этот бот демонстрирует работу FSM\n\n'
                              'Чтобы перейти к заполнению анкеты - '
                              'отправьте команду /start')

async def process_start_command(message: Message):
    markup = InlineKeyboardMarkup()

    amd_button = InlineKeyboardButton(text='Армянский драм',
                                            callback_data='amd')
    rub_button = InlineKeyboardButton(text='Российский рубль',
                                         callback_data='rub')
    usd_button = InlineKeyboardButton(text='Американский доллар',
                                         callback_data='usd')
    eur_button = InlineKeyboardButton(text='Евро',
                                         callback_data='eur')

    markup.add(amd_button, rub_button).add(usd_button, eur_button)

    await message.answer(text='Спасибо!\n\nУкажите ваше образование',
                         reply_markup=markup)


async def process_education_press(callback: CallbackQuery, state: FSMContext):

    markup = InlineKeyboardMarkup()
    amd_button = InlineKeyboardButton(text='Армянский драм',
                                            callback_data='amd')
    rub_button = InlineKeyboardButton(text='Российский рубль',
                                         callback_data='rub')
    usd_button = InlineKeyboardButton(text='Американский доллар',
                                         callback_data='usd')
    eur_button = InlineKeyboardButton(text='Евро',
                                         callback_data='eur')
    
    
    await callback.message.edit_text(text='Спасибо!\n\n'
                                          'Остался последний шаг.\n'
                                          'Хотели бы вы получать новости?',
                                     reply_markup=markup)
    # Устанавливаем состояние ожидания выбора получать новости или нет



dp.register_message_handler(process_help_command,
                            commands='help')

dp.register_message_handler(process_start_command,
                            commands='start')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)