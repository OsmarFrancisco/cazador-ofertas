import requests


urls = [

    "https://knasta.pe/search?q=Samsung",
    "https://knasta.pe/buscar?q=Samsung",
    "https://knasta.pe/?q=Samsung"

]


for url in urls:

    print("\n================")
    print(url)

    r = requests.get(url)

    print("Estado:", r.status_code)

    texto = r.text.lower()

    if "samsung" in texto:

        print("✅ contiene samsung")

    else:

        print("❌ no contiene samsung")
