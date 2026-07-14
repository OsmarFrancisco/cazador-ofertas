from knasta.buscar_producto_knasta import buscar_producto_knasta


def normalizar(texto):

    texto = texto.lower()

    eliminar = [
        '"',
        "'",
        ",",
        ".",
        "(",
        ")"
    ]

    for e in eliminar:
        texto = texto.replace(e, "")

    return texto



def calcular_match(a,b):

    palabras_a = set(
        normalizar(a).split()
    )

    palabras_b = set(
        normalizar(b).split()
    )


    comunes = palabras_a.intersection(
        palabras_b
    )


    if not palabras_a:
        return 0


    return round(
        len(comunes)
        /
        len(palabras_a)
        *
        100
    )



producto = "Samsung Galaxy S24 FE 6.7 8GB 128GB 50MP"


resultados = buscar_producto_knasta(
    producto
)


print("================")
print("BUSQUEDA")
print(producto)
print("================")


for p in resultados:

    score = calcular_match(
        producto,
        p.get("title","")
    )


    if score >= 20:

        print("----------------")
        print(
            "MATCH:",
            score,
            "%"
        )

        print(
            p.get("title")
        )

        print(
            p.get("url")
        )