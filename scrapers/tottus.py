import requests
import json
import re


URL = "https://www.tottus.com.pe/tottus-pe/buscar?Ntt=iphone"


def guardar():

    productos = []

    try:

        headers = {
            "User-Agent":
            "Mozilla/5.0"
        }


        r = requests.get(
            URL,
            headers=headers,
            timeout=20
        )


        print(
            "Estado Tottus:",
            r.status_code
        )


        html = r.text


        inicio = html.find(
            '<script id="__NEXT_DATA__"'
        )


        if inicio == -1:

            print(
                "❌ No se encontró NEXT DATA"
            )

            return []


        inicio_json = html.find(
            ">",
            inicio
        ) + 1


        fin_json = html.find(
            "</script>",
            inicio_json
        )


        json_texto = html[
            inicio_json:fin_json
        ]


        data = json.loads(
            json_texto
        )


        resultados = (
            data
            ["props"]
            ["pageProps"]
            ["results"]
        )


        print(
            "Productos encontrados:",
            len(resultados)
        )


        for p in resultados:


            nombre = p.get(
                "displayName",
                ""
            )


            marca = p.get(
                "brand",
                ""
            )


            url = p.get(
                "url",
                ""
            )


            imagen = ""

            if p.get("mediaUrls"):

                imagen = p["mediaUrls"][0]


            precio = 0


            precios = p.get(
                "prices",
                []
            )


            for precio_item in precios:

                if precio_item.get(
                    "type"
                ) == "internetPrice":

                    precio = precio_item["price"][0]

                    break


            if precio == 0 and precios:

                precio = precios[0]["price"][0]



            descuento = ""

            if p.get(
                "discountBadge"
            ):

                descuento = p[
                    "discountBadge"
                ].get(
                    "label",
                    ""
                )



            productos.append({

                "titulo":
                    f"{marca} {nombre}",

                "precio":
                    f"S/ {precio}",

                "tienda":
                    "Tottus",

                "ubicacion":
                    "Huancayo",

                "imagen":
                    imagen,

                "link":
                    url,

                "descuento":
                    descuento

            })


    except Exception as e:

        print(
            "Error Tottus:",
            e
        )


    print(
        "Tottus guardados:",
        len(productos)
    )


    return productos