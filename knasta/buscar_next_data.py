import requests
import re


url = "https://knasta.pe/?q=Samsung%20Galaxy%20S24%20FE"


html = requests.get(url).text


print("Buscando NEXT_DATA...")


if "__NEXT_DATA__" in html:

    print("✅ Encontrado NEXT_DATA")


else:

    print("❌ No encontrado")


print("\nBuscando Samsung dentro del JSON...")


pos = html.find("Samsung")


if pos != -1:

    print("Encontrado posición:", pos)

    print("\n====================")

    print(
        html[pos-300:pos+500]
    )

else:

    print("Samsung no aparece")
