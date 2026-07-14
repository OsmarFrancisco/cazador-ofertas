import requests


url = "https://knasta.pe"

html = requests.get(url).text


palabra = "Samsung"

posicion = html.lower().find(palabra.lower())


if posicion == -1:

    print("No encontrado")

else:

    print("Encontrado en posicion:", posicion)

    inicio = max(0, posicion - 500)
    fin = posicion + 1000

    print("\n========== FRAGMENTO ==========\n")

    print(html[inicio:fin])
