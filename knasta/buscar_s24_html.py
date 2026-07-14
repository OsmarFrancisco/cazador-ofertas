import requests


url = "https://knasta.pe"

html = requests.get(url).text


palabra = "Samsung"


if palabra.lower() in html.lower():
    print("ENCONTRADO")
else:
    print("NO ESTA")

