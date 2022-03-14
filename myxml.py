import urllib

url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=EUR&date=20200302'

usock = urllib.urlopen(url)
xmldoc = minidom.parse(usock)
usock.close()
print(xmldoc.toxml())
