from playwright.sync_api import sync_playwright


URL = "https://www.falabella.com.pe/falabella-pe/search?Ntt=mouse"


def guardar():

    productos = []

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )

            page = browser.new_page()

            page.goto(
                URL,
                wait_until="domcontentloaded",
                timeout=60000
            )

            page.wait_for_timeout(7000)


            cards = page.locator(
                "a.pod-link"
            )


            cantidad = cards.count()

            print(
                "Productos Falabella detectados:",
                cantidad
            )


            for i in range(min(cantidad,100)):

                try:

                    card = cards.nth(i)

                    texto = card.inner_text(
                        timeout=3000
                    )


                    if "S/" not in texto:
                        continue


                    partes = texto.split("\n")


                    partes = [
                        x.strip()
                        for x in partes
                        if x.strip()
                    ]


                    titulo = " ".join(
                        partes[:4]
                    )


                    precio = "Consultar"


                    for x in partes:

                        if "S/" in x:

                            precio = x
                            break



                    imagen = ""

                    try:

                        imagen = card.locator(
                            "img"
                        ).first.get_attribute(
                            "src",
                            timeout=2000
                        )

                    except:

                        pass



                    link = ""

                    try:

                        link = card.get_attribute(
                            "href"
                        )

                    except:

                        pass



                    if link and not link.startswith("http"):

                        link = (
                            "https://www.falabella.com.pe"
                            + link
                        )


                    productos.append({

                        "titulo": titulo[:120],

                        "precio": precio,

                        "tienda": "Falabella Perú",

                        "ubicacion": "Huancayo",

                        "imagen": imagen,

                        "link": link

                    })



                    print(
                        "✔",
                        len(productos),
                        titulo[:35]
                    )


                except:

                    continue



            browser.close()



    except Exception as e:

        print(
            "Error Falabella:",
            e
        )



    print(
        "Falabella encontradas:",
        len(productos)
    )


    return productos