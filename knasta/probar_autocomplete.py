import requests
import re


url = "https://knasta.pe"


html = requests.get(url).text


print("Buscando autocomplete...")


pos = html.find("autocomplete")


if pos != -1:

    print("ENCONTRADO")
    print()

    print(
        html[pos-300:pos+500]
    )

else:

    print("No encontrado")