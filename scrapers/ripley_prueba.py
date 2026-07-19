from playwright.sync_api import sync_playwright


URL = "https://simple.ripley.com.pe/search/iphone?sort=relevance_desc&page=1"


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    print("Entrando a Ripley...")

    page.goto(
        URL,
        wait_until="domcontentloaded",
        timeout=120000
    )

    print("URL actual:")
    print(page.url)

    page.wait_for_timeout(10000)


    print("Titulo pagina:")
    print(page.title())


    tarjetas = page.locator(
        "article.product-item--wrapper"
    )


    print(
        "Productos encontrados:",
        tarjetas.count()
    )


    for i in range(
        min(tarjetas.count(),5)
    ):

        tarjeta = tarjetas.nth(i)

        try:

            titulo = tarjeta.locator(
                ".product-item--name"
            ).inner_text()

        except:

            titulo = "SIN TITULO"


        try:

            precio = tarjeta.locator(
                ".product-price-price"
            ).first.inner_text()

        except:

            precio = "SIN PRECIO"


        try:

            imagen = tarjeta.locator(
                "img.product-image-img"
            ).first.get_attribute(
                "src"
            )

        except:

            imagen = "SIN IMAGEN"


        print("----------------")
        print(titulo)
        print(precio)
        print(imagen)


    input("Presiona ENTER para cerrar...")

    browser.close()