import requests


BUILD_ID = "248264bb79fa47c3974be0ef7caba2a2cf0a5952"


def buscar_api_knasta(texto):

    url = (
        "https://knasta.pe/_next/data/"
        + BUILD_ID
        + "/es/results.json?q="
        + texto.replace(" ", "+")
    )


    try:
        r = requests.get(
            url,
            timeout=10
        )

    except requests.exceptions.RequestException:
        print("⚠️ Error conexión Knasta")
        return []


    # print("STATUS:", r.status_code)


    if r.status_code != 200:
        return []


    data = r.json()


    initial = (
        data["pageProps"]
        ["initialData"]
    )


    productos = initial.get(
        "products",
        []
    )


    return productos



if __name__ == "__main__":


    resultados = buscar_api_knasta(
        "Samsung Galaxy S24 FE"
    )


    print(
        "TOTAL:",
        len(resultados)
    )


    for p in resultados[:10]:

        print("----------------")
        print(
            p.get("title")
        )

        print(
            p.get("retail_label")
        )

        print(
            p.get("url")
        )