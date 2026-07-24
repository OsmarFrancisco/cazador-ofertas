from playwright.sync_api import sync_playwright


def obtener_promart():

    productos = []


    url = "https://www.promart.pe/tecnologia"


    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )


            page = browser.new_page()


            page.goto(
                url,
                wait_until="networkidle",
                timeout=60000
            )


            page.wait_for_timeout(8000)


            cards = page.locator(".product")


            print(
                "Promart encontrados:",
                cards.count()
            )


            for i in range(cards.count()):

                try:

                    card = cards.nth(i)


                    nombre = card.locator(
                        ".item__productName"
                    ).inner_text()


                    marca = card.locator(
                        ".item__brand"
                    ).inner_text()

                    sku = card.locator(
                    ".item__sku"
                    ).inner_text()


                    precio_texto = card.locator(
                        ".bestPrice"
                    ).inner_text()

                    descuento = ""

                    texto_card = card.inner_text()


                    if "%" in texto_card:

                        palabras = texto_card.split()

                        for palabra in palabras:

                            if "%" in palabra:

                                descuento = palabra

                                break

                    precio_limpio = (
                        precio_texto
                        .replace("s/", "")
                        .replace("S/", "")
                        .replace("\n", " ")
                        .strip()
                    )


                    precio_numero = precio_limpio.split()[0]


                    link = card.locator(
                        "a.item__imagen"
                    ).get_attribute(
                        "href"
                    )


                    imagen = card.locator(
                        ".item__imagen img"
                    ).first.get_attribute(
                        "src"
                    )


                    productos.append({

                        "titulo": nombre.strip(),

                        "producto": nombre.strip(),

                        "marca": marca.strip(),

                        "sku": sku.strip(),

                        "precio": precio_numero,

                        "descuento_tienda": descuento,

                        "tienda": "Promart",

                        "link": link,

                        "imagen": imagen

                    })


                except Exception as e:

                    continue


            browser.close()


    except Exception as e:

        print(
            "Error Promart:",
            e
        )


    return productos