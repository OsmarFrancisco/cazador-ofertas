import json
import re
import time

from knasta.buscar_api_knasta import buscar_api_knasta


ARCHIVO = "ofertas.json"


def normalizar(texto):

    texto = texto.lower()

    texto = re.sub(
        r'[^a-z0-9\s]',
        ' ',
        texto
    )

    palabras = texto.split()

    palabras = [
        p for p in palabras
        if len(p) > 2
    ]

    return set(palabras)



def calcular_match(titulo_oferta, titulo_knasta):

    a = normalizar(titulo_oferta)
    b = normalizar(titulo_knasta)

    if not a or not b:
        return 0


    comunes = a.intersection(b)


    porcentaje = (
        len(comunes) /
        len(a)
    ) * 100


    return porcentaje



def limpiar_busqueda(titulo):

    palabras_quitar = [
        "por",
        "falabella",
        "plazavea",
        "oechsle",
        "promart",
        "coolbox",
        "s/",
    ]


    titulo = titulo.lower()


    for palabra in palabras_quitar:
        titulo = titulo.replace(
            palabra,
            ""
        )


    titulo = re.sub(
        r'[^a-z0-9\s]',
        ' ',
        titulo
    )

    return " ".join(
        titulo.split()[:12]
    )


def buscar_mejor_match(producto):

    titulo_original = producto.get(
        "titulo",
        ""
    )


    consulta = limpiar_busqueda(
        titulo_original
    )


    consultas = [
        consulta
    ]


    palabras = consulta.split()


    if len(palabras) > 4:

        consultas.append(
            " ".join(
                palabras[:4]
            )
        )


    if len(palabras) > 3:

        consultas.append(
            " ".join(
                palabras[:3]
            )
        )


    resultados = []


    for c in consultas:

        print(
            "\nPROBANDO:",
            c
        )


        encontrados = buscar_api_knasta(
            c
        )


        if encontrados:

            resultados = encontrados

            break



    mejor = None

    mejor_score = 0



    for r in resultados:


        score = calcular_match(
            titulo_original,
            r.get(
                "title",
                ""
            )
        )


        if score > mejor_score:

            mejor_score = score

            mejor = r



    if mejor and mejor_score >= 65:


        return {

            "score":
                round(
                    mejor_score,
                    2
                ),

            "url":
                mejor.get(
                    "url"
                )

        }


    return None



def main():


    with open(
        ARCHIVO,
        encoding="utf-8"
    ) as f:

        productos = json.load(f)



    encontrados = 0



    for producto in productos:


        if producto.get("knasta_url"):

            continue



        resultado = buscar_mejor_match(
            producto
        )


        time.sleep(1)


        if resultado:


            producto["knasta_url"] = resultado["url"]

            encontrados += 1


            print(
                "✔",
                producto["titulo"]
            )

            print(
                "MATCH:",
                resultado["score"]
            )

            print(
                producto["knasta_url"]
            )

            print("----------------")



    with open(
        ARCHIVO,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            productos,
            f,
            ensure_ascii=False,
            indent=4
        )



    print("====================")
    print(
        "URLs Knasta agregadas:",
        encontrados
    )



if __name__ == "__main__":

    main()