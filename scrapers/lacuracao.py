from playwright.sync_api import sync_playwright


URL = "https://www.lacuracao.pe/curacao/apple-celulare2.html"


def guardar():

    productos = []

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        print("Entrando a La Curacao...")

        page.goto(
            URL,
            wait_until="domcontentloaded",
            timeout=120000
        )
          
        page.wait_for_timeout(10000)

        print("TITULO PAGINA:")
        print(page.title())

        print("URL ACTUAL:")
        print(page.url)

        page.wait_for_timeout(5000)

        print("URL actual:")
        print(page.url)


        print("TITULO PAGINA:")
        print(page.title())


        print("BUSCANDO PRODUCTOS...")


        tarjetas = page.locator(
            "li.item.product.product-item"
        )


        total = tarjetas.count()


        print(
            "Productos encontrados:",
            total
        )

        for i in range(total):

            tarjeta = tarjetas.nth(i)

            try:

                titulo = tarjeta.locator(
                    ".product-item-name"
                ).inner_text()

            except:

                titulo = ""

            try:

                precio = tarjeta.locator(
                    ".price"
                ).first.inner_text()

            except:

                precio = ""

            try:

                link = tarjeta.locator(
                    "a.product-item-link"
                ).get_attribute("href")

            except:

                link = ""

            try:

                imagen = tarjeta.locator(
                    "img.product-image-photo"
                ).get_attribute("src")

            except:

                imagen = ""

            print("--------------------------------")

            print(titulo)

            print(precio)

            print(link)

            print(imagen)

            productos.append({

                "titulo": titulo,

                "precio": precio,

                "tienda": "La Curacao",

                "imagen": imagen,

                "link": link

            })

        browser.close()

    return productos


if __name__ == "__main__":

    guardar()