import requests
import xmltodict

date = str('20200302')
def myxml(date):
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date='+date
    response = requests.get(url)
    data = xmltodict.parse(response.content)

    print(data['exchange']['currency']['txt'])
    print(data['exchange']['currency']['rate'])
    print(data['exchange']['currency']['cc'])
    print(data['exchange']['currency']['exchangedate'])

myxml(date)