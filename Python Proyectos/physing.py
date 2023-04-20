import requests

link = "http://info.cern.ch/"
r = requests.get(link)
print(r.status_code)

html = r.text
print(html)
html2 = html.replace(".ch", ".eus").replace("home", "casa").replace("line", "linea")
print(html2)