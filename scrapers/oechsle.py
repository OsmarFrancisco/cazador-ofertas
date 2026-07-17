from playwright.sync_api import sync_playwright

URL = "https://www.oechsle.pe/tecnologia/telefonia/celulares"


def guardar():

    productos = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page()

        print("Entrando a Oechsle...")

        page.goto(
            URL,
            wait_until="networkidle",
            timeout=120000
        )

        page.wait_for_timeout(5000)

        tarjetas = page.locator("div.resultItem")

        total = tarjetas.count()

        print("Productos encontrados:", total)

        for i in range(tarjetas.count()):

            tarjeta = tarjetas.nth(i)

            titulo = tarjeta.locator(
                ".resultItem__detail--name"
            ).inner_text()

            precio = tarjeta.locator(
                ".resultItem__detail--price .value"
            ).first.inner_text()

            try:
                titulo = tarjeta.locator(
                    "img.resultItem__image"
                ).get_attribute("alt")
            except:
                titulo = ""

            try:
                precio = tarjeta.locator(
                    "span.value"
                ).first.inner_text()
            except:
                precio = ""

            try:

                link = tarjeta.locator(
                    "a.resultItem__link"
                ).first.get_attribute("href")

                if link:
                    link = "https://www.oechsle.pe" + link

            except:

                link = ""

            try:
                imagen = tarjeta.locator(
                    "img.resultItem__image"
                ).get_attribute("src")
            except:
                imagen = ""
           
            

            productos.append({

                "titulo": titulo,

                "precio": precio,

                "tienda": "Oechsle",

                "imagen": imagen,

                "link": link

            })

        browser.close()

    return productos


if __name__ == "__main__":

    datos = guardar()

    for p in datos:

        print("--------------------------------")
        print(p["titulo"])
        print(p["precio"])
        print(p["link"])