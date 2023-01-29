# initial currencies 
AMD_CODE = 'amd'
RUB_CODE = 'rub'
USD_CODE =' usd'
EUR_CODE = 'eur'
GEL_CODE = 'gel'
TRY_CODE = 'try'


class Currency:
    def __init__(self, name: str, currencyCode: str, emoji: str = ''):
        self.name = name
        self.curryncyCode = currencyCode
        self.emoji = emoji
    
def createInital_currencies_list():
    return [Currency('Армянский драм', AMD_CODE, ':Armenia:'), Currency('Российский рубль', RUB_CODE, ':skull:'), 
            Currency('Американский доллар', USD_CODE, ':United_States:'), Currency('Евро', EUR_CODE, ':European_Union:'), 
            Currency('Турецкая лира', TRY_CODE,':Turkey:'), Currency('Грузинский лари', GEL_CODE, ':Georgia:')]
