import requests
import re


producto = "Samsung Galaxy S24 FE"


url = "https://knasta.pe/?q=" + producto.replace(" ", "%20")


print("URL:")
print(url)


html = requests.get(url).text


print("\nLONGITUD HTML:")
print(len(html))


# Buscar enlaces detail

patron = r'/detail/[a-zA-Z0-9_\-/]+'


resultados = re.findall(
    patron,
    html
)


print("\nDETALLES ENCONTRADOS:")


vistos = set()


for r in resultados:

    if r not in vistos:

        vistos.add(r)

        print(r)


print("\nTOTAL:")
print(len(vistos))