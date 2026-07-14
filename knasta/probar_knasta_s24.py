from knasta.buscar_api_knasta import buscar_api_knasta


busqueda = "Samsung Galaxy S24 FE 128GB"


productos = buscar_api_knasta(busqueda)


print("================")
print("TOTAL:", len(productos))
print("================")


for p in productos:

    titulo = p.get("title","")

    if "s24" in titulo.lower():

        print("----------------")
        print("TITULO:")
        print(titulo)

        print("RETAIL:")
        print(p.get("retail"))

        print("ID:")
        print(p.get("product_id"))

        print("URL:")
        print(p.get("url"))