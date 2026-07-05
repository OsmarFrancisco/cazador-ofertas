import requests

URL = "https://api.bsale.io/v1/products"


def guardar():

    productos = []

    try:

        r = requests.get("https://api.mercadolibre.com/sites/MPE/search?q=mouse&limit=20")

        data = r.json()

        for p in data.get("results", []):

            productos.append({
                "titulo": p.get("title", "")[:120],
                "precio": f"S/ {p.get('price', 0)}",
                "tienda": "Oechsle",
                "ubicacion": "Huancayo",
                "imagen": p.get("thumbnail", ""),
                "link": p.get("permalink", "")
            })

    except:
        pass

    return productos