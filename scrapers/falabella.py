from playwright.sync_api import sync_playwright


BUSQUEDAS = [
    "televisor smart tv",
    "iphone",
    "samsung galaxy",
    "laptop",
    "ps5",
    "tablet"
]


def guardar():

    productos = []

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=True
            )
      

            for busqueda in BUSQUEDAS:
                
                page = browser.new_page()   

                print(f"\n🔎 Falabella buscando: {busqueda}")

                url = (
                    "https://www.falabella.com.pe/falabella-pe/search?Ntt="
                    + busqueda.replace(" ", "%20")
                )

                page.goto(
                    url,
                    wait_until="domcontentloaded",
                    timeout=20000
                )

                page.wait_for_timeout(1500)

                cards = page.locator(
                    "a.pod-link"
                )

                cantidad = cards.count()

                print(
                    "Productos encontrados:",
                    cantidad
                )

                for i in range(min(cantidad, 30)):

                    try:
                        
                        print(f"   Leyendo producto {i+1}/{cantidad}")

                        card_html = cards.nth(i).evaluate(
                            "(el)=>el.innerHTML"
                        )                                               

                        texto = cards.nth(i).inner_text(
                            timeout=1000
                        )

                        if "S/" not in texto:
                            continue

                        partes = [
                            x.strip()
                            for x in texto.split("\n")
                            if x.strip()
                        ]

                        titulo = " ".join(
                            partes[:4]
                        )

                        precio = "Consultar"

                        for x in partes:

                            if "S/" in x:

                                precio = x

                                break

                        imagen = ""

                        try:

                            img = card.locator("img").first

                            imagen = (
                                img.get_attribute("src")
                                or img.get_attribute("data-src")
                                or ""
                            )

                        except:

                            pass

                        link = ""

                        try:

                            link = card.get_attribute("href")

                        except:

                            pass

                        if link and not link.startswith("http"):

                            link = (
                                "https://www.falabella.com.pe"
                                + link
                            )

                        productos.append({

                            "titulo": titulo[:120],

                            "precio": precio,

                            "tienda": "Falabella Perú",

                            "ubicacion": "Huancayo",

                            "imagen": imagen,

                            "link": link

                        })

                    except:

                        continue

                              
                page.close()
                                
            browser.close()

    except Exception as e:

        print(
            "Error Falabella:",
            e
        )

    # ===========================
    # ELIMINAR DUPLICADOS
    # ===========================

    unicos = {}

    for producto in productos:

        clave = producto.get(
            "link",
            ""
        )

        if not clave:

            clave = producto.get(
                "titulo",
                ""
            ).lower()

        if clave not in unicos:

            unicos[clave] = producto

    productos = list(
        unicos.values()
    )

    print(
        "Falabella encontradas:",
        len(productos)
    )

    return productos