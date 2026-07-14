from knasta.buscar_producto_knasta import buscar_producto_knasta


busquedas = [

    "Samsung S24 FE",

    "Galaxy S24 FE",

    "S24 FE 128GB",

    "Samsung Galaxy S24",

    "Samsung Galaxy S24 FE 128GB"

]


for b in busquedas:

    print("\n================")
    print("BUSQUEDA:", b)
    print("================")


    resultados = buscar_producto_knasta(b)


    for p in resultados[:5]:

        print(
            "-",
            p.get("title")
        )