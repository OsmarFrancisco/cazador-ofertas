import requests
import re
import json


URL = "https://knasta.pe/detail/plazavea/20472497/smartphone-samsung-galaxy-s24-fe-67-8gb-128gb-50mp-12mp-8mp-negro?q=Samsung+Galaxy+S24"


def buscar_json(texto):

    patrones = [
        r'window\.__INITIAL_STATE__\s*=\s*(\{.*?\});',
        r'__NEXT_DATA__"\s*:\s*(\{.*?\})',
        r'current_price.*?'
    ]

    for patron in patrones:
        encontrado = re.search(
            patron,
            texto,
            re.DOTALL
        )

        if encontrado:
            return encontrado.group(1)

    return None



def probar():

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }


    print("Consultando Knasta...")

    r = requests.get(
        URL,
        headers=headers,
        timeout=20
    )


    print("STATUS:", r.status_code)

    html = r.text


    print(
        "Tamaño HTML:",
        len(html)
    )


    palabras = [
        "current_price",
        "last_variation_price",
        "best_variation_price",
        "dprices"
    ]


    for palabra in palabras:

        if palabra in html:
            print("Encontrado:", palabra)

        else:
            print("NO existe:", palabra)



    print("\nBuscando valores...")


    for palabra in palabras:

        pos = html.find(palabra)

        if pos != -1:

            inicio = pos - 200
            fin = pos + 500

            print("\n==========")
            print(html[inicio:fin])



if __name__ == "__main__":
    probar()