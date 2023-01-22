import requests

myCurrency = ['amd', 'rub', 'usd', 'eur']


class CurrencyApi:        
    def pair(first: str, second: str) -> str:
        pass
    
    def allCurrecy(self):
        pass  
    


def allCurrencyApi():
    response = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json')
    return response.json()


def one(cur: str):
    response = requests.get(f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{cur}.json')
    return response.json()
   
def allCurrency():
    response = allCurrencyApi()
    for cur in myCurrency:
        if cur in response:
            print(cur, response[cur])
 
 
def oneCur(cur: str):
    response = one(cur)
    for cur_item in myCurrency:
        if cur_item in response[cur]:
            print(cur, cur_item, response[cur][cur_item])



command = ""
while command != "end":
    command = input()
    if command == "all":
       allCurrency()
    elif command in myCurrency:
        oneCur(command)
    elif command == 'alll':
        print(allCurrencyApi())
    
        