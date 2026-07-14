import requests
import re


url = "https://knasta.pe"


headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "Chrome/138 Safari/537.36"
    )
}


r = requests.get(
    url,
    headers=headers,
    timeout=20
)


html = r.text


print("Estado:", r.status_code)


patrones = [
    r'\/[a-zA-Z0-9_\-/]*search[a-zA-Z0-9_\-/]*',
    r'\/[a-zA-Z0-9_\-/]*detail[a-zA-Z0-9_\-/]*',
    r'\/[a-zA-Z0-9_\-/]*product[a-zA-Z0-9_\-/]*',
    r'\/[a-zA-Z0-9_\-/]*autocomplete[a-zA-Z0-9_\-/]*'
]


for patron in patrones:

    print("\nPATRON:", patron)

    encontrados = re.findall(
        patron,
        html
    )

    for e in encontrados[:20]:
        print(e)