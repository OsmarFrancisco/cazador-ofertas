import requests
import json


def buscar_producto_knasta(nombre):

    url = (
        "https://knasta.pe/?q="
        + nombre.replace(" ", "%20")
    )

    html = requests.get(url).text


    inicio = html.find(
        '<script id="__NEXT_DATA__"'
    )

    if inicio == -1:
        return []


    inicio_json = html.find(">", inicio) + 1

    fin_json = html.find(
        "</script>",
        inicio_json
    )


    contenido = html[
        inicio_json:fin_json
    ]


    data = json.loads(contenido)


    initial = (
        data["props"]
        ["pageProps"]
        ["initialData"]
    )


    productos = []


    # sections
    for seccion in initial.get(
        "sections",
        []
    ):

        for p in seccion.get(
            "items",
            []
        ):

            productos.append(p)


    # otras listas de Knasta

    for bloque in [
        "bestpricesection",
        "mostviewed",
        "best7"
    ]:

        for p in initial.get(
            bloque,
            []
        ):

            productos.append(p)



    # eliminar duplicados

    vistos = set()

    resultado = []


    for p in productos:

        pid = p.get(
            "kid"
        )

        if pid not in vistos:

            vistos.add(pid)

            resultado.append(p)


    return resultado



if __name__ == "__main__":


    resultados = buscar_producto_knasta(
        "Samsung Galaxy S24 FE"
    )


    print(
        "TOTAL:",
        len(resultados)
    )


    for p in resultados[:20]:

        print("----------------")
        print(
            p.get("title")
        )

        print(
            p.get("retail_label")
        )

        print(
            p.get("current_price")
        )

        print(
            p.get("url")
        )