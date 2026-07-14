from playwright.sync_api import sync_playwright


URL = "https://knasta.pe/detail/oechsle/1001868742/iphone-15-plus-256gb-blue-condicion-excelente-a2847?q=iPhone+15"


with sync_playwright() as p:

    browser = p.chromium.launch(headless=True)

    page = browser.new_page()

    page.goto(
        URL,
        wait_until="networkidle",
        timeout=60000
    )


    scripts = page.locator("script")


    for i in range(scripts.count()):

        texto = scripts.nth(i).inner_text()


        if "initialData" in texto:

            print("SCRIPT ENCONTRADO")


            for palabra in [
                "best_variation_price",
                "last_variation_price",
                "current_price"
            ]:

                posicion = texto.find(palabra)


                print("\n================")
                print("BUSCANDO:", palabra)
                print("POSICION:", posicion)
                print("================")


                if posicion != -1:

                    inicio = posicion - 150
                    fin = posicion + 300

                    print(
                        texto[inicio:fin]
                    )


            break


    browser.close()