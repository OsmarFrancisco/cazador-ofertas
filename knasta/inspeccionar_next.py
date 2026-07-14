import requests
import json

url = "https://knasta.pe/?q=Samsung%20Galaxy%20S24%20FE"

html = requests.get(url).text

inicio = html.find('<script id="__NEXT_DATA__"')

inicio_json = html.find(">", inicio) + 1
fin_json = html.find("</script>", inicio_json)

contenido = html[inicio_json:fin_json]

data = json.loads(contenido)

initial = data["props"]["pageProps"]["initialData"]

print("\nCLAVES DE initialData:\n")

for k, v in initial.items():
    print("=" * 50)
    print(k)
    print(type(v).__name__)

    if isinstance(v, list):
        print("cantidad:", len(v))
        if len(v):
            print("primer elemento:")
            print(v[0])

    elif isinstance(v, dict):
        print("keys:")
        print(v.keys())