import requests

URL = "https://simple.ripley.com.pe/api/v2/products"


def guardar():

    productos = []

    try:

        params = {
            "query": "mouse",
            "page": 1
        }

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(URL, params=params, headers=headers, timeout=20)

        print("Estado API Ripley:", r.status_code)

        data = r.json()

        items = data.get("data", [])

        print("Productos API Ripley:", len(items))

        for p in items:

            nombre = p.get("name", "Sin nombre")
            precio = p.get("price", 0)

            imagen = ""
            if p.get("images"):
                imagen = p["images"][0]

            link = p.get("url", "")

            productos.append({
                "titulo": nombre[:120],
                "precio": f"S/ {precio}",
                "tienda": "Ripley Perú",
                "ubicacion": "Huancayo",
                "imagen": imagen,
                "link": link
            })

    except Exception as e:

        print("Error API Ripley:", e)

    print("Ripley guardadas:", len(productos))

    return productos

if __name__ == "__main__":
    guardar()