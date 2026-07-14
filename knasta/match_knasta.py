import re


PALABRAS_IGNORAR = [
    "smartphone",
    "celular",
    "telefono",
    "phone",
    "negro",
    "black",
    "graphite",
    "gris",
    "por",
    "falabella",
    "peru",
    "s/",
]


def palabras(texto):

    texto = texto.lower()


    texto = re.sub(
        r'[^a-z0-9\s]',
        ' ',
        texto
    )


    resultado = []


    for palabra in texto.split():

        if palabra not in PALABRAS_IGNORAR:

            resultado.append(
                palabra
            )


    return set(resultado)



def extraer_memoria(texto):

    texto = texto.lower()

    return re.findall(
        r'\b(64|128|256|512|1024)\s?gb\b',
        texto
    )



def calcular_match(titulo1, titulo2):


    a = palabras(titulo1)
    b = palabras(titulo2)


    if not a:
        return 0



    comunes = a.intersection(b)



    score = (
        len(comunes)
        /
        len(a)
    ) * 100



    mem1 = extraer_memoria(titulo1)
    mem2 = extraer_memoria(titulo2)



    if mem1 and mem2:

        if mem1[0] == mem2[0]:

            score += 20

        else:

            score -= 50



    return round(
        max(min(score,100),0),
        2
    )



if __name__ == "__main__":


    casos = [

        (
        "SAMSUNG Celular Galaxy S24 FE 128GB Graphite",
        "Smartphone SAMSUNG Galaxy S24 Fe 6.7 8GB 128GB 50MP Graphite"
        ),

        (
        "SAMSUNG Celular Galaxy S24 FE 256GB Black",
        "Celular Samsung Galaxy S24 FE 256GB Black+Fit3"
        )

    ]


    for a,b in casos:

        print("----------------")
        print(a)
        print(b)
        print(
            "MATCH:",
            calcular_match(a,b)
        )