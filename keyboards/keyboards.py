from aiogram.types import  InlineKeyboardButton, InlineKeyboardMarkup

import emoji
from  currency_support import * 


def create_button(cur: Currency)->InlineKeyboardButton:
    return InlineKeyboardButton(text=emoji.emojize(cur.name+' ' + cur.emoji), callback_data=cur.curryncyCode)

def make_currency_keyboard(excluded = list()) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width = 2)
    [markup.insert(create_button(item)) for item in createInital_currencies_list() if item.curryncyCode not in excluded]
    return markup

def update_currency_keyboard(markup: InlineKeyboardMarkup, selecteed: str) -> InlineKeyboardMarkup:
    for line in markup.inline_keyboard:
        for button in line:
            if button.callback_data  == selecteed:
                button.text = button.text + emoji.emojize(':green_circle:')
                return markup
    return markup

def add_menu(markup: InlineKeyboardMarkup) -> InlineKeyboardMarkup:
    acceptButton = InlineKeyboardButton(text=emoji.emojize("Принять"+':check_mark_button:'), callback_data="accept")
    cancelButton = InlineKeyboardButton(text=emoji.emojize("Отменить"+':cross_mark:'), callback_data="cancel")
    backButton = InlineKeyboardButton(text=emoji.emojize("Назад"+':BACK_arrow:'), callback_data="back")
    markup.row(acceptButton, cancelButton, backButton)
    return markup