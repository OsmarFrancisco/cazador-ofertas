"""
knasta_buscar.py

Lee una página de Knasta y extrae:

- current_price
- last_variation_price
- best_variation_price
- dprices

No modifica ningún archivo.
Solo devuelve información.
"""

import json
import re
import requests


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/138.0 Safari/537.36"
    )
}


def extraer_numero(html, campo):
    """
    Extrae un número o None.

    Ejemplo:

    "current_price":1899

    devuelve:

    1899
    """

    patron = rf'"{campo}":(null|\d+)'

    m = re.search(patron, html)

    if not m:
        return None

    valor = m.group(1)

    if valor == "null":
        return None

    return int(valor)


def extraer_dprices(html):
    """
    Extrae el arreglo dprices.
    """

    inicio = html.find('"dprices":[')

    if inicio == -1:
        return []

    inicio = html.find("[", inicio)

    if inicio == -1:
        return []

    contador = 0

    fin = inicio

    while fin < len(html):

        if html[fin] == "[":
            contador += 1

        elif html[fin] == "]":
            contador -= 1

            if contador == 0:
                break

        fin += 1

    bloque = html[inicio:fin + 1]

    try:
        return json.loads(bloque)

    except Exception:
        return []


def obtener_datos_knasta(url):

    try:

        r = requests.get(
            url,
            headers=HEADERS,
            timeout=20
        )

        r.raise_for_status()

    except Exception as e:

        return {
            "ok": False,
            "error": str(e)
        }

    html = r.text

    return {

        "ok": True,

        "current_price":
            extraer_numero(
                html,
                "current_price"
            ),

        "last_variation_price":
            extraer_numero(
                html,
                "last_variation_price"
            ),

        "best_variation_price":
            extraer_numero(
                html,
                "best_variation_price"
            ),

        "dprices":
            extraer_dprices(html)

    }


if __name__ == "__main__":

    URL = (
        "https://knasta.pe/detail/plazavea/20472497/"
        "smartphone-samsung-galaxy-s24-fe-67-8gb-128gb-50mp-12mp-8mp-negro?q=Samsung+Galaxy+S24"
    )

    from pprint import pprint

    pprint(
        obtener_datos_knasta(URL)
    )