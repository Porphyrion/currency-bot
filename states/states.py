from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMFastConversion(StatesGroup):
    set_from_currency = State()
    setting_to_currencies = State()
    currencies_choosed = State()
    set_name_to_convertion_pattern = State()
    
