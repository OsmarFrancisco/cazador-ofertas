import requests
from bs4 import BeautifulSoup


def buscar_mercado_libre():

    url = "https://listado.mercadolibre.com.pe/laptop"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }


    respuesta = requests.get(
        url,
        headers=headers
    )


    sopa = BeautifulSoup(
        respuesta.text,
        "html.parser"
    )


    productos = []


    items = sopa.select(
        "li.ui-search-layout__item"
    )


    for item in items[:5]:

        titulo = item.select_one(
            "h2"
        )

        precio = item.select_one(
            "span.andes-money-amount__fraction"
        )


        if titulo and precio:

            productos.append(
                {
                    "producto": titulo.text,
                    "precio": "S/" + precio.text,
                    "tienda": "Mercado Libre"
                }
            )


    return productos