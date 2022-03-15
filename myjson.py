import json
import urllib.request
import mysqlite as mysqlite

# date = str('20220307')

def myjson(date):
    # download raw json object
    url ='https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date='+date+'&json'
    data = urllib.request.urlopen(url).read().decode()

    # parse json object
    obj = json.loads(data)

    exchangedate = obj[0].get('exchangedate', 0)
    rate = obj[0].get('rate', 0)
    mysqlite.mysqlite(exchangedate, rate)

    # print(obj[0].get('rate', 0))
    # print(obj[0].get('cc', 0))
    # print(obj[0].get('txt', 0))
    # print(obj[0].get('r030', 0))
    # print(obj[0].get('exchangedate', 0))

# myjson(date)