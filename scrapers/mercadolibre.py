from playwright.sync_api import sync_playwright
import re


URL = "https://listado.mercadolibre.com.pe/mouse"


def guardar():

    productos = []

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True,
                args=[
                    "--disable-blink-features=AutomationControlled"
                ]
            )


            context = browser.new_context(
                viewport={"width":1366,"height":768},
                locale="es-PE",
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/137 Safari/537.36"
            )


            page = context.new_page()


            page.goto(
                URL,
                wait_until="domcontentloaded",
                timeout=90000
            )


            page.wait_for_timeout(10000)



            print(
                "Mercado Libre titulo:",
                page.title()
            )


            # captura por si cambia algo
            try:

                page.screenshot(
                    path="mercadolibre_debug.png",
                    full_page=True
                )

            except:

                pass



            # varios selectores posibles

            selectores = [

                "li.ui-search-layout__item",

                "div.poly-card",

                "li[class*='ui-search-layout__item']",

                "div.ui-search-result"

            ]


            cards = None


            for selector in selectores:

                cantidad = page.locator(
                    selector
                ).count()


                if cantidad > 0:

                    print(
                        "Selector encontrado:",
                        selector,
                        cantidad
                    )

                    cards = page.locator(
                        selector
                    )

                    break



            if cards is None:

                print(
                    "Mercado Libre no encontró tarjetas"
                )

                browser.close()

                return []



            cantidad = cards.count()


            print(
                "Mercado Libre cards:",
                cantidad
            )



            for i in range(min(cantidad,50)):


                try:

                    card = cards.nth(i)



                    texto_card = card.inner_text(
                        timeout=3000
                    )


                    if not texto_card:

                        continue




                    # TITULO

                    titulo = ""


                    for selector in [

                        "a.poly-component__title",

                        "h3",

                        ".poly-component__title",

                        ".ui-search-item__title"

                    ]:


                        try:

                            titulo = card.locator(
                                selector
                            ).first.inner_text(
                                timeout=1500
                            ).strip()


                            if titulo:

                                break


                        except:

                            pass



                    if not titulo:

                        continue





                    # PRECIO

                    precio = "Consultar"



                    encontrados = re.findall(

                        r'S\/\s?[\d\.,]+',

                        texto_card

                    )


                    if encontrados:

                        precio = encontrados[0]




                    # IMAGEN

                    imagen = ""


                    try:

                        img = card.locator(
                            "img"
                        ).first


                        for atributo in [

                            "src",

                            "data-src",

                            "data-lazy"

                        ]:


                            valor = img.get_attribute(
                                atributo
                            )


                            if valor:

                                imagen = valor

                                break


                    except:

                        pass





                    # LINK

                    link = ""


                    try:

                        link = card.locator(
                            "a"
                        ).first.get_attribute(
                            "href"
                        ) or ""


                    except:

                        pass




                    productos.append({

                        "titulo": titulo[:120],

                        "precio": precio,

                        "tienda": "Mercado Libre",

                        "ubicacion": "Huancayo",

                        "imagen": imagen,

                        "link": link

                    })



                except:

                    continue




            browser.close()



    except Exception as e:

        print(
            "Error Mercado Libre:",
            e
        )



    print(
        "Mercado Libre encontrados:",
        len(productos)
    )


    return productos