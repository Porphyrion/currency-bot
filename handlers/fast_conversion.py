from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher

from keyboards.keyboards import *
from states.states import * 

async def process_start_command(message: Message):
    markup = make_currency_keyboard()
    await message.answer(text='Выберите конвертиртируемую валюту\n',
                         reply_markup=markup)
    await FSMFastConversion.set_from_currency.set()


async def process_set_from(callback: CallbackQuery, state: FSMContext):
    cur = callback.data
    
    async with state.proxy() as data:
        data['from'] = cur
        data['to'] = list()
    
    markup = make_currency_keyboard(cur)
    markup = add_menu(markup)

    await callback.message.edit_text(text='Выберите валюты для ковертации\n',
                         reply_markup=markup)
    await FSMFastConversion.setting_to_currencies.set()


async def process_set_to(callback: CallbackQuery, state: FSMContext):
    res = callback.data

    if res == 'accept':   
        async with state.proxy() as data:
            data['to'].append(res) 
            fromC, to = data['from'], data['to']
            to = ' '.join(to)
            await  callback.message.edit_text(text=f'{fromC}--->{to}!\n')
            await  FSMFastConversion.currencies_choosed.set()
            return
    # elif res == 'cancel':
    #     async with state.proxy() as data:
    #         excluded  = data['to'].pop()
    #         await callback.message.edit_text(text='Выберите валюты для ковертации\n',
    #                      reply_markup=updateCurrencyKeyboard(callback.message.reply_markup, excluded))
    #         await  FSMFChooseCPair.currencies_chosed.set()
    #         return
    elif res == 'back':
        async with state.proxy() as data:
            data['to'] = list()
            
            markup = make_currency_keyboard()
            await callback.message.edit_text(text='Выберите конвертиртируемую валюту\n',
                         reply_markup=markup)
            await FSMFastConversion.set_from_currency.set()
            return
    
    async with state.proxy() as data:
        data['to'].append(res)

    
    
    await callback.message.edit_text(text='Выберите валюты для ковертации\n',
                         reply_markup=update_currency_keyboard(callback.message.reply_markup, res))
    await FSMFastConversion.setting_to_currencies.set()



def init(dp: Dispatcher):
    dp.register_message_handler(process_start_command,
                            commands='start')

    dp.register_callback_query_handler(process_set_from,
                            state=FSMFastConversion.set_from_currency)

    dp.register_callback_query_handler(process_set_to,
                            state=FSMFastConversion.setting_to_currencies)