
# initial currencies 
AMD_CODE = 'amd'
RUB_CODE = 'rub'
USD_CODE =' rub'
EUR_CODE = 'eur'
GEL_CODE = 'gel'
TRY_CODE = 'try'



class Currency:
    def __init__(self, name: str, currencyCode:str):
        self.name = name
        self.curryncyCode = currencyCode
    
def createInitalCurrenciesList():
    return [Currency('Армянский драм', AMD_CODE), Currency('Российский рубль', RUB_CODE), 
              Currency('Американский доллар', USD_CODE), Currency('Евро', EUR_CODE), Currency('Турецкая лира', TRY_CODE)]
