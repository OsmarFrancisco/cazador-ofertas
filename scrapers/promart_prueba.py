from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()


    page.goto(
        "https://www.promart.pe/tecnologia",
        wait_until="networkidle",
        timeout=60000
    )


    page.wait_for_timeout(8000)


    productos = page.locator(".product")


    print(
        "Productos encontrados:",
        productos.count()
    )


    for i in range(min(productos.count(),3)):

        print("\n====================")
        print("PRODUCTO", i)


        texto = productos.nth(i).inner_text()

        print(texto)


        html = productos.nth(i).inner_html()


        archivo = f"producto_{i}.html"


        with open(
            archivo,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(html)


        print("HTML guardado:", archivo)


    page.pause()