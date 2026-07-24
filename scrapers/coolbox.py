from playwright.sync_api import sync_playwright
import re


URL = "https://www.coolbox.pe/tecnologia"


def limpiar_precio(texto):

    if not texto:
        return ""

    texto = (
        texto
        .replace("S/", "")
        .replace(",", "")
        .replace(" ", "")
        .strip()
    )

    numeros = re.findall(r"\d+\.\d+|\d+", texto)

    if numeros:
        return numeros[0]

    return ""


def guardar():

    productos_final = []


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


        page.wait_for_timeout(5000)


        productos = page.locator(
            ".vtex-product-summary-2-x-container"
        )


        print(
            "Coolbox encontrados:",
            productos.count()
        )


        for i in range(productos.count()):

            try:

                producto = productos.nth(i)


                titulo = producto.locator(
                    ".vtex-product-summary-2-x-productNameContainer"
                ).inner_text()


                marca = producto.locator(
                    ".vtex-store-components-3-x-productBrandName"
                ).inner_text()


                link = producto.locator(
                    "a.vtex-product-summary-2-x-clearLink"
                ).get_attribute(
                    "href"
                )


                imagen = producto.locator(
                    "img"
                ).first.get_attribute(
                    "src"
                )


                precio = ""

                precio_actual = producto.locator(
                    ".vtex-product-price-1-x-sellingPriceValue"
                )

                if precio_actual.count():

                    precio = limpiar_precio(
                        precio_actual.inner_text()
                    )


                precio_anterior = ""

                precio_viejo = producto.locator(
                    ".vtex-product-price-1-x-listPriceValue"
                )

                if precio_viejo.count():

                    precio_anterior = limpiar_precio(
                        precio_viejo.inner_text()
                    )


                descuento = ""

                ahorro = producto.locator(
                    ".vtex-product-price-1-x-savings"
                )

                if ahorro.count():

                    descuento = ahorro.inner_text()



                if link:

                    if link.startswith("/"):

                        link = (
                            "https://www.coolbox.pe"
                            +
                            link
                        )


                productos_final.append(

                    {
                        "titulo": titulo.strip(),

                        "marca": marca.strip(),

                        "sku": "",

                        "precio": precio,

                        "precio_anterior": precio_anterior,

                        "descuento_tienda": descuento.strip(),

                        "tienda": "Coolbox",

                        "link": link,

                        "imagen": imagen

                    }

                )


            except Exception as e:

                print(
                    "Error producto",
                    i,
                    e
                )


        browser.close()


    return productos_final