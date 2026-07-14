"""
Prueba búsqueda automática Knasta
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def buscar_knasta(texto):

    consulta = quote(texto)

    url = f"https://knasta.pe/search?q={consulta}"

    print("Buscando:")
    print(url)

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "Chrome/138 Safari/537.36"
        )
    }

    r = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    print("Estado:", r.status_code)

    soup = BeautifulSoup(
        r.text,
        "html.parser"
    )

    enlaces = []

    for a in soup.find_all("a", href=True):

        href = a["href"]

        if "/detail/" in href:

            enlaces.append(
                "https://knasta.pe" + href
                if href.startswith("/")
                else href
            )


    return enlaces[:5]


if __name__ == "__main__":

    producto = (
        "SAMSUNG Televisor 75 UHD U8000H "
        "Falabella"
    )


    resultados = buscar_knasta(producto)


    print("\nRESULTADOS:")
    
    for r in resultados:
        print(r)