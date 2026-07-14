import json
import re

from knasta.buscar_api_knasta import buscar_api_knasta
from knasta.generar_url_knasta import crear_knasta_url
from knasta.match_knasta import calcular_match


def limpiar_busqueda(titulo):

    texto = titulo.lower()


    # quitar precios tipo:
    # s/ 2099
    # 2,099
    texto = re.sub(
        r's/\s?\d+[.,]?\d*',
        '',
        texto
    )


    texto = re.sub(
        r'\b\d{1,3},\d{3}\b',
        '',
        texto
    )


    quitar = [
        "por",
        "falabella",
        "perú",
        "celular",
    ]


    for x in quitar:
        texto = texto.replace(
            x,
            ""
        )


    texto = re.sub(
        r'[^a-z0-9\s]',
        ' ',
        texto
    )


    palabras = texto.split()


    return " ".join(
        palabras[:8]
    )



with open("ofertas.json", encoding="utf-8") as f:
    datos = json.load(f)



for producto in datos:


    titulo = producto.get(
        "titulo",
        ""
    )


    if "s24 fe" not in titulo.lower():
        continue



    print("====================")
    print("PRODUCTO:")
    print(titulo)



    consulta = limpiar_busqueda(
        titulo
    )


    print()
    print("BUSQUEDA:")
    print(consulta)



    resultados = buscar_api_knasta(
        consulta
    )


    mejor = None
    mejor_score = 0



    for r in resultados:


        score = calcular_match(
            titulo,
            r.get("title","")
        )


        print(
            "CANDIDATO:",
            r.get("title"),
            "MATCH:",
            score
        )



        if score > mejor_score:

            mejor_score = score
            mejor = r



    print()


    if mejor and mejor_score >= 50:


        kn_url = crear_knasta_url(
            mejor
        )


        print(
            "✅ ELEGIDO:"
        )

        print(
            mejor.get("title")
        )


        print(
            "MATCH FINAL:",
            mejor_score
        )


        print(
            "URL KNASTA:"
        )

        print(
            kn_url
        )


    else:

        print(
            "❌ SIN MATCH BUENO"
        )