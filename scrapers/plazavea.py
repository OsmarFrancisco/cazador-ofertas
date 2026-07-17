from playwright.sync_api import sync_playwright


URL = "https://www.plazavea.com.pe/tecnologia/televisores/lg"


def guardar():

    productos = []


    with sync_playwright() as p:


        browser = p.chromium.launch(
            headless=False
        )


        page = browser.new_page()


        print("Entrando a PlazaVea...")


        page.goto(
            URL,
            wait_until="networkidle",
            timeout=120000
        )


        page.wait_for_timeout(5000)


        print("TITULO PAGINA:")
        print(page.title())


        tarjetas = page.locator(
            "div.Showcase.ga-product-item"
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
                    ".Showcase__name"
                ).inner_text()

            except:

                titulo = ""


            try:

                precio = tarjeta.get_attribute(
                    "data-ga-price"
                )

            except:

                precio = ""


            try:

                vendedor = tarjeta.locator(
                    ".Showcase__SellerName"
                ).inner_text()

            except:

                vendedor = ""


            try:

                imagen = tarjeta.locator(
                    ".showcase__image"
                ).get_attribute(
                    "src"
                )

            except:

                imagen = ""


            try:

                sku = tarjeta.get_attribute(
                    "data-sku"
                )

            except:

                sku = ""


            try:

                link = tarjeta.locator(
                    "a"
                ).first.get_attribute(
                    "href"
                )

            except:

                link = ""


            if link and link.startswith("/"):

                link = (
                    "https://www.plazavea.com.pe"
                    + link
                )


            print("-----------------------------")

            print(titulo)

            print(precio)

            print(vendedor)


            productos.append({

            "titulo": titulo,

            "precio": precio,

            "tienda": "PlazaVea",

            "imagen": imagen,

            "link": link,

            "sku": sku,

            "vendedor": vendedor,

            "marca": "LG",

            "categoria": "Televisores"

        })


        browser.close()


    return productos



if __name__ == "__main__":

    guardar()