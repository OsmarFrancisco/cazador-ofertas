import requests
import json
import re


busqueda = "Samsung Galaxy S24 FE"


url = "https://knasta.pe/?q=" + busqueda.replace(" ", "%20")


html = requests.get(url).text


# Buscar NEXT_DATA

inicio = html.find('<script id="__NEXT_DATA__"')

if inicio == -1:
    print("No existe NEXT_DATA")
    exit()


inicio_json = html.find(">", inicio) + 1
fin_json = html.find("</script>", inicio_json)


contenido = html[inicio_json:fin_json]


data = json.loads(contenido)


print("NEXT_DATA cargado correctamente")


texto = json.dumps(data, ensure_ascii=False)


# Buscar productos

patron = r'https://knasta\.pe/detail/[^\"]+'


urls = re.findall(
    patron,
    texto
)


vistos = set()


print("\nPRODUCTOS ENCONTRADOS:\n")


for u in urls:

    if u not in vistos:

        vistos.add(u)
        print(u)


print("\nTOTAL:")
print(len(vistos))