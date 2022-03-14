import json
import urllib.request

# download raw json object
url ='https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date=20200302&json'
data = urllib.request.urlopen(url).read().decode()

# parse json object
obj = json.loads(data)

print(obj[0])

print(obj[0].get('rate', 0))
print(obj[0].get('cc', 0))
print(obj[0].get('txt', 0))
print(obj[0].get('r030', 0))
print(obj[0].get('exchangedate', 0))