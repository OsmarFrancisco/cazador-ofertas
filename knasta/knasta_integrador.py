"""
knasta_integrador.py

Une productos de ofertas.json
con información histórica de Knasta.
"""


from knasta.knasta_buscar import obtener_datos_knasta
from knasta.knasta_historial import analizar_historial



def integrar_knasta(producto):

    url = producto.get("knasta_url")


    # Si no tiene URL no hacemos nada
    if not url:

        return producto



    datos = obtener_datos_knasta(url)


    if not datos.get("ok"):

        return producto



    precio_actual = datos.get("current_price")


    historial = analizar_historial(
        datos.get("dprices", []),
        precio_actual
    )



    # =========================
    # DATOS KNasta
    # =========================

    producto["precio_actual_knasta"] = precio_actual


    producto["precio_minimo_knasta"] = historial.get(
        "precio_minimo_knasta"
    )


    producto["precio_maximo_knasta"] = historial.get(
        "precio_maximo_knasta"
    )


    producto["promedio_historico"] = historial.get(
        "promedio_historico"
    )


    producto["historial_precios_knasta"] = historial.get(
        "historial_precios",
        []
    )


    producto["diferencia_minimo_knasta"] = historial.get(
        "diferencia_minimo"
    )


    producto["porcentaje_sobre_minimo_knasta"] = historial.get(
        "porcentaje_sobre_minimo"
    )


    return producto


def integrar_lista_knasta(productos):

    resultado = []

    for producto in productos:

        try:

            producto = integrar_knasta(producto)

        except Exception as e:

            print(
                "❌ Error Knasta:",
                e
            )

        resultado.append(
            producto
        )

    return resultado


if __name__ == "__main__":


    producto_prueba = {

        "titulo":
        "Samsung Galaxy S24 FE",

        "precio":
        "S/ 1899",

        "tienda":
        "Plazavea",

        "knasta_url":
        "https://knasta.pe/detail/plazavea/20472497/smartphone-samsung-galaxy-s24-fe-67-8gb-128gb-50mp-12mp-8mp-negro?q=Samsung+Galaxy+S24"

    }


    from pprint import pprint


    resultado = integrar_knasta(producto_prueba)


    pprint(resultado)