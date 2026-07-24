from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://www.coolbox.pe/celulares",
        wait_until="domcontentloaded",
        timeout=60000
    )

    page.wait_for_timeout(6000)

    print("BUSCANDO TARJETAS...\n")

    posibles = [

        "article",

        ".product-item",

        ".product",

        ".product-card",

        ".productCard",

        ".vtex-product-summary-2-x-container",

        ".vtex-search-result-3-x-galleryItem",

        "li",

        "[data-testid='product-card']"

    ]

    for selector in posibles:

        try:

            cantidad = page.locator(selector).count()
            print(selector, "->", cantidad)

        except Exception:
            pass

    print("\nBUSCANDO PRODUCTOS\n")

    productos = page.locator(".vtex-product-summary-2-x-container")

    print("Productos encontrados:", productos.count())

    print("\nBUSCANDO PRECIOS COOLBOX\n")

    primera = productos.first

    print(
        primera.inner_text()
    )


    print("\nCLASES DE PRECIO\n")

    html = primera.inner_html()

    for palabra in [
        "sellingPrice",
        "listPrice",
        "savings",
        "discount",
        "price"
    ]:

        if palabra in html:
            print("ENCONTRADO:", palabra)

    primer = productos.nth(0)

    print("\n====================")
    print(primer.inner_text())

    with open(
        "coolbox_producto_0.html",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            primer.inner_html()
        )

    print("\nHTML guardado.")
    browser.close()
