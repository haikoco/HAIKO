import re  
import requests  
import json  
  
  
URL = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'  
  
  
def load_exchange():  
    return json.loads(requests.get(URL).text)  
  
  
def get_exchange(CurrencyCodeL_key):  
    for exc in load_exchange():  
        if CurrencyCodeL_key == exc['CurrencyCodeL']:  
            return exc  
    return False  
  
  
def get_exchanges(CurrencyCodeL_pattern):  
    result = []  
    CurrencyCodeL_pattern = re.escape(CurrencyCodeL_pattern) + '.*'  
    for exc in load_exchange():  
        if re.match(CurrencyCodeL_pattern, exc['CurrencyCodeL'], re.IGNORECASE) is not None:  
            result.append(exc)  
    return result
