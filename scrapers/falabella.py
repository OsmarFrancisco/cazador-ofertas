from playwright.sync_api import sync_playwright


BUSQUEDAS = [
    "televisor smart tv",
    "iphone",
    "samsung galaxy",
    "laptop",
    "ps5",
    "tablet"
]


def guardar():

    productos = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        for busqueda in BUSQUEDAS:

            print(f"\n🔎 Falabella buscando: {busqueda}")

            url = (
                "https://www.falabella.com.pe/falabella-pe/search?Ntt="
                + busqueda.replace(" ", "%20")
            )

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=20000
            )

            page.wait_for_timeout(2000)

            cards = page.locator("a.pod-link")

            cantidad = cards.count()

            print(
                "Productos encontrados:",
                cantidad
            )


            for i in range(min(cantidad, 30)):

                print(
                    f"   Leyendo producto {i+1}/{cantidad}"
                )

                try:

                    print("      paso A")

                    card = cards.nth(i)

                    print("      paso B")

                    link = card.get_attribute("href")

                    print("      paso C")


                    if link and not link.startswith("http"):

                        link = (
                            "https://www.falabella.com.pe"
                            + link
                        )


                    texto = card.inner_text(
                        timeout=3000
                    )

                    print("      paso D")


                    if "S/" not in texto:
                        continue


                    partes = [
                        x.strip()
                        for x in texto.split("\n")
                        if x.strip()
                    ]

                    descuento_tienda = 0

                    for parte in partes:
                        if "%" in parte:

                            try:
                                descuento_tienda = abs(
                                    int(
                                        parte.replace("%","")
                                             .replace("-","")
                                    )
                                )
                            except:
                                descuento_tienda = 0                 


                    productos.append({

                        "titulo": " ".join(partes[:4]),

                        "precio": next(
                            (
                                x for x in partes
                                if "S/" in x
                            ),
                            "Consultar"
                        ),

                        "descuento_tienda": descuento_tienda,

                        "tienda": "Falabella Perú",

                        "ubicacion": "Huancayo",

                        "imagen": "",

                        "link": link or ""

                    })


                except Exception as e:

                    print(
                        "ERROR producto:",
                        i,
                        e
                    )

                    continue


        browser.close()


    print(
        "Falabella encontradas:",
        len(productos)
    )


    return productos