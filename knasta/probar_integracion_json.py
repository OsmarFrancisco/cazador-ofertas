import json

from knasta.knasta_integrador import integrar_knasta


ARCHIVO = "ofertas.json"



def cargar_ofertas():

    with open(
        ARCHIVO,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def main():

    ofertas = cargar_ofertas()


    encontrados = 0


    for producto in ofertas:


        url = producto.get(
            "knasta_url"
        )


        if url:


            encontrados += 1


            print("\n====================")
            print("PRODUCTO:")
            print(producto.get("titulo"))


            resultado = integrar_knasta(
                producto
            )


            print(
                "Precio Knasta:",
                resultado.get(
                    "precio_actual_knasta"
                )
            )

            print(
                "Mínimo:",
                resultado.get(
                    "precio_minimo_knasta"
                )
            )



    print("\n====================")
    print(
        "Productos procesados:",
        encontrados
    )



if __name__ == "__main__":

    main()