from .interface import CurrencyApiInterface
import requests

class FreeApi(CurrencyApiInterface):
    all_currencies = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json'
    from_to_rate = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{}.json'
    
    def list_of_currency(self):
        return self.all_currencies_request().keys()
    
    def get_currency_rate(self, fromCur: str, toCur: list = list()):
        rate = self.rate_request(fromCur)
        return dict((cur, rate[fromCur][cur]) for cur in rate[fromCur] if cur in toCur)
    
    def rate_request(self, fromCur: str):
        response = requests.get(self.from_to_rate.format(fromCur))
        return response.json()
    
    def all_currencies_request(self):
        response = requests.get(self.all_currencies)
        return response.json()


   
        