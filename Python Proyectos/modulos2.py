#from urllib.request import urlopen
#page = urlopen("http://info.cern.ch/")
#content = page.read()
#print(content)

import requests
currency = "eur"
basecurrency = "usd"

url = "http://freecurrencyrates.com/api/action.php?do=cvals&iso=" + currency + "&f=" + basecurrency + "&v=1&s=cbr"

resp = requests.get(url)
print(resp.text)
print(resp.json())