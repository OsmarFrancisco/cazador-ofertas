from playwright.sync_api import sync_playwright

URL = "https://www.tottus.com.pe/tottus-pe/buscar?Ntt=iphone"

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(URL)

    page.wait_for_timeout(8000)

    with open("tottus_debug.html","w",encoding="utf-8") as f:
        f.write(page.content())

    print(page.title())

    print("HTML guardado")

    input("ENTER")

    browser.close()